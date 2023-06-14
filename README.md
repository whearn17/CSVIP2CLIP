# CSVIP2CLIP
## Introduction
CSVIP2CLIP is a Python script for searching for IP addresses in CSV files. It's capable of searching through a single file or a directory of files, and can optionally perform a recursive search through subdirectories. The IP addresses it finds are directly copied to the system clipboard for convenient use.

## Requirements
To run CSVIP2CLIP , you will need Python 3.6 or later. The script also requires the following Python package:

* pyperclip
  
You can install the necessary packages with pip:

```
pip install pyperclip
```
## Usage
You can run CSVIP2CLIP from the command line with the following syntax:
```
python CSVIP2CLIP.py -f <file> 
python CSVIP2CLIP.py -d <directory>
python CSVIP2CLIP.py -rd <directory>
```
* -f : Specifies a single CSV file to search for IP addresses.

* -d : Specifies a directory of CSV files to search for IP addresses.

* -r: If specified, the script will recursively search through subdirectories of the specified directory.

Note: There seems to be an issue with the Argparse module - when adding a \ to the end of an argument with a quote will make the quote actually appear as part of the argument which breaks the program. To fix this, either don't put any arguments after the file/directory that you input, or dont put a trailing backslash.

## Contributing
Contributions to CSVIP2CLIP are welcome. Please open an issue to discuss your proposed changes before submitting a pull request.

## License
CSVIP2CLIP is licensed under the MIT License.
