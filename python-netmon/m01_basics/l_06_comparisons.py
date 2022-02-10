from utils.create_utils import created_devices
from pprint import pprint
from random import randint, uniform
from datetime import datetime
from copy import copy
from copy import deepcopy

devices = created_devices(num_subnets=2, num_devices=25)
print("\n      NAME      VENDOR : OS      IP ADDRESS      LAST_HEARD")
print("       -----     -------  ----    --------------  -------------")
for device in devices:
    print(
        f'{device["name"]:>7}  {device["vendor"]:>10}   {device["OS"]:<6}   {device["IP"]:<15}   {device["version"]}'
    )

print("\n      NAME      VENDOR : OS      IP ADDRESS      LAST_HEARD")
print("       -----     -------  ----    --------------  -------------")
for device in devices:
    if device["vendor"].lower()== "cisco":
        print(
            f'{device["name"]:>7}  {device["vendor"]:>10}   {device["OS"]:<6}   {device["IP"]:<15}   {device["version"]}'
    )

print("\n--------------Comparison of device names--------------")
for index, device_a in enumerate(devices):
    for device_b in devices[index+1:]:
        if device_a["name"] == device_b["name"]:
            print(f"Found match! {device_a['name']} for both {device_a['IP']} and {device_b['IP']}!")
print("-----------Device name comparison is complete-----------")

print("\n\n-----Create list of arbitrary 'standard' versions for each vendor : OS------")
standard_versions=dict()
for device in devices:
    vendor_os = device["vendor"] + ":" + device["OS"]
    if vendor_os not in standard_versions:
        standard_versions[vendor_os] = device["version"]
pprint(standard_versions)

print("\n\n------Create list of non-compliant devices for each vendor: OS------")
non_compliant_devices = dict()
for vendor_os, _ in standard_versions.items():
    non_compliant_devices[vendor_os] = []

for device in devices:
    vendor_os = device["vendor"] + ":" + device["OS"]
    if device["version"] != standard_versions[vendor_os]:
        non_compliant_devices[vendor_os].append(device["IP"] + " version: " + device["version"])

pprint(non_compliant_devices)

print("\n\n ------Assignment, copy, and deep copy------")
devices2 = devices
devices[0]["name"] = "This is a dumb device name"
if devices2 == devices:
    print("\n  Assignment and modifications: devices2 STILL equals devices")
    print("   ---->Moral: Assignment is NOT the same as copy")
else:
    print("     Huh?")

devices2 = copy(devices)
devices2[0]["name"] = "This is also a dumb device name"
if devices2 == devices:
    print("\n  Shallow copy and modifications: devices2 STILL equals devices")
    print("    ----> Moral: copy() only does a shallow (1st level) copy")
    print("    Result: Oops, I just screwed up the original version!")

devices2 = deepcopy(devices)
devices2[0]["name"] = "This is also a dumb device name"
if devices2 == devices:
    print("    Huh?")
else:
    print("\n     Deep copy and modifications: devices2 no longer equals devices")
    print("    ----> Moral: deepcopy() gives you a complete copy of the original")
    print("    Result: I can do whatever I want with my copy, without touching the original!")

new_set_of_devices = created_devices(num_subnets=2, num_devices=25)
if new_set_of_devices == devices:
    print("    Huh?")
else:
    print("\n    Comparisons of complex, deep data is easy in Python")
    print("    -----> Moral: You can compare any two data structures, regardless of complexity")

print("\n\n----------Comparisons for implementing SLAs----------\n")
SLA_Availability = 96
SLA_Response_Time = 1.0

devices = created_devices(num_devices=25, num_subnets=2)
for device in devices:

    device["availability"] = randint(94, 100)
    device["response_time"] = uniform(0.5, 1.1)

    if device["availability"] < SLA_Availability:
        print(f"{datetime.now()}: {device['name']:6} - Availability {device['availability']} < {SLA_Availability}")
    if device["response_time"] > SLA_Response_Time:
        print(f"{datetime.now()}: {device['name']:6} - Response time {device['response_time']:.3f} > {SLA_Response_Time}")

print("\n\n--------Comparing Classes-------")


class DeviceWithEq:

    def __init__(self, name, ip):
        self.name = name
        self.ip_address = ip

    def __eq__(self, other):
        if not isinstance(other, DeviceWithEq):
            return False
        return self.name == other.name and self.ip_address == other.ip_address


d1 = DeviceWithEq("device 1", "10.10.10.1")
d1_equal = DeviceWithEq("device 1", "10.10.10.1")
d1_different = DeviceWithEq("device 2", "10.10.10.2")

print("\n Comparison with an __eq__ method to handle evaluation")
if d1 == d1_equal:
    print(f"    ---> Using __eq__ : {d1} equals {d1_equal}")
else:
    print(f"      !!! Using __eq__ : Uh-oh! Classes are not equal and they should be!")

if d1 == d1_different:
    print(f"    !!! Using __eq__ : Uh-oh! Classes are equal and they should not be!")
else:
    print(f"      ---> Using __eq__ : {d1} not equal to {d1_different}")


class DeviceWithNoEq:

    def __init__(self, name, ip):
        self.name = name
        self.ip_address = ip


d1 = DeviceWithNoEq("device 1", "10.10.10.1")
d1_equal = DeviceWithNoEq("device 1", "10.10.10.1")
d1_same = d1

print("\n    Comparison WITHOUT an __eq__ method to handle evaluation")
if d1 == d1_equal:
    print(f"      !!! with no __eq__ : Oops!  Didn't expect this!")
else:
    print(f"    ---> With no __eq__ : Success! Not equal, as expected!")

if d1 == d1_same:
    print(f"    ---> With no __eq__ : Success! {d1} points to same object instance as {d1_same}.")
else:
    print("    !!!! With no __eq__ : Oops, I didn't expect this!")
