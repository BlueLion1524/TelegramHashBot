from ppadb.client import Client as AdbClient
from time import sleep


BOT_USERNAME = "@JpegHashBot"


def enter_bot_chat(device):
    """Enters the chat with the bot once in the telegram landing page

    Args:
        device (Device): The device to enter the chat with the bot in
    """
    device.shell("input tap 1150 170")
    device.shell(f'input text "{BOT_USERNAME}"')
    sleep(1)
    device.shell("input tap 590 360")
    sleep(1)


def main():
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.devices()[0]

    # Creating directory with test files on the phone
    device.shell("mkdir /sdcard/JpegHasherTestFiles")
    device.push("TestFile.jpg", "/sdcard/JpegHasherTestFiles/TestFile.jpg")
    device.push("TestFile.png", "/sdcard/JpegHasherTestFiles/TestFile.png")

    device.shell("am start -n org.telegram.messenger/org.telegram.messenger.DefaultIcon") # Open telegram
    sleep(0.5)

    enter_bot_chat(device)
    device.shell('input text "Texting Test Case"')
    sleep(0.3)
    device.shell("input tap 1150 1630")

    # The send action lets you send something somewhere, using the stream extra directive makes it send a file specified by the URI given in stream,
    # and the package name afterwards directs it to where it should be sent.
    # I specified application/octet-stream instead of image/png because telegram compresses all pictures sent on it and makes them jpg's, this way
    # it doesn't know it's an image and sends it as a file, as is.
    device.shell('am start --user 0 -a android.intent.action.SEND -t application/octet-stream --eu android.intent.extra.STREAM file:///sdcard/JpegHasherTestFiles/TestFile.png org.telegram.messenger')
    sleep(0.5)
    enter_bot_chat(device)
    device.shell("input tap 1115 2440")
    sleep(0.5)
    device.shell("input tap 1110 2490")
    sleep(0.5)

    device.shell('am start --user 0 -a android.intent.action.SEND -t image/jpeg --eu android.intent.extra.STREAM file:///sdcard/JpegHasherTestFiles/TestFile.jpg org.telegram.messenger')
    sleep(0.5)
    enter_bot_chat(device)
    device.shell("input tap 1115 2440")
    sleep(0.5)
    device.shell("input tap 1110 2490")

    # Cleaning up the test files
    device.shell("rm -r /sdcard/JpegHasherTestFiles")


if __name__ == "__main__":
    main()