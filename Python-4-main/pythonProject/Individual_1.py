#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


A = [int(input(f"Введите элемент {i+1}: ")) for i in range(10)]
product = 1
count = 0
for num in A:
    if num > 0 and num % 3 == 0:
        product *= num
        count += 1
if count > 0:
    print(f"Произведение положительных элементов, кратных 3: {product}")
    print(f"Количество таких элементов: {count}")
else:
    print("Нет положительных элементов, кратных 3.")
