from random import choice
import string


def created_devices(num_devices=1, num_subnets=1):

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


def create_network(num_devices=1, num_subnets=1):
    devices = created_devices(num_devices, num_subnets)
    network = dict()
    network["subnets"] = dict()

    for device in devices:
        subnet_address_bytes = device["IP"].split(".")
        subnet_address_bytes[3] = "0"
        subnet_address = ".".join(subnet_address_bytes)

    if subnet_address not in network["subnets"]:
        network["subnets"][subnet_address] = dict()
        network["subnets"][subnet_address]["devices"] = list()

    network["subnets"][subnet_address]["devices"].append(device)

    interfaces = list()
    for index in range(0, choice([2, 4, 8])):
        interface = {
            "name": "g/0/0/" + str(index),
            "speed": choice(["10", "100", "1000"])
        }
        interfaces.append(interface)

    device["interfaces"] = interfaces

    return network