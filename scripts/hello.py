#!/usr/bin/env python3
import sys
import os

# Add src to python path to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from {project}.main import hello

def main():
    print("Executing script from scripts directory...")
    print(hello("Script"))

if __name__ == "__main__":
    main()
