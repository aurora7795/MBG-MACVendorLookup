#!/usr/bin/env python3
"""Simple tool for determining the vendor associated with a MAC Address"""

# TODO: Replace shebang as means of executing via command line:
#  I've used a shebang above to make this tool easier to run at the command line (with some adjustments to the
#  permissions but a better means of making the tool usable at the command line is likely possible that is more
#  portable. Would investigate if i had more time. Current workaround is to run 'chmod 755 vendorFromMac.py' to make
#  executable with './vendorFromMac.py'

import requests
import argparse

# Using the argument parser to handle arguments sent into the app
parser = argparse.ArgumentParser()
parser.add_argument("mac_address", help="MAC Address to interrogate", type=str)
args = parser.parse_args()


def get_vendor(mac_address: object) -> str:
    """
    Gets the vendor of a device based on a MAC address
    Note:
    structure of address validated at server end, will return error if not formatted correctly.

    :param mac_address: The MAC address to interrogate
    :return: Vendor information
    """

    # TODO: Implement encryption of API Key:
    #  API key is present in a file but not encrypted. Dabbled with python
    #  encryption techniques but could not get working in reasonable timescale
    apikey = open("apiKey", "r").read()
    url = f'https://api.macaddress.io/v1?apiKey={apikey}&output=vendor&search={mac_address}'
    x = requests.get(url)
    return x.text


# Simple main
if __name__ == '__main__':
    f = open("apiKey", "r")
    vendor = get_vendor(args.mac_address)
    print(vendor)
