from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list()  # CREATE EMPTY LIST FOR HOLDING DEVICES

# FOR LOOP TO CREATE LARGE NUMBER OF DEVICES
for index in range(1, 10):

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
    device["IP"] = "10.10.10." + str(index)

    # NICELY FORMATTED PRINT FOR EACH DEVICE
    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")

    # ADD THIS DEVICE TO THE LIST OF DEVICES
    devices.append(device)

# USE PPRINT TO PRINT DATA AS-IS
pprint("\n-----------DEVICES AS LIST OF DICTIONARIES-------------")
pprint(devices)

# USE 'TABULATE' TO CREATE TABLE OF DEVICES
print("\n---------SORTED DEVICES IN TABULAR FORMAT--------------")
print(tabulate(sorted(devices, key=itemgetter("vendor", "OS", "version")), headers="keys"))