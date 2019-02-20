#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:39:00 2019

@author: ale
Observações:
    Não existe switch em python.
    Casting em python é int(valor) e não (int)(valor) como nas linguagens 
    convencionais.
    
"""
'''
Leia um valor inteiro X (1 <= X <= 1000).Em seguida mostre os os números 
divisores do número , um valor por linha. Caso seja primo imprima primo
'''
class Error(Exception):
    def __init__(self):
        return
    def __str__(self):
        return "O numero deve estar no intervalo de 1 a 1000."

def VerificaPrimo(x, vetor_primo):
    primo = True
    for index in range(2, x - 1):
        if( x%index == 0):
            vetor_primo.append(index)
            primo = False
    return primo

if __name__ == "__main__":
    try:
        x = int(input("Digite um numero de 1 até 1000 \n"))
        if((x > 1000) or (x < 1)):
            raise Error
        
    except Error as e:
        print(e)
    except TypeError:
        print("Não é possível ler string")
    except:
        print("Problema Encontrado")
    vetor_primo = []
    primo = VerificaPrimo(x, vetor_primo)
    if(primo == True):
        print("O número " + str(x) +  " é primo")
    else:
        for index in vetor_primo:
            print(index)