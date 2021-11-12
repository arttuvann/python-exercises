#!/usr/bin/python3

# This script is an exercise in:
#   * setting up development environment with a remote (github) repository,
#   * getting practice in git push, and
#   * establishing basic unit test workflow with assertEqual.
# 
# Tests are run with:
# $ python3 -m unittest test_hello_world.py
#
# TODO:
#   * Create more test cases with unittest to get comfortable with it
#   * Integrate testing into Docker container debugging and deployment so that testing is done inside container (with its packages)
#     rather than the host machine.

def hello_world():
    return "Hello world!"

def main():
    hello_world()

if __name__ == "__main__":
    main()