#!/usr/bin/env python

import argparse
import hashlib
import time

algorithms = ["md5", "sha256", "sha1"]

def extract2string(value):
    return hashlib.md5(value.encode()).hexdigest()

def extract2file(filename):
    with open(filename, 'rb') as file:
        digest = hashlib.file_digest(file, 'md5')
        return digest.hexdigest()

def compare(h1, h2):
    if h1 == h2:
        print("[+] Hash equals")
    else:
        print("[!] Hash not equals")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="test")
  parser.add_argument("-c", "--compare", required=True, action="store_true")
  parser.add_argument("-t", "--text", required=False)
  parser.add_argument("-f", "--filename", required = False)
  parser.add_argument("-f2", "--filename2", required=False)
  args = parser.parse_args()

  if args.compare == True:
      try:
          if args.text is None:
              r1 = extract2file("test.txt")
              r2 = extract2file("test2.txt")
          else:
              extract2string(args.text)
      except ValueError:
  else:
      pass
