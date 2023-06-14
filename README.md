# CSV IP Finder
## Introduction
CSV IP Finder is a Python script for searching for IP addresses in CSV files. It's capable of searching through a single file or a directory of files, and can optionally perform a recursive search through subdirectories. The IP addresses it finds are used to gather geolocation information from the IP-API service. The geolocation information can be printed to the console or saved to a CSV file.

## Requirements
To run CSV IP Finder, you will need Python 3.6 or later. The script also requires the following Python packages:

* requests

You can install the necessary packages with pip:

```
pip install requests
```
## Usage
You can run CSV IP Finder from the command line with the following syntax:
```
python CSVIP2GEO.py -f <file> 
python CSVIP2GEO.py -d <directory>
python CSVIP2GEO.py -d <directory> -r
python CSVIP2GEO.py -d <directory> --csv <output.csv>
```
* -f <file>: Specifies a single CSV file to search for IP addresses.

* -d <directory>: Specifies a directory of CSV files to search for IP addresses.

* -r: If specified, the script will recursively search through subdirectories of the specified directory.

* --csv <output.csv>: If specified, the script will write the geolocation information to the specified CSV file instead of printing it to the console.

Note: Be sure to enclose file paths in quotes if they contain spaces.

## Contributing
Contributions to CSV IP Finder are welcome. Please open an issue to discuss your proposed changes before submitting a pull request.

## License
CSV IP Finder is licensed under the MIT License. See the LICENSE file for details.
