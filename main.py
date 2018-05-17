#!/usr/bin/env python3
"""
pSerialise, command line utility for serialising and deserialising personal data
"""

__author__ = "Callum Howard"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import pytest
import sys
from JsonSerialiser import JsonSerialiser
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
        return

    if args.test:
        pytest.main("test_pserialise.py")
        return

    if args.format == "xml":
        pass
    elif args.format == "pickle":
        pass
    else:  # args.format == "json":
        serialiser = JsonSerialiser

    if args.deserialise:
        with open(args.target_filename, "r") as f:
            serialised_data = f.read()

        data = serialiser.deserialise(serialised_data, PersonalData)
        print(data)

    else:
        data = interactively_read_data()
        serialised_data = serialiser.serialise(data)
        with open(args.target_filename, "w") as f:
            f.write(serialised_data)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("target_filename", help="filename to read or write")

    # Optional argument flag which defaults to False
    parser.add_argument("-d", "--deserialise", action="store_true", default=False)

    # Optional argument flag which defaults to False
    parser.add_argument("-t", "--test", action="store_true", default=False)

    # Optional argument flag which defaults to False
    parser.add_argument("-l", "--list-formats", action="store_true", default=False)

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--format", action="store", dest="format")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
