import csv
import re
import argparse
import os
import pyperclip

def extract_ips(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        ips = set()  # use a set to automatically de-duplicate IPs
        ip_pattern = re.compile(
            r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')
        for row in reader:
            for field in row:
                matches = ip_pattern.findall(field)
                if matches:
                    ips.update(matches)
    return ips


def search_directory(directory):
    ips = set()  # use a set to automatically de-duplicate IPs
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            ips.update(extract_ips(os.path.join(directory, file)))
    return ips


def recursive_search(directory):
    ips = set()  # use a set to automatically de-duplicate IPs
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                ips.update(extract_ips(os.path.join(root, file)))
    return ips


def main():
    parser = argparse.ArgumentParser(
        description='Search for IP addresses in CSV files.')
    parser.add_argument('-d', '--directory',
                        help='Base directory to search for CSV files.')
    parser.add_argument(
        '-f', '--file', help='Specific CSV file to search for IP addresses.')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Recursively search through directories.')
    args = parser.parse_args()

    # Clean up directory and file path inputs
    if args.file:
        args.file = args.file.rstrip('\\').rstrip('"')
    if args.directory:
        args.directory = args.directory.rstrip('\\').rstrip('"')

    # Process the inputs
    ips = set()
    if args.file:
        try:
            ips = extract_ips(args.file)
        except PermissionError:
            print("You used -f... Please specify a file, not a directory")
        except OSError:
            print("Remove trailing \\ from path")
    elif args.directory:
        if args.recursive:
            ips = recursive_search(args.directory)
        else:
            try:
                ips = search_directory(args.directory)
            except OSError:
                print("Remove trailing \\ from path")

    # Copy IPs to clipboard
    pyperclip.copy('\n'.join(ips))


if __name__ == '__main__':
    main()
