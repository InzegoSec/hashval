#!/usr/bin/env python

import argparse
import hashlib

algorithms = ["md5", "sha256", "sha1"]

def extract2string(value):
    return hashlib.md5(value.encode()).hexdigest()

def extract2file(filename):
    with open(filename, 'rb') as file:
        digest = hashlib.file_digest(file, 'md5')
        return digest.hexdigest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="hashval.py", description="hash tool")
    args = parser.
