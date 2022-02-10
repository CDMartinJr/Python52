from random import choice
import string
from tabulate import tabulate


def create_devices(num_devices=1, num_subnets=1):
    # CREATE LIST OF DEVICES
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets requested")
        return created_devices

    for subnet_index in range(1, num_subnets+1):
        for device_index in range (1, num_devices+1):

            # CREATE DEVICE DICTIONARY
            device = dict()

            # RANDOM DEVICE NAME
            device["name"] = (
                    choice(["r2", "r3", "r4", "r6", "r10"])
                    + choice(["L", "U"])
                    + choice(string.ascii_letters)
            )

            # RANDOM VENDOR FROM CHOICE OF CISCO, JUNIPER, AND ARISTA
            device["vendor"] = choice(["Cisco", "Juniper", "Arista"])
            if device["vendor"] == "Cisco":
                device["OS"] = choice(["ios", "iosexe", "iosxr", "nexus"])
                device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).10"])
            elif device["vendor"] == "Juniper":
                device["OS"] = "Junos"
                device["version"] = choice(["J6.23.1", "RL345.06", "P3.CPO"])
            elif device["vendor"] == "Arista":
                device["OS"] = "Eos"
                device["version"] = choice(["2.45", "2.63", "3.08"])
            device["IP"] = "10.0." + str(subnet_index) + "." + str(device_index)

            created_devices.append(device)

        return created_devices


# MAIN PROGRAM
if __name__ == "__main__":

    devices = create_devices(num_devices=10, num_subnets=5)
    print("\n", tabulate(devices, headers="keys"))
