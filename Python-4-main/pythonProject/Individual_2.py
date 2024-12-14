#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


A = [3, -2, 5, -1.2, 7, -4, 2, -9, 4, 19]
min_index = 0
min_value = abs(A[0])
for i in range(1, len(A)):
    if abs(A[i]) < min_value:
        min_value = abs(A[i])
        min_index = i
print(f"Номер минимального по модулю элемента: {min_index}")
sum_after_first_negative = 0
found_first_negative = False
for num in A:
    if num < 0 and not found_first_negative:
        found_first_negative = True
    elif found_first_negative:
        sum_after_first_negative += abs(num)
print(f"Сумма модулей элементов после первого отрицательного элемента: {sum_after_first_negative}")
