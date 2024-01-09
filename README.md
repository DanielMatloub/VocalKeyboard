# VocalKeyboard: A Voice-Controlled Python Script for Basic System Control and Web Navigation

This Python script demonstrates a voice-controlled interface using the Speech Recognition library (speech_recognition) along with pyautogui, platform, and webbrowser modules. The script allows users to control their system and navigate to specific websites using voice commands.

Dependencies:
speech_recognition
pyautogui

System Commands:
Move cursor ('left', 'right', 'up', 'down')
Open new windows or switch between different pages
Perform specific actions like typing, clicking, searching, and scrolling

Website Navigation:
Open various websites directly using voice commands ('open google', 'open youtube', etc.)

Instructions for Use:
Ensure the necessary libraries (speech_recognition, pyautogui) are installed.
Run the script in a Python environment.
The script initializes listening for voice commands and adjusts for ambient noise.
Speak one of the predefined commands to control system functions or navigate to specific websites.

Code Structure Overview:
moveCommands, hotkeyCommands, websiteCommands: Dictionaries mapping voice commands to corresponding actions for cursor movement, hotkey commands, and website URLs respectively.
callback Function: Recognizes voice commands using Google Speech Recognition, performs associated actions based on recognized commands.
main Execution: Initializes microphone, starts background listening for voice commands, and continuously executes the loop until an "off" command is received.

Additional Notes:
Modify or expand the dictionaries (moveCommands, hotkeyCommands, websiteCommands) to add new voice commands or functionalities.
The script will continuously listen for voice commands until the "stop listening" command is recognized or the script is terminated.

Note: Ensure proper microphone access and environment configuration for accurate voice recognition and system interaction.
