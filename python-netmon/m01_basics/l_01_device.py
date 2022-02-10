from pprint import pprint

# DICTIONARY representing a device
device = {
    "name": "sbx-n9kv-ao",
    "vendor": "Cisco",
    "model": "Nexus 9000 C9300v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "IP": "10.1.1.1"
}

# SIMPLE PRINT
print("\n______SIMPLE PRINT_________")
print("device: ", device)
print("device name: ", device["name"])

# PRETTY PRINT
print("\n______PRETTY PRINT_________")
pprint(device)

# NICELY FORMATTED PRINT
print("\n______FOR LOOP, USING F-STRING_________")
for key, value in device.items():
    print(f"{key:>16s} : {value}")