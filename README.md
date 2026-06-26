# Terminal

A lightweight terminal application written in Python.

This project is a personal terminal/shell made for learning Python and experimenting with command-line utilities. It includes basic file management commands, system information, and a built-in file downloader with a progress bar.

## Features

* Lightweight
* Colored terminal output
* File management commands
* Built-in downloader with progress bar
* Cross-platform Python code
* Simple and easy to extend

## Commands

| Command          | Description                                                                        |
| ---------------- | ---------------------------------------------------------------------------------- |
| `stats`          | Display system information such as username, hostname, current directory and time. |
| `help`           | Help menu *(Work in Progress)*                                                     |
| `echo <text>`    | Print text to the terminal.                                                        |
| `exit`           | Exit the terminal.                                                                 |
| `whoami`         | Show the current username.                                                         |
| `pwd`            | Display the current working directory.                                             |
| `version`        | Display the terminal version.                                                      |
| `clear`          | Clear the terminal screen.                                                         |
| `ls`             | List files and folders.                                                            |
| `cat <file>`     | Display the contents of a file.                                                    |
| `date`           | Display the current date.                                                          |
| `color <color>`  | Change the terminal output color.                                                  |
| `touch <file>`   | Create an empty file.                                                              |
| `reload`         | Reload the terminal interface.                                                     |
| `rm <file>`      | Delete a file.                                                                     |
| `write <text>`   | Write text into a file.                                                            |
| `download <url>` | Download a file from the internet with a progress bar.                             |
| `os`             | Display the operating system name.                                                 |

## Installation

Clone the repository:

```bash
git clone https://github.com/reyaansh72/MyBash-Python.git
```

Go into the project folder:

```bash
cd MyBash-Python
```

Install dependencies:

```bash
pip install requests
```

Run the terminal:

```bash
python app.py
```

## Example

```text
reyaansh@fedora:/home/reyaansh/Terminal$ ls
app.py  Utils

reyaansh@fedora:/home/reyaansh/Terminal$ download https://example.com/file.zip
File Name To Save as: file.zip
[██████████████████████████████] 100.0%
Downloaded file.zip
```

## Project Goals

* Learn Python
* Learn how command-line shells work
* Build a simple but useful terminal application
* Continue adding new commands and features

## Version

**v1.0 Stable**

## License

This project is released under the MIT License.
