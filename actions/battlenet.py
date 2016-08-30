from commonhelpers import app

APP_NAME = "Battle.net"
DATA_DIR = "../data/battlenet/"
# http://www.hearthhead.com/card=922&power

def start():
    app.open(APP_NAME)
    app.wait(15)


def stop():
    app.close(APP_NAME)
    app.wait(1)


def start_hearthstone():
    app.click_image(DATA_DIR + "hearthstone_icon.png")
    app.wait(10)
    app.click_image(DATA_DIR + "play_button.png")
    app.wait(25)
    app.ui.mouseclick(640, 540)
    app.wait(2)


def stop_hearthstone():
    app.close("Hearthstone")
    app.wait(5)
