from tabulate import tabulate
from utils.create_utils import created_devices

# _____________MAIN PROGRAM _____________________
if __name__ == "__main__":

    devices = created_devices(num_subnets=5, num_devices=4)
    print("\n", tabulate(devices, headers="keys"))

