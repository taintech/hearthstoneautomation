from commonhelpers import app

APP_NAME = "OBS"
DATA_DIR = "../data/obs/"


def start():
    app.open(APP_NAME)
    app.wait(2)


def stop():
    app.close(APP_NAME)
    app.wait(1)


def start_recording():
    app.click_image(DATA_DIR + "start_recording.png")
    app.wait(1)


def stop_recording():
    app.click_image(DATA_DIR + "app_icon.png")
    app.wait(1)
    app.click_image(DATA_DIR + "stop_recording.png")
    app.wait(2)
