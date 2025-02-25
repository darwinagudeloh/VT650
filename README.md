# **Fluke® VT650 Data Capture Application**

This application provides a graphical interface to capture, process, and visualize data from the **Fluke VT650** device. It supports real-time data acquisition, plotting, and saving of pressure, flow, and volume data into a CSV file. The application also allows users to save the generated graphs.

## Requirements

- **Fluke VT650** with firmware version **2.04**.
- Python 3.7 or higher.
- Dependencies listed in `requirements.txt`.

## License

This project is licensed under the **GNU General Public License (GPL)**. See the [LICENSE](LICENSE) file for details.

---

## **Setup Instructions**

### 1. Create a Virtual Environment

To avoid conflicts with system-wide Python packages, it is recommended to create a virtual environment.

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Activate the Virtual Environment

#### On Windows:
```bash
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---
## **Usage Instructions**


### 1. Configure the Fluke VT650
  1. Zero the Device: Before starting, ensure the Fluke VT650 is zeroed using the local button on the device.

  2. Set Sampling Rate: Use the device's menu to configure the desired sampling rate.

  3. Connect the Device: Connect the Fluke VT650 to your computer via the serial port.

### 2. Configure the Application
  1. Select Serial Port: Enter the serial port (e.g., `COM3` on Windows or `/dev/ttyUSB0` on Linux) in the "Serial Port" field.

  2. Configure the Device: Click the Config button to establish communication with the Fluke VT650.

### 3. Start Data Capture
  1. Start Capture: Click the Start button to begin capturing data. The application will start receiving and plotting pressure, flow, and volume data in real time.

  2. Stop Capture: Click the Stop button to end the data capture. The captured data will be automatically saved to a CSV file, and the file path will be displayed in the "File Path" field.

### 4. Save the Graph
After stopping the capture, the Save Graph button will be enabled. Click it to save the displayed graph as an image file.

---
## **Important Notes**
 - **Data Capture:** The application only captures pressure, flow, and volume data.

 - **Device Behavior:** After stopping the capture in the application, the Fluke VT650 will continue sending data until the local button on the device is pressed.

 - **File Naming:** The CSV file is automatically named using the current Unix timestamp (e.g., `1633072800.csv`).

___

## **Dependencies**
The following Python packages are required:

 - `pyserial` for serial communication.

 - `matplotlib` for data visualization.

 - `pandas` for data processing and CSV export.

 - `pyside6` for the graphical user interface.

These dependencies are listed in the `requirements.txt` file.

---

## **Troubleshooting**
 - **Serial Port Issues:** Ensure the correct serial port is selected and the Fluke VT650 is properly connected.

 - **Firmware Version:** The application is designed for Fluke VT650 devices with firmware version 2.04. Using a different firmware version may cause compatibility issues.

 - **Data Loss:** If the application is closed or crashes during data capture, data may be lost. Always stop the capture properly before closing the application.

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Acknowledgments
- This project was developed to facilitate data acquisition and visualization for the Fluke VT650 device.
- Special thanks to the **GIBIC Research Group** at the **University of Antioquia** for their support and collaboration.
- Thanks to the open-source community for providing the tools and libraries used in this project.
___

For any questions or issues, please contact the project maintainer.
- Name: Darwin Agudelo - Email: darwinaguhe@gmail.com