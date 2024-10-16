# Hen Fishman - TelegramHashBot
A telegram bot that calculates the hash of jpg/jpeg images.

## Project Overview
This telegram bot calculates the sha256 hash of jpg/jpeg images, denying any text message or other types of files. The tests included showcase these capabilities, using ADB to automate the test cases.

### Supported platforms
This project was developed on and for Windows 10, and the test cases on Android (specifically developed on Xiaomi 13T, but shouldn't be an issue to other android phones). Others using different OS's can utilize the included docker to run the project, but will have to make sure to download the appropriate version of ADB for their system first.

## Running The Project
### Prerequisites
Before attempting to use the project, you must first download telegram and have an account, enable developer options and download ADB to run the test cases.

To enable developer mode, go to your Android's "About" section in the settings, and continuously tap on the "OS version"/"Build number"/something similar until a prompt informing you that developer mode is on appears.
Then, go back to settings and find "Developer options" or something similar, and enable "USB Debugging" and "USB Debugging (Security settings)" (if you have it, if not it's all good not every Android does), and your phone should be ready for the testing, just plug it into the computer via USB and you should be set.

To download ADB, first visit https://developer.android.com/tools/releases/platform-tools and download the version for your machine. The rest of the instructions are about the Windows version specifically.
After the zip finishes downloading extract the folder to a location suitable for you (doesn't matter where), and open the CMD in the folder.
the the following command to start the ADB server:
```cmd
adb start-server
```
Then, to check if your phone is connected, type the following command:
```cmd
adb devices
```
You should see an ID and device written next to it, similar to this:
```cmd
List of devices attached
5k1I31d1        device
```
It is likely that instead of device you will see 'inaccessible' or a similar message, and your phone will prompt you asking if you want to allow the computer's request to use its debugging mode. Simply allow and run the command again, and you should see that it now writes device next to the ID properly.

After this, you should be ready to run the project.

### How To Run
#### Method 1 - Using the source directly, only for Windows

#### Method 2 - Using the docker
