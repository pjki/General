#! /usr/bin/env python

import numpy as np

import argparse

def inargs():
	"""Handle command line arguments."""

	parser = argparse.ArgumentParser(description="Quicklook data plotting")

	parser.add_argument('infile', type=str, help='a csv data file')

	args = parser.parse_args()

	return args

def extractdata(file, **keywords) :
	pass

if __name__ == '__main__':


