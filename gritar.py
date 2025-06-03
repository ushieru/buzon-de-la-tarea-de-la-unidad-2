#! bin/python3.13.3 [GCC 15.0.1 20250418 (Red Hat 15.0.1-0)]

# Escriba un programa para leer un archivo e imprimir el contenido del
# archivo (línea por línea) todo en mayúsculas. La ejecución del programa se verá de la siguiente manera:

# python gritar.py
# Teclea nombre del archivo: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
# BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
# SAT, 05 JAN 2008 09:14:16 -0500
import os

name = input("Teclee el nombre del archivo:\n> ")

with open(f'{name}', "r") as file:
    for line in file:
        print(line.strip().upper())