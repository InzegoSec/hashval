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
  parser.add_argument("-t", "--text", required=False)
  parser.add_argument("-f", "--filename", required = False)
  args = parser.parse_args()

  text = args.text
  file = args.filename

  r1 = extract2string(text)
  r2 = extract2file(file)

  time.sleep(2)
  print(f"[!] First hash: {r1}")
  print(f"[!] Second hash: {r2}")

  compare(r1, r2)
