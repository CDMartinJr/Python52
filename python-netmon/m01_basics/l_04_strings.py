from pprint import pprint

device1_str = " r3-L-n7, Cisco, catalyst 2960, ios "

# SPLIT
print("STRING STRIP, SPLIT, REPLACE")
device1 = device1_str.split(",")
print("device1 using split")
print("    ", device1)

# STRIP
device1 = device1_str.strip().split()
print("device1 using strip and split")
print("    ", device1)

# REMOVE BLANKS
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split: \n", device1)

# REMOVE BLANKS, CHANGE COMMA TO COLON
device1_str_colon = device1_str.replace(" ", ",").replace(",", ":")
print("device1 replaced blanks, commas to colons")
print("    ", device1_str_colon)

# LOOP WITH STRIP AND SPLIT
device1 = list()
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and strip for each item:")
print("    ", device1)

# STRIP AND SPLIT, SINGLE LINE USING LIST COMPREHENSION
device1 = [item.strip() for item in device1_str.split(",")]
print("device using list comprehension:")
print("    ", device1)

# IGNORING CASE
print("\n\n Ignoring Case:")
model = "CSR1000V"
if model == "csr1000v":
    print(f"matched {model}")
else:
    print(f"Didn't match {model}")

model = "CSR1000V"
if model.lower == "csR1000v".lower():
    print(f"Matched using lower(): {model}")
else:
    print(f"Didn't match {model}")

# FINDING SUBSTRING
print("\n\nFinding Substrings:")
version = "Virtual XE Software (X86_64_Linux_IOSD_UNIVERSALK9_M), Version 16.11.1a, Release Software (fcl)"
expected_version = "Version 16.11.1a"
index = version.find(expected_version)
if index >= 0:
    print(f"Found version: {expected_version} at location {index} ")
else:
    print(f"Not found: {expected_version}")

# SEPARATING STRING COMPONENTS
print("\n\n Separating Version String Components")
version_info = version.split(",")
for part_no, version_info_part in enumerate(version_info):
    print(f"Version part: {part_no}: {version_info_part.strip()}")

# show_interface_stats =