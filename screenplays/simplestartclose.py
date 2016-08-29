from actions import battlenet
from actions import obs


obs.start()
obs.start_recording()
battlenet.start()
battlenet.start_hearthstone()
battlenet.stop_hearthstone()
battlenet.stop()
obs.stop_recording()
obs.stop()
