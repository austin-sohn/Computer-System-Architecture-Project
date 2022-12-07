# Description
- Classic games designed with Python and a game controller made with an Arduino Uno R3
- There are 4 buttons to use as the movement keys

# Hardware
- Arduino Uno R3
- Buttons 
- 220 ohm resistor
- Breadboard
- Jumper wires
- Jumper cap (or anything conductive/metal)

# Software:
- Python 3.7+ (pygame)
  - Linux
    - sudo apt-get install python3-pygame
  - Macos
    - python3 -m pip install -U pygame --user
- Arduino IDE
- Flip 3.4.7

# How to Setup Arduino:
- Setup Arduino Uno R3 as seen below  
 ![controls](https://user-images.githubusercontent.com/60045116/206090993-5dfa6c51-c538-4e79-ad8f-b7ad86a5a300.png)

- Plug Uno R3 into computer
- Type “python3 main.py” into terminal
- Upload sketch into Arduino Uno R3 using the Arduino IDE
- Download Flip 3.4.7 (install instructions in ArduinoHIDKeyboard >> FLIP install)
- Short the pins as indicated in the picture below  
 ![short](https://user-images.githubusercontent.com/60045116/206091070-d1b6b21a-3399-4fc9-acfc-3cbadca6c49f.png)

- Go to Device Manager and the Arduino R3 should be labeled as Arduino Uno
- Right click and select "Update Driver"
- Select "Browse for drivers on your computer" >> Local Disk >> Program Files(x86) >> Atmel >> Flip 3.4.7 >> usb >> OK
- Make sure "Include subfolders" is checked. Click Next >> Close. Arduino Uno should now say ATmega16U2
- Open Flip >> Select Communication Medium >> USB
- Navigate to File >> Load Hex File. Import Keyboard from ArduinoHIDKeyboard (ArduinoHIDKeyboard >> HEX >> KeyboardFirmware >> Arduino-keyboard-0.3.hex)
- Initiate the flash then unplug Arduino Uno R3
- Plug it back in and ATmega16U2 should no longer be visible. There should be another HID Keyboard under Keyboard. This indicates it now is registered as a keyboard

# How to Run
  - python3 main_menu.py
# Pong
  - Player 1 Controls
    - w: up
    - s: down
  - Player 2 Controls
    - o: up
    - l: down
# Space Invaders
  - Controls:
    - w: up
    - s: down
    - o: left
    - l: right
# Definitely Not Super Mario
  - Controls:
    - w: jump
    - s: crouch
    - o: left
    - l: right
# Created By:
- Austin Sohn
- Ethan Luu
