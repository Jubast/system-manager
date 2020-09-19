import subprocess
from clients.base import *

def list_domains():
    command = ["virsh", "-c", "qemu:///system", "list", "--name", "--all"]
    output = run(command)

    domains = []
    lines = output.splitlines()
    for line in lines:
        if not line:
            continue

        domains.append(to_object({
            "name", line
            }))

    return domains


def attach_device_live(host_name, file):
    command = ["virsh", "-c", "qemu:///system", "attach-device", host_name, "--file", file, "--live"]
    output = run(command)

def detach_device_live(host_name, file):
    command = ["virsh", "-c", "qemu:///system", "detach-device", host_name, "--file", file]
    output = run(command)
