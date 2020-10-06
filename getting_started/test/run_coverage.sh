#!/usr/bin/env bash

# Change to the directory where this script lives
SCRIPT_DIR=$(dirname $0)
cd $SCRIPT_DIR

# Add executable and python program to respective paths
export PATH=../bin:$PATH
export PYTHONPATH=../src:$PYTHONPATH

# Generate the coverage report for your code
COVERAGE_REPORT=$(mktemp)
coverage run -m --source ../src/funprog unittest discover unit_tests -p "*test.py" -b
coverage report -m > $COVERAGE_REPORT

cat $COVERAGE_REPORT
rm -f $COVERAGE_REPORT
