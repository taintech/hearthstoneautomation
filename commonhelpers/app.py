import subprocess
import time


def open(name):
    subprocess.call(
            ["/usr/bin/open", "-W", "-n", "-a", "/Applications/" + name + ".app"]
    )


def wait(seconds):
    time.sleep(seconds)


def close(name):
    subprocess.call(['osascript', '-e', 'tell application "' + name + '" to quit'])
