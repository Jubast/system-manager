import subprocess
import re
from clients.base import *

def list_monitors():
    command = [ "ddcutil", "detect" ]
    output = run(command)

    i2c_pattern = "I2C bus:.*?\/dev\/i2c-([0-9])"
    i2c_matches = re.findall(i2c_pattern, output) 

    model_pattern = "Model:\s*(.*)"
    model_matches = re.findall(model_pattern, output)

    monitors = []
    index = 0
    for match in i2c_matches:
        monitors.append(to_object({
            "i2c_addr": match,
            "model": model_matches[index]
            }))
        index += 1

    return monitors

def set_vcp(bus, addr, value):
    print("/dev/i2c-" + str(bus) + " set " + str(addr) + " to " + str(value))
    command = [ "ddcutil", "setvcp", "--bus", bus, addr, value ]
    output = run(command)
