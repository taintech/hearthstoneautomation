import os
import subprocess
import time
import quartzcoregraphics as ui
import opencv as ai

RUNTIME_DIR = "../data/runtime/"


def open(name):
    subprocess.call(
            ["/usr/bin/open", "-n", "-a", "/Applications/" + name + ".app"]
    )


def wait(seconds):
    time.sleep(seconds)


def close(name):
    subprocess.call(['osascript', '-e', 'tell application "' + name + '" to quit'])


def screenshot():
    path = RUNTIME_DIR + "screenshot.png"
    os.system("screencapture -x " + path)
    return path


def click_image(template):
    x, y = ai.find(template, screenshot())
    ui.mouseclick(x,y)
