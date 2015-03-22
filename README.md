# yac2qc

yet another csv 2 qif convertor

## about

This is a simple tool to convert bank statements in the csv
format to the [Quicken Interchange format
(QIF)](https://en.wikipedia.org/wiki/Quicken_Interchange_Format)
as used by accounting software such as
[GnuCash](http://www.gnucash.org/). It is written for
conversion of the statements that you can download from
mijning.nl, but it should be easily modifiable to support
other formats.

To my knowledge, the main difference between this tool and
the many existing tools is that this tool tries to maintain
all information in the original statement by storing it in
the 'memo' field of the QIF record. A potential problem with
this approach is that it is harder for GnuCash to recognize
the individual statements as being part of a certain account.
The tool yac2qc solves this by assigning a 'category' to each
QIF transaction that can be used by GnuCash to map the
transactions to specific accounts more easily.

The assignment of categories is not 'automatic'. Instead, the
user has to define their own categories and rules for
assigning transactions to these categories. The fact that you
have to define your own rules can be a pain in the beginning,
but once you have a proper set of rules I find the
deterministic approach preferable over some heuristics to map
transactions to categories. If this doesn't appeal to you,
use one of the other tools (just search csv2qif on github).

Note: this tool is in no way related to any bank or any other
company. It is just a simple tool that I've created to make
my own life easier when importing bank account statements
into GnuCash. I hope it helps you too, but I'm not
responsible if it leads to corrupted data or any other
problems you may encounter by using this tool. See 'licence'
for a disclaimer.

## licence

The MIT Licence. See the file LICENCE for details.

## requirements

This was written for python3. No additional modules should be
required.

## usage

The tool consists of two files: yac2qc.py and rules.py. The
file yac2qc.py contains the actual program and the file
rules.py contains category mapping rules. The default
rules.py contains some very simple rules that mainly serve as
an example on how to define your own rules. When no rules are
defined, the default behaviour is to assign the category
'unspecified' to each record.

A note about the configuration file: Instead of defining a
configuration file format and having to parse this, I figured
that a simple python file with declarative rules is probably
just as simple to modify for end-users, so the file rules.py
is just a very simple python file. The list of rules (named
'rules') is imported by the yac2qc.py tool upon execution.

Usage examples:

	$ ./yac2qc.py -h
	usage: yac2qc.py [-h] [-o OUTFILE] [-u] INFILE

	convert csv files from your bank account to QIF format.

	positional arguments:
	  INFILE      csv file to convert

	optional arguments:
	  -h, --help  show this help message and exit
	  -o OUTFILE  destination file
	  -u          print records for which category is unknown.

	example usage:
	 yac2qc.py -o statements.qif statements.csv
	 yac2qc.py -u statements.csv

	configuration:
	 define your own category rules in rules.py

