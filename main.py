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
import pathlib
from JsonSerialiser import JsonSerialiser
from PersonalData import PersonalData


def main(arg_parser):
    """ Main entry point of the app """

    args, filenames = arg_parser.parse_known_args()

    if args.list_formats:
        print("Supported formats:", ["json", "xml", "pickle"])
        return

    if args.test:
        pytest.main("test_pserialise.py")
        return

    if len(filenames) == 0:
        print("No filenames specified.", file=sys.stderr)
        arg_parser.print_help(file=sys.stderr)
        return

    # process given files
    input_filename, *output_filenames = filenames

    with open(input_filename, "r") as f:
        serialised_data = f.read()

    # process source format
    serialiser = get_serialiser(get_extension(input_filename))
    data = serialiser.deserialise(serialised_data, PersonalData)

    # process output format
    if len(output_filenames) == 0:
        print("No ouput file specified, printing to stdout.\n", file=sys.stderr)
        for entry in data:
            print("{}".format(entry.name))
            print("{}".format("".join("-" for _ in entry.name)))
            print("ad: {}".format(entry.address))
            print("ph: {}".format(entry.phone))
            print()

    else:
        for filename in output_filenames:
            process_output(data, filename)


def interactively_read_data():
    print("Starting interactive session:")
    name = input("name: ")
    address = input("address: ")
    phone_number = input("phone number: ")
    return PersonalData(name, address, phone_number)


def get_extension(path_string):
    return pathlib.Path(path_string).suffix[1:]


def get_serialiser(format):
    if format == "xml":
        pass
    elif format == "pickle":
        pass
    elif format == "json":
        return JsonSerialiser
    else:
        print("Unknown output file format: \"{}\"".format(format), file=sys.stderr)
        exit(1);


def process_output(data, output_filename):
    serialiser = get_serialiser(get_extension(output_filename))
    serialised_data = serialiser.serialise(data)
    with open(output_filename, "w") as f:
        f.write(serialised_data)


def usage_message(name=None):
    return "main.py [-h] [-t] [-l] [-v] source_file [target_file ...]" + \
            "\nnote: formats are determined by file extension." + \
            " For supported extensions, see --list-formats"


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser(usage=usage_message())

    # Optional argument flag which defaults to False
    parser.add_argument("-t", "--test", action="store_true", default=False)

    # Optional argument flag which defaults to False
    parser.add_argument("-l", "--list-formats", action="store_true", default=False)

    # Specify output of "--version"
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    main(parser)
