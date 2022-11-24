# DESCRIPTION

- Play a classic Pong game with a controller made with an Arduino Uno R3

# REQUIREMENTS

- python 3.7.7+
- Arduino IDE
- pygame
  - python3 -m pip install -U pygame --user

# HOW TO RUN (Windows 10+)

- python3 main.py
- Setup Arduino Uno R3
 ![controls](https://user-images.githubusercontent.com/60045116/203705137-60695bc9-bd9f-4a2d-8ec7-34c0dcf9b566.png)
 
- Plug Uno R3 into computer
- Upload sketch into Arduino Uno R3
- Download Flip 3.4.7 (install instructions in ArduinoHIDKeyboard >> FLIP install)
- Short the pins indicated in the picture above
 ![short](https://user-images.githubusercontent.com/60045116/203705104-ddfe3398-ca22-4c25-8c8f-587575c5bee2.png)
 
- Go to Device Manager and the Arduino R3 should be labeled as Arduino Uno
- Right click and select "Update Driver"
- Select "Browse for drivers on your computer" >> Local Disk >> Program Files(x86) >> Atmel >> Flip 3.4.7 >> usb >> ok
- Make sure "Include subfolders" is checked. Click Next >> Close. Arduino Uno should now say ATmega16U2
- Open Flip >> Select Communication Medium >> USB
- Navigate to File >> Load Hex File. Import Keyboard from ArduinoHIDKeyboard (ArduinoHIDKeyboard >> HEX >> KeyboardFirmware >> Arduino-keyboard-0.3.hex)
- Initiate the flash then unplug Arduino Uno R3
- Plug it back in and ATmega16U2 should no longer be visible. There should be another HID Keyboard under Keyboard. This indicates it now is registered as a keyboard

# CREATED BY

- Austin Sohn
- Ethan Luu
