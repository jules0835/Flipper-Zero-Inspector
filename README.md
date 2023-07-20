# Flipper Zero Inspector 0.1.0

## Disclaimer
Only test on MacOS. Need modification for Windows.
This project is a work in progress and is not finished yet. I am not a professional developer, it is possible that there are errors in the code. If you find any issues or have any suggestions, please let me know.

## Description
Flipper Zero Inspector is a Python script designed to inspect and check the functionality of a Flipper Zero device. The script connects to the Flipper Zero via USB and performs various tests to ensure that different components of the device are working correctly.

### What is the purpose of this program ?
This project is currently aimed at testing your own pinball machine. In the future, the number of second-hand pinball machines being resold is expected to increase. The purpose of this project will be to test a pinball machine before selling it or when one wishes to buy one. It could also serve as a foundation for a company looking to refurbish used pinball machines and ensure they are functioning properly.

## Requirements
To run this script, you need to have the following:

- Python 3 installed on your system.
- The `pyflipper` library, which provides the necessary functionality to interact with the Flipper Zero.

## Usage
1. Make sure you have Python 3 installed on your computer.
2. Install the required `pyflipper` library using the following command:
```
pip install pyflipper
```
3. Connect your Flipper Zero device to your computer via USB.
4. Run the `flipper_inspector.py` script using the following command:
```
python flipper_inspector.py
```
5. The script will automatically detect the connected Flipper Zero device and begin the inspection.

## Features
- Tests the vibration motor.
- Checks the functionality of the LEDs (Red, Green, and Blue).
- Checks the screen functionality by changing the screen brightness.
- Displays device information, including hardware model, firmware version, serial number, Bluetooth MAC.

## How to Use
1. Connect your Flipper Zero device to your computer using a USB cable.
2. Run the script as described in the Usage section above.
3. Follow the on-screen instructions to perform the inspection.
4. The script will provide feedback on the status of different components of the Flipper Zero.
5. If any issues are detected, they will be displayed at the end of the inspection.

## Note
- This script is intended for personal use and is not guaranteed to work perfectly.
- The developer is not responsible for any damages that may occur while running this script.
- Use this script at your own risk.

## To Do
- Checks the NFC functionality by detecting a NFC card (emulation option commented out).
- Sends and receives an IR signal to test the IR functionality.
- Checks the brightness of the device screen.

## Author
Contact me if you have any questions or suggestions.

## Feedback
If you encounter any issues or have suggestions for improvement, please let me know by raising an issue on this repository.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as you see fit.
