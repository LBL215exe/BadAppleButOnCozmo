# Bad Apple on Cozmo

## Overview
"Bad Apple" is an engaging project that animates the Cozmo robot to perform a rendition of the popular song and animation. This README outlines how to set up and run the project using the Cozmo SDK.

## Requirements
•	Python 3.6 or higher: Download from python.org. 	
•	Cozmo Robot: A physical Cozmo robot is necessary to execute the program.

## Installation
	
### 1.	Clone the Repository:

Open a terminal and run:
 git clone https://github.com/LBL215exe/BadAppleButOnCozmo.git
cd BadAppleButOnCozmo
  	
### 2.	Install Required Packages:

 pip install -r requirements.txt
  	
### 3.	Connect to Cozmo:

Ensure your Cozmo robot is powered on and connected to the same Wi-Fi network as Cozmo showed.
Running the Program
	
### 1.	Start the Cozmo SDK and Play Bad Apple:

Follow the SDK documentation [Here](https://cozmosdk.anki.bot)

Open a terminal and run:
 python3 badapple.py
The main functionality is contained within the badapple.py script. Here’s a brief overview of the main components
  
### BadApple.py

 Key Functions
	
  •	cozmo_program: This function contains the main thing for animating Cozmo in sync with the "Bad Apple" audio track. You can modify this function to customize Cozmo's movements and interactions.

Troubleshooting
	
  •	Connection Issues: Ensure Cozmo is on and connected to the same network as your Device runing the app. 	
  
  •	Performance Lag: Close unnecessary applications to improve performance.

### Contributing

Contributions are welcome! Feel free to submit issues or pull requests for improvements.

## License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.
