# Py Unittest Walkthrough

This repository is designed to be a learning tool for learning the usage and best practices of the Python unittest package.
Please read the entire README and CODE_OF_CONDUCT.md files before contributing.

## Prerequisites

+ [Python 3.x](https://docs.python.org/3/using/)
+ [Coverage](https://coverage.readthedocs.io/en/coverage-5.3/install.html)

## Layout

There are several walk-throughs available for python unit testing, each addressing different areas of unit testing. Additional tests are welcome!
The structure of this repo has subdirectories containing a simple example of unit testing for a python program. Currently, the following walk-throughs are available:

 - getting_started
 - class_testing

The following are planned by the end of October:

 - argparse_testing

If you would like to contribute a new set of test cases for a program this is welcome! Please take the following steps when doing so:

 1. Create an issue addressing the specific type of unit test cases you are adding (example "file_creation_testing")
 2. Fork the repository and create a new directory with a clear name which will describe the type of tests being covered. The layout of the new directory should exactly match the other directories in the repo. If they deviate (an example would be a python program containing submodules), please document the reason for the deviation in the issue and the PR when it is opened.
 3. Write clean, well documented code with testable functions which perform the area being tested.
 4. Write passing test cases and copy the `setup-env.sh` to the base level directory, and the `run_coverage.sh` script in the `./test` directory. Tests should exceed 70% coverage. This can be found in the "Cover" column of the `./run_coverage.sh` output.
 5. Submit a PR and wait for reviews. Please do not commit any changes prior to the review being completed, as it will drastically slow down the review process.
 6. Make changes requested by reviews **in your forked copy** and commit changes. These will directly be added to the PR. Wait for next round of reviews.
 7. Upon successful review, the code will be merged!

## Usage 

To initially configure the environment for a specific walk-through (using getting_started as an example):

    cd ./getting_started    
    source setup-env.sh

To see how it works you can run individual tests by:

    cd test/unit_tests
    python3 utils_test.py
    python3 core_test.py

You can get code coverage by:

    cd test
    ./run_coverage.sh


## Contributing

If you wish to contribute to this project be sure to read the CODE_OF_CONDUCT.md file. 
You should then fork, make changes to your fork and submit pull request to begin the review process. 
The pull request should include the issue number being addressed.