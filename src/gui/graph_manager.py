import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QGraphicsScene

class GraphManager:
    def __init__(self, max_seconds=30):
        self.max_seconds = max_seconds
        self.samplerate = None
        self.df = pd.DataFrame(columns=["Presion", "Flujo", "Volumen", "ID"])
        self.fig = None
        self.axes = {}
        self.canvas = None
        self.scene = QGraphicsScene()
        
    def setup_plots(self, graphics_view):
        """Configura las gráficas iniciales"""
        self.fig, (self.axes['Presion'], self.axes['Flujo'], self.axes['Volumen']) = plt.subplots(3, 1, figsize=(7.7, 5.7))
        self.fig.tight_layout(pad=3.0)
        self.canvas = FigureCanvas(self.fig)
        self.scene.addWidget(self.canvas)
        graphics_view.setScene(self.scene)
        
        # Configurar ejes
        for ax in self.axes.values():
            ax.set_xlabel('Tiempo (s)')
            ax.relim()
            ax.autoscale_view()
            
        self.axes['Presion'].set_ylabel('cmH2O')
        self.axes['Flujo'].set_ylabel('lpm')
        self.axes['Volumen'].set_ylabel('l')

    def set_samplerate(self, samplerate):
        """Actualiza la frecuencia de muestreo y ajusta el buffer"""
        self.samplerate = float(samplerate)
        max_samples = int(self.samplerate * self.max_seconds)
        
        # Redimensionar el DataFrame manteniendo los últimos datos
        self.df = self.df.tail(max_samples - 1)

    def update_data(self, new_row):
        """Actualiza los datos con buffer circular"""
        if self.samplerate is None:
            return
            
        max_samples = int(self.samplerate * self.max_seconds)
        
        # Añadir nueva fila
        self.df.loc[len(self.df)] = new_row
        
        # Mantener el tamaño máximo
        if len(self.df) > max_samples:
            self.df = self.df.iloc[-max_samples:]

    def update_plots(self):
        """Actualiza las gráficas con los datos actuales"""
        if self.df.empty or self.samplerate is None:
            return
            
        # Calcular eje de tiempo
        self.df['Tiempo'] = (self.df['ID'].astype(int) / self.samplerate) - \
                           (self.df['ID'].iloc[-1] / self.samplerate - self.max_seconds)

        # Actualizar cada gráfica
        for i, (name, ax) in enumerate(self.axes.items()):
            ax.clear()
            ax.plot(self.df['Tiempo'], self.df[name], label=name, color=['r', 'g', 'b'][i])
            ax.set_title(f'Gráfica de {name}')
            ax.relim()
            ax.autoscale_view()
            
        self.canvas.draw()