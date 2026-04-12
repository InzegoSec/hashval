#!/usr/bin/env python

# librerias a usar
import argparse
import hashlib
import time
import sys
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

# Validacion de longitud de hash, para que la comparacion se haga con hashes del mismo algoritmo
def leng_val(h1, h2):
    return len(h1) == len(h2) # Retorna True o False si el numero de caracteres son iguales

def compare(h1, h2):
    return h1 == h2 # Returna True o False si los hashes son iguales

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

        log.info("Now type your hashes to compare")
        usr_input = input("[*] First hash: ")
        usr_input_2 = input("[*] Second hash: ")
        p = log.progress("Working in")
        p.status("Verifying algorithms...")
        time.sleep(2)

        if leng_val(usr_input, usr_input_2) == True:
            log.success("Verified")
            p.status("Comparing...")
            time.sleep(2)

            try:
                r = compare(usr_input, usr_input_2)
                if r == True:
                    log.success("Equal hashes.")
                else:
                    log.failure("No equal hashes.")
                    sys.exit(0)
            except ValueError as e:
                log.failure(f"{e}")
        else:
            log.failure("Error in verificate, exiting...")
            sys.exit(0)
    else:
        sys.exit(0)