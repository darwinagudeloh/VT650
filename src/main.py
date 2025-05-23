import sys
import time
import pandas as pd
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt  # Importar pyplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsScene, QFileDialog
from PySide6.QtCore import QTimer, QThread, Signal
from gui.main_window import Ui_MainWindow
from hardware import SerialManager, SerialManagerError

class SerialThread(QThread):
    data_received = Signal(str)  # Señal para emitir los datos recibidos

    def __init__(self, serial_manager):
        super().__init__()
        self.serial_manager = serial_manager
        self.running = True

    def run(self):
        while self.running:
            line = self.serial_manager.read_line()
            if line:
                self.data_received.emit(line)

    def stop(self):
        self.running = False

class PlotUpdateThread(QThread):
    update_plot_signal = Signal()
    
    def __init__(self, interval=50):
        super().__init__()
        self.interval = interval  # en milisegundos
        self.running = True

    def run(self):
        while self.running:
            self.update_plot_signal.emit()
            self.msleep(self.interval)  # Dormir en milisegundos

    def stop(self):
        self.running = False        

class VT650App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # load ui file
        
        # serial port
        self.serial_manager = SerialManager()

        # Init config
        #self.serial_conn = None
        self.data = []
        self.df = pd.DataFrame(columns=["Presion", "Flujo", "Volumen", "ID"])
        self.start_time = None
        self.stop_time = None
        self.samplerate = None

        # Conectar eventos de los botones
        self.bconfig.clicked.connect(self.config_serial)
        self.bstart.clicked.connect(self.start_capture)
        self.bstop.clicked.connect(self.stop_capture)
        self.bsgrap.clicked.connect(self.guardar_grafica)

        # Configurar gráficas
        self.ax1 = None 
        self.ax2 = None
        self.ax3 = None
        self.setup_plots()

        # List serial ports and populate combo box
        self.populate_serial_ports()

        # Actualizar valores cada 250 ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_values)
        self.timer.start(200)

        # Iniciar thread para actualizar la gráfica
        self.plot_thread = PlotUpdateThread(interval=200)
        self.plot_thread.update_plot_signal.connect(self.update_plot)
        self.plot_thread.start()

    def setup_plots(self):
        # Crear un layout para el widget contenedor de la gráfica
        self.fig, (self.ax_x, self.ax_y, self.ax_z) = plt.subplots(3, 1, figsize=(7.7, 5.7))
        self.fig.tight_layout(pad=3.0)

        # Crear el canvas a partir de la figura
        self.canvas = FigureCanvas(self.fig)

        # Crear una escena de gráficos y agregar el canvas
        scene = QGraphicsScene()
        scene.addWidget(self.canvas)
        
        # Asignar la escena al QGraphicsView (gvdata)
        self.gvdata.setScene(scene)

    def populate_serial_ports(self):
        ports = self.serial_manager.list_available_ports()
        self.cbserial.clear()  # clear combo box
        default_port = "/dev/ttyUSB0"
        default_index = -1

        for i, port in enumerate(ports):
            self.cbserial.addItem(port.device)
            if port.device == default_port:
                default_index = i
        
        if default_index != -1:
            self.cbserial.setCurrentIndex(default_index)   

    def config_serial(self):

        # verificar si fue seleccionado la rata de muestreo
        if self.action25_Hz.isChecked():
            self.samplerate = "25"
            self.action50_Hz.setEnabled(False)
            self.action100_Hz.setEnabled(False)
            self.action150_Hz.setEnabled(False)
            self.action200_Hz.setEnabled(False)
        elif self.action50_Hz.isChecked():
            self.samplerate = "50"
            self.action25_Hz.setEnabled(False)
            self.action100_Hz.setEnabled(False)
            self.action150_Hz.setEnabled(False)
            self.action200_Hz.setEnabled(False)
        elif self.action100_Hz.isChecked():
            self.samplerate = "100"
            self.action25_Hz.setEnabled(False)
            self.action50_Hz.setEnabled(False)
            self.action150_Hz.setEnabled(False)
            self.action200_Hz.setEnabled(False)
        elif self.action150_Hz.isChecked():
            self.samplerate = "150"
            self.action25_Hz.setEnabled(False)
            self.action50_Hz.setEnabled(False)
            self.action100_Hz.setEnabled(False)
            self.action200_Hz.setEnabled(False)
        elif self.action200_Hz.isChecked(): 
            self.samplerate = "200"
            self.action25_Hz.setEnabled(False)
            self.action50_Hz.setEnabled(False)
            self.action100_Hz.setEnabled(False)
            self.action150_Hz.setEnabled(False)
        else:
            self.action25_Hz.setEnabled(True)
            self.action50_Hz.setEnabled(True)
            self.action100_Hz.setEnabled(True)
            self.action150_Hz.setEnabled(True)
            self.action200_Hz.setEnabled(True)
            QMessageBox.critical(self, "Error", "Por favor, selecciona una tasa de muestreo " 
                                 "en el menu de configuracion.")
            return

        port = self.cbserial.currentText()
        if not port:
            QMessageBox.critical(self, "Error", "Por favor, ingresa un puerto serial válido.")
            return

        try:
            port = self.cbserial.currentText()
            if not self.serial_manager.connect(port, self.samplerate):
                QMessageBox.critical(self,"Error", "No se pudo establecer la conexión con el Fluke VT650. UARTFAST-2")
                return

            print(f"puerto configurado")
            # Habilitar botones
            self.bconfig.setEnabled(False)
            self.bstart.setEnabled(True)
            QMessageBox.information(self, "Configuración", "Puerto serial configurado correctamente.")
            
            # Configurar el equipo
            # @todo toda esta parte cambiara.
            # se implementara lectura por comando y no por stream
            self.serial_manager._configure_device(self.samplerate)

            # Habilitar botones
            self.bconfig.setEnabled(False)
            self.bstart.setEnabled(True)
            self.bstop.setEnabled(False)
            #QMessageBox.information(self, "Configuración", "Puerto serial configurado correctamente.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el puerto serial: {e}")

    def start_capture(self):
        if not self.serial_manager.serial_conn:
            QMessageBox.critical(self, "Error", "Primero configura el puerto serial.")
            return

        self.df = pd.DataFrame(columns=["Presion", "Flujo", "Volumen", "ID"])
        self.start_time = time.time()
        self.capturing = True

        # Iniciar el hilo para recibir datos
        self.serial_thread = SerialThread(self.serial_manager)
        self.serial_thread.data_received.connect(self.process_line)
        self.serial_thread.start()
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        # Iniciar la captura de datos
        self.serial_manager.serial_conn.write(b'STREAMIDX\n')
        self.serial_manager.serial_conn.flush()

        # Habilitar/deshabilitar botones
        self.bstart.setEnabled(False)
        self.bstop.setEnabled(True)
        self.bsgrap.setEnabled(False)
        QMessageBox.information(self, "Captura", "Captura de datos iniciada.")
    
    def process_line(self, line):
        try:
            values = line.strip('\r').split(',')
            self.df.loc[len(self.df)] = values
            #self.update_plot()
        except ValueError:
            print(f"Error al procesar la línea: {line}")
    
    def update_plot(self):
        if not self.df.empty:
            # Extraer los últimos 500 datos
            df_plot = self.df.tail(500)
            
            # Calcular el eje x en segundos
            sample_rate = float(self.samplerate)  # Asegurarse de que samplerate sea un número
            df_plot.loc[:, 'Tiempo'] = df_plot['ID'].astype(int) / sample_rate  # Crear columna 'Tiempo'

            self.ax_x.clear()
            self.ax_y.clear()
            self.ax_z.clear()

            self.ax_x.plot(df_plot["Tiempo"], df_plot["Presion"], label="Presion", color='r')
            self.ax_x.set_title('Gráfica de Presion')
            self.ax_x.set_xlabel('Tiempo (s)')
            self.ax_x.set_ylabel('cmH2O')
            self.ax_x.legend()
            self.ax_x.yaxis.set_major_locator(ticker.MaxNLocator(5))
            self.ax_x.relim()
            self.ax_x.autoscale_view()
            #y_min = self.df["Presion"].min()
            #y_max = self.df["Presion"].max()
            #self.ax_x.set_ylim(y_min, y_max)

            

            self.ax_y.plot(df_plot["Tiempo"], df_plot["Flujo"], label="Flujo", color='g')
            self.ax_y.set_title('Gráfica de Flujo')
            self.ax_y.set_xlabel('Tiempo (s)')
            self.ax_y.set_ylabel('lpm')
            self.ax_y.legend()
            self.ax_y.yaxis.set_major_locator(ticker.MaxNLocator(5))
            self.ax_y.relim()
            self.ax_y.autoscale_view()
            #fmin = self.df["Flujo"].min()
            #fmax = self.df["Flujo"].max()
            #self.ax_y.set_ylim(fmin, fmax)


            self.ax_z.plot(df_plot["Tiempo"], df_plot["Volumen"], label="Volumen", color='b')
            self.ax_z.set_title('Gráfica de Volumen')
            self.ax_z.set_xlabel('Tiempo (s)')
            self.ax_z.set_ylabel('l')
            self.ax_z.legend()
            self.ax_z.yaxis.set_major_locator(ticker.MaxNLocator(5))
            self.ax_z.relim()
            self.ax_z.autoscale_view()

            self.canvas.draw()

    def stop_capture(self):
        if not self.serial_manager.serial_conn:
            QMessageBox.critical(self, "Error", "No hay conexión serial activa.")
            return

        self.serial_thread.stop()
        self.plot_thread.stop()
        #self.serial_manager.serial_conn.write(b'LOCAL\n')
        self.stop_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        # Guardar los datos en un archivo CSV
        encabezado = [f"Inicio: {self.start_time}", 
                      f"Final: {self.stop_time}",
                      f"Rata de muestreo: {self.samplerate}"
                      ]
        self.file_path = f"{int(time.time())}.csv"
        with open(self.file_path, 'w') as f:
            for line in encabezado:
                f.write(line + '\n')
            self.df.to_csv(f, index=False, mode='a')
        
        self.lefilename.setText(self.file_path)

        # Habilitar/deshabilitar botones
        self.bconfig.setEnabled(True)
        self.bstop.setEnabled(False)
        self.bsgrap.setEnabled(True)
        QMessageBox.information(self, "Captura", "Captura de datos detenida y guardada.")

    def update_values(self):
        if not self.df.empty:
            last_row = self.df.iloc[-1]
            try:
                self.lepression.setText(f"{float(last_row['Presion']):.2f}")
                self.leflow.setText(f"{float(last_row['Flujo']):.2f}")
                self.levol.setText(f"{float(last_row['Volumen']):.2f}")
            except Exception:
                pass

    def guardar_grafica(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Guardar gráfica", "",
                                              "Imágenes PNG (*.png);;Imágenes JPG (*.jpg)", options=options)
        if filename:
            self.fig.savefig(filename)
            QMessageBox.information(self, "Gráfica guardada", "La gráfica se ha guardado correctamente.")        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VT650App()
    window.show()
    sys.exit(app.exec())