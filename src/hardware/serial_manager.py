import serial
import serial.tools.list_ports
import time

class SerialManagerError(Exception):
    pass

class SerialConnectionError(SerialManagerError):
    pass

class SerialCommandError(SerialManagerError):
    pass

class SerialManager:
    def __init__(self):
        self.serial_conn = None
        self.current_baudrate = 115200
        self.default_commands = {
            'remote': b'REMOTE\n',
            'uart_fast': b'UARTFAST=TRUE\n',
            'meas': b'MEAS=AW\n',
            'mpraw': b'MPRAW=TRUE\n',
            'mflaw': b'MFLAW=TRUE\n',
            'mvol': b'MVOL=TRUE\n',
            'stream': b'STREAMIDX\n',
            'local': b'LOCAL\n'
        }

    def list_available_ports(self):
        """Lista los puertos seriales disponibles"""
        return sorted(serial.tools.list_ports.comports(), key=lambda port: port.device)

    def connect(self, port, samplerate):
        """Establece la conexión con el dispositivo"""
        try:
            # Primer intento de conexión
            self._basic_connect(port, 115200)
            
            # Configuración inicial
            self._send_command('remote')
            response = self.read_line()
            
            if response != 'RMAIN':
                self._reconnect_fast_baud(port)
                self._send_command('remote')
                response = self.read_line()
                if response != 'RMAIN':
                    return False
            elif response == 'RMAIN':
                self._reconnect_fast_baud(port)
                response = self._read_response()
                if 'A' in response:
                    self._send_custom_command('A')
                    time.sleep(0.01)
                else:
                    return False

            # Configuración avanzada
            #self._configure_device(samplerate)
            return True
            
        except Exception as e:
            raise SerialConnectionError(f"Connection failed: {str(e)}")

    def _basic_connect(self, port, baudrate):
        """Conexión básica con parámetros iniciales"""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
        self.serial_conn = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=1,
            rtscts=True
        )
        self.current_baudrate = baudrate
        time.sleep(0.1)

    def _reconnect_fast_baud(self, port):
        """Reconexión con baudrate más alto"""
        self._send_command('uart_fast')
        time.sleep(0.01)

        self._basic_connect(port, 921600)
        self.serial_conn.reset_input_buffer()
        self.serial_conn.reset_output_buffer()
        time.sleep(0.01)
        
    def _configure_device(self, samplerate):
        """Configuración del dispositivo"""
        commands = [
            'meas', 'mpraw', 'mflaw', 'mvol',
            ('mfreq', f'MFREQ={samplerate}\n')
        ]
        
        for cmd in commands:
            if isinstance(cmd, tuple):
                self._send_custom_command(cmd[1])
            else:
                self._send_command(cmd)
            
            response = self.read_line()
            if response != '*':
                raise SerialCommandError(f"Command {cmd} failed")

    def _send_command(self, command_key):
        """Envía un comando predefinido"""
        if command_key not in self.default_commands:
            raise SerialCommandError(f"Unknown command: {command_key}")
        
        self.serial_conn.write(self.default_commands[command_key])
        time.sleep(0.05)

    def _send_custom_command(self, command):
        """Envía un comando personalizado"""
        self.serial_conn.write(command.encode())
        time.sleep(0.05)

    def _read_response(self, char_count=2):
        """Lee la respuesta del dispositivo"""
        return self.serial_conn.read(char_count).decode('utf-8')

    def disconnect(self):
        """Cierra la conexión serial"""
        if self.serial_conn and self.serial_conn.is_open:
            self._send_command('local')
            self.serial_conn.close()

    def write_read(self, command):
        """Envía un comando y lee la respuesta"""
        self._send_command(command)
        return self._read_response()

    def start_streaming(self):
        """Inicia el streaming de datos"""
        self._send_command('stream')

    def read_line(self):
        """Lee una línea del puerto serial"""
        return self.serial_conn.readline().decode('utf-8').strip()
        