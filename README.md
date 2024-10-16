# Hen Fishman - TelegramHashBot
A telegram bot that calculates the hash of jpg/jpeg images - will be made a private repository after review.

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
Run the following command to start the ADB server:
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

### How To Run The Bot
#### Method 1 - Using the source directly, only for Windows
In order to run the bot on your machine, follow these steps:

1. **Open Git Bash and clone the repository:**
    ```bash
    git clone https://github.com/BlueLion1524/TelegramHashBot.git
    ```
    
2. **In the cloned folder, open a CMD window and install the requirements:**
    ```cmd
    pip install -r NsoDockerFiles/requirements.txt
    ```

3. **Run the bot:**
    ```cmd
    python3 JpegHashBot.py
    ```
4. **To stop the bot, simply press Ctrl+C.**

#### Method 2 - Using the docker
In order to run the docker and the bot on it, follow these steps:

1. **Open Git Bash and clone the repository:**
    ```bash
    git clone https://github.com/BlueLion1524/TelegramHashBot.git
    cd TelegramHashBot
    ```
    
2. **Load the docker image:**
    ```bash
    docker load -i NsoDockerImage.tar
    ```
    
3. **Run a container with the loaded image in the background:**
    ```bash
    docker run -d 31fce0b12c42
    ```
    
4. **To kill and clean up the container and the bot, find the container's ID first:**
    ```bash
    docker ps
    ```

5. **Copy the CONTAINER ID in the row where the IMAGE is 31fce0b12c42, and run the commands:**
    ```bash
    docker kill <CONTAINER ID>
    docker rm <CONTAINER ID>
    ```

### How To Run The Tests
#### Method 1 - Using the source directly, only for Windows
Assuming you are running the bot and cloned the repository, to run the tests open a CMD window in the repository folder and follow these steps:

1. **If you ran the bot using the docker, and therefore have not installed the requirements yet, install the requirements:**
    ```cmd
    pip install -r NsoDockerFiles/requirements.txt
    ```
    
2. **Run the tests (make sure the ADB server is running and your phone is connected):**
    ```cmd
    Python3 BotTester.py
    ```

#### Method 2 - Using the docker
To run the tests from inside the docker, which I don't really recommend but suit yourself, follow these steps (assuming you ran the bot on the docker):

1. **Go to where you put the ADB files, open a terminal there, and run the ADB server as nodaemon:**
    ```bash
    adb kill-server
    adb -a nodaemon server start
    ```
    
2.  **Find the container ID to run bash in it:**
    ```bash
    docker ps
    ```
    
3.  **Enter bash in the container:**
    ```bash
    docker exec -it <CONTAINER ID> bash
    ```
    
4.  **Inside the container's bash, run the tests:**
    ```bash
    python3 source/BotTester.py
    ```
