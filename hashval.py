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

def leng_val(h1, h2):
    return len(h1) == len(h2)

def compare(h1, h2):
    return h1 == h2

if __name__ == "__main__":
    print(panel)

    # argumentos
    parser = argparse.ArgumentParser(prog="hashval", description="hashval is a tool to generate and compare hashes", epilog="use flag --help to more info")
    parser.add_argument("-g", "--generate", required=False, action="store_true", help="use this flag to generate hash mode")
    parser.add_argument("-c", "--compare", required=False, action="store_true")
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
                p.status("generating a file hash...")
                time.sleep(2)

                print()
                r = e_file(args.filename, args.algorithm)
                log.info(f"Filename: {args.filename}")
                log.info(f"Algorithm: {args.algorithm}")
                log.success(f"Hash: {r}")
            else:
                p.status("generating a text hash...")
                time.sleep(2)

                print()
                r = e_string(args.text, args.algorithm)
                log.info(f"String: {args.text}")
                log.info(f"Algorithm: {args.algorithm}")
                log.success(f"Hash: {r}")
        except ValueError as e:
            log.failure(f"Error: {e}")
    else:
        pass

    # funcion de comparacion
    if args.compare == True:
        log.info("Compare mode selected...")
        time.sleep(2)

        print()
        u_in = input("[*] Input the hash: ")
        u_in2 = input("[*] Input the second hash: ")
        print()

        r = leng_val(u_in, u_in2)
        if r == True:
            log.info("Algoritmos iguales")
        else:
            log.failure("Error")

        result = compare(u_in, u_in2)
        if result == True:
            log.success("Hashes iguales")
        else:
            log.failure("Hashes no iguales")