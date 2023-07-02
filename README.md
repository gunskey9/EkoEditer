# EkoEdit - A File Editing Tool

EkoEdit is a command-line file editing tool designed to manipulate and modify text files containing domain names or URLs. It offers various options to customize and clean up the data within the file. The tool uses common Linux commands and subprocesses to perform the operations efficiently.

## Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x

### Installation

There is no formal installation process required for EkoEdit. Simply download the Python script and run it using the Python interpreter.

```bash
$ python ekedit.py
```

## Usage

1. Upon running the script, the terminal screen will be cleared, and the ASCII art representation of "EkoEdit" will be displayed.

2. You will be prompted to enter the name or location of the file you want to edit.

3. The script will then present a list of options to perform different editing tasks on the file:

    - Edit spaces between entries
    - Add "https" to each domain
    - Erase extra characters from the domain list
    - Remove "http" from sites in the list
    - Edit domains into bare URLs
    - Edit out all numbers before the domain
    - Edit out extra extensions (suffixes)
    - Edit out all extra commas in the file
    - Edit out all numbers in the file
    - Edit out URL parameters
    - Delete specific text from the file
    - Get the IP address of each domain
    - Check the status code of each domain
    - Edit out repeat domains

4. Enter the number corresponding to the editing task you wish to perform or 'Q' to quit the program.

5. After performing the selected operation, you will be prompted to enter the name of the new file to save the changes. Press Enter to overwrite the original file.

6. If you chose to save the changes with a new filename, the script will create a new file containing the edited data.

## Example

Suppose you have a file named `domains.txt` containing a list of domain names like this:

```
example.com
https://example.org
sub.domain.net
```

You can use EkoEdit to edit this file:

```bash
$ python ekedit.py
```

Enter the filename: `domains.txt`

Now, you can choose the desired operation, say option '2' to add "https" to each domain. After completing the edit, you will be prompted to enter a new filename to save the changes or press Enter to overwrite the original file.

## Note

- Always make a backup of your original file before using EkoEdit for editing to avoid accidental data loss.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

EkoEdit was created with love by [Your Name]. Special thanks to the contributors and the open-source community for their invaluable support and feedback.

If you have any suggestions, bug reports, or feature requests, please feel free to contact us or create an issue in the repository. Happy editing!
