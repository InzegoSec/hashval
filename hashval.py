#!/usr/bin/env python

# librerias a usar
import argparse
import hashlib
import time
from pwn import *

panel = r'''
      |\ |\  hashval
      \ \| | created by
       \ | | inzegosec
     .--''/
    /o     \
    \      /
    {>o<}='
'''

# algoritmos, recomendados por rapidez
algorithms = ["md5", "sha256", "sha1"]

# funciones
def e_string(text, algorithm):
    h = hashlib.new(algorithm)
    h.update(text.encode('utf-8'))
    return h.hexdigest() # la funcion responde con el hash en hexadecimal 

def e_file(filename, algorithm): # lectura en bytes del archivo
    with open(filename, 'rb') as file:
        digest = hashlib.file_digest(file, f'{algorithm}')
        return digest.hexdigest() # retorna hash en hexadecimal
if __name__ == "__main__":
   print(panel)

   # argumentos
   parser = argparse.ArgumentParser(prog="hashval", description="hashval is a tool to generate and compare hashes", epilog="use flag --help to more info")
   parser.add_argument("-g", "--generate", required=False, action="store_true", help="use this flag to generate hash mode")
   parser.add_argument("-t", "--text", required=False, help="type a text to generate a hash")
   parser.add_argument("-f", "--filename", required=False, help="path to file")
   parser.add_argument("-a", "--algorithm", required=False, choices=[algorithms[0], algorithms[1], algorithms[2]], help="select algorithm to use")
   args = parser.parse_args()
   
   # funcion generador de hashes
   if args.generate == True:
       log.info("Generate mode selected...")
       time.sleep(2)
       p = log.progress("Working in")
       try:
           if args.text is None:
               p.status("Generate file Hash...")
               time.sleep(2)
               r = e_file(args.filename, args.algorithm)
               print()
               log.info(f"Filename: {args.filename}")
               log.info(f"Algorithm: {args.algorithm}")
               log.success(f"Hash: {r}")
           else:
               p.status("Generate string hash...")
               time.sleep(2)
               r = e_string(args.text, args.algorithm)
               print()
               log.info(f"String: {args.text}")
               log.info(f"Algorithm: {args.algorithm}")
               log.success(f"Hash: {r}")
       except ValueError as e:
           log.failure(f"Error: {e}")
   else:
       pass
