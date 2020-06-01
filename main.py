#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

num1 = sys.argv[1]
num2 = sys.argv[2]

def get_bin_string(number):
    return bin(int(number)).replace('0b', '')

bin_num_1 = get_bin_string(num1)
bin_num_2 = get_bin_string(num2)

def portAND(input1, input2):
    return '1' if int(input1) and int(input2) else '0'

def portXOR(input1, input2):
    return '1' if (int(input1) or int(input2)) and int(input1) != int(input2) else '0'

print(u"O primeiro numero em binário é: %s" % bin_num_1)
print(u"O Segundo número em binário é: %s" % bin_num_2)

# Iguala o número de zeros nos dois
max_length = len(bin_num_1)
if len(bin_num_2) > max_length:
    max_length = len(bin_num_2)

bin_num_1 = bin_num_1.zfill(max_length)
bin_num_2 = bin_num_2.zfill(max_length)

print(u"Número 1: %s" % bin_num_1)
print(u"Número 2: %s" % bin_num_2)

result = []
for index in range(max_length):
    # pass the numbers on logical gates
    if index == 0:
        bit = portAND(bin_num_1[index], bin_num_2[index])
        print(u"[AND] Primeira posição. Adicionando bit %s - De %s e %s" % (bit, bin_num_1[index], bin_num_2[index]))
        result.append(bit)
    bit = portXOR(bin_num_1[index], bin_num_2[index])
    print(u"[XOR] Adicionando bit %s - De %s e %s" % (bit, bin_num_1[index], bin_num_2[index]))
    result.append(bit)
    

result_string = ''.join(result)
result_string_decimal = int(result_string, 2)
correct_decimal_result = int(num1) + int(num2)

print(u"Resultado de %s + %s = %s" % (bin_num_1, bin_num_2, result_string))
print(u"Resultado em decimal do cálculo binário: %s" % result_string_decimal)
print(u"Resultado esperado: %s" % correct_decimal_result)

