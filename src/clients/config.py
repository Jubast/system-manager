import json
import os
from clients.base import *

KEYBOARD = "virsh_keyboard.xml"
MOUSE = "virsh_mouse.xml"
AUDIO = "virsh_audio.xml"
BLUETOOTH = "virsh_bluetooth.xml"

def configuration_directory():
    file_path = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(os.path.dirname(file_path))

    return os.path.join(root_dir, "config")

def monitors_configuration():
    directory = configuration_directory()
    config = os.path.join(directory, "monitors.json")

    with open(config) as json_file:
        data = json.load(json_file)
    
    items = []
    for item in data:
        items.append(to_object(item))
    return items 

def device_configuration_path(device_file_name):
    directory = configuration_directory()
    config = os.path.join(directory, device_file_name)
    return config
