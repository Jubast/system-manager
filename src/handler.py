from clients import config, ddc, usb, virsh

def handle_switch(machine, type):
    if machine == "linux":
        if type == "clean":
            switch_linux("win10_clean_gaming")

        if type == "sketchy":
            switch_linux("win10_sketchy_gaming")

    if machine == "windows":
        if type == "clean":
            switch_windows("win10_clean_gaming")

        if type == "sketchy":
            switch_windows("win10_sketchy_gaming")

def switch_linux(domain):
    # devices
    virsh.detach_device_live(domain, 
            config.device_configuration_path(config.KEYBOARD))
    virsh.detach_device_live(domain, 
            config.device_configuration_path(config.MOUSE))
    virsh.detach_device_live(domain, 
            config.device_configuration_path(config.AUDIO))
    virsh.detach_device_live(domain, 
            config.device_configuration_path(config.BLUETOOTH))

    # monitors
    switch_monitors("linux")

def switch_windows(domain):
    # devices
    virsh.attach_device_live(domain,
            config.device_configuration_path(config.KEYBOARD))
    virsh.attach_device_live(domain,
            config.device_configuration_path(config.MOUSE))
    virsh.attach_device_live(domain,
            config.device_configuration_path(config.AUDIO))
    virsh.attach_device_live(domain,
            config.device_configuration_path(config.BLUETOOTH))

    # monitors
    switch_monitors("windows")

def switch_monitors(type):
    monitors_config = config.monitors_configuration()
    monitors = ddc.list_monitors()

    for monitor in monitors:
        for monconf in monitors_config:
            if monconf.model == monitor.model:
                address = monconf.address
                for conf in monconf.configurations:
                    if conf["name"] == type:
                        value = conf["value"]
                        ddc.set_vcp(monitor.i2c_addr, address, value)
                        break
                break
