import os
import subprocess
import time

def wifi_connected(host="8.8.8.8", port=53, timeout=3):
    try:
        subprocess.check_output(["ping", "-c", "1", host], timeout=timeout)
        return True
    except subprocess.CalledProcessError:
        pass
    return False

if __name__ == "__main__":

    while not wifi_connected():
        print("connection waiting")
        time.sleep(5)  

    print("connection established, running bot")


    os.system("python3 bot.py")