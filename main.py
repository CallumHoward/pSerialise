#!/usr/bin/env python3
"""
pSerialise, command line utility for serialising and deserialising personal data
"""

__author__ = "Callum Howard"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import pytest
from PersonalData import PersonalData


def interactively_read_data():
    print("Starting interactive session:")
    name = input("name: ")
    address = input("address: ")
    phone_number = input("phone number: ")
    return PersonalData(name, address, phone_number)


def main(args):
    """ Main entry point of the app """

    if args.list_formats:
        print("Supported formats:", ["json", "xml", "pickle"])

    if args.test:
        pytest.main("test_pserialise.py")

    #TODO if file not specified in args, create data to serialise interactively
    data = interactively_read_data()
    #TODO serialise



if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Optional argument flag which defaults to False
    parser.add_argument("-t", "--test", action="store_true", default=False)

    # Optional argument flag which defaults to False
    parser.add_argument("-l", "--list-formats", action="store_true", default=False)

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
