import subprocess
from clients.base import *

def list_usb_devices():
    command = [ "lsusb" ]
    output = run(command)

    devices = []
    lines = output.splitlines()
    for line in lines:
        if not line:
            continue

        tokens = line.split(" ")
        if len(tokens) < 6:
            continue

        ids = tokens[5].split(":")
        if len(ids) != 2:
            continue

        name = ""
        for token in tokens[6:]:
            name += token + " "

        devices.append(to_object({
            "name": name,
            "vendor_id": ids[0],
            "product_id": ids[1]
            }))

    return devices
