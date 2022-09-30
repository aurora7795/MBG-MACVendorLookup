# MBG-MACVendorLookup
MBG-MACVendorLookup is a utility that allows users to do lookups of device vendors based on a MAC address.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed the latest version of Python3
* You have a *nix machine. This was developed on Mac for use on similar environments. Milage with Windows may vary.

## Using MBG-MACVendorLookup

To use MBG-MACVendorLookup, follow these steps:

Navigate to the location of the script and run:

```
python ./vendorFromMac.py {MAC address to check}
```

For example:
```
python ./vendorFromMac.py 44:38:39:ff:ef:57
```

Example Output:
```
Cumulus Networks, Inc
```

The program will return null if the program is given a valid MAC address but cannot find a vendor to match:
```
python ./vendorFromMac.py 00:38:39:ff:ef:00
```
Example Output:
```

```

The program will inform the user if the MAC Address is malformed or missing:
```
python ./vendorFromMac.py invalid_input
```
Example Output:
```
Invalid MAC or OUI address was received.
```

## Contributors

Thanks to the following people who have contributed to this project:

* [@aurora7795](https://github.com/aurora7795) 📖

## Contact

If you want to contact me you can reach me at m.bradford.gago@me.com.

## License
This project uses the following license: MIT Licence(https://spdx.org/licenses/MIT.html).
