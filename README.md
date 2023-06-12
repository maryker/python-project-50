### Hexlet tests and linter status:
[![Actions Status](https://github.com/maryker/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/maryker/python-project-50/actions)

![tests and linter](https://github.com/maryker/python-project-50/actions/workflows/pyci.yml/badge.svg)

[![Test Coverage](https://api.codeclimate.com/v1/badges/cb1325fe2b6e3134d6da/test_coverage)](https://codeclimate.com/github/maryker/python-project-50/test_coverage)

[![Maintainability](https://api.codeclimate.com/v1/badges/cb1325fe2b6e3134d6da/maintainability)](https://codeclimate.com/github/maryker/python-project-50/maintainability)


## About

This program makes diff of two files (json and yml).

## Installation

To install this programm use this commands:
```
make build
make install
make package-install
```

## Usage

To get help use

`gendiff -h`

To make diff of two files use

`gendiff path/to/file1.json path/to/file2.json`

You can change style of result diff. To do that use flag -f. 

`gendiff -f stylish path/to/file1.json path/to/file2.json`

You can choose from:
+ stylish
+ plain
+ json

## Demonstration:
[![asciicast](https://asciinema.org/a/jjvccILVSJeO9qf6LTWbyhqE6.svg)](https://asciinema.org/a/jjvccILVSJeO9qf6LTWbyhqE6)