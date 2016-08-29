from commonhelpers import app

APP_NAME = "Battle.net"


def start():
    app.open(APP_NAME)
    app.wait(7)


def stop():
    app.close(APP_NAME)


def start_hearthstone():
    # TODO implement this method
    pass


def stop_hearthstone():
    # TODO implement this method
    pass
