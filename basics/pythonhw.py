#!/usr/bin/env python3

import random

num = 1
def task_number():
    global num
    print('==========Task #{}============='.format(num))
    num += 1

task_number()
#===Task #1===
def hello_string(arg):
    print('Hello, {}'.format(arg))

a = "Vasya"
hello_string(a)

task_number()
#===Task #2===
def sum(_list):
    count = 0
    for i in _list: 
        count += i
    return count

def multiply(_list):
    count = 1
    for i in _list:
        count *= i
    return count

l = [1,2,3,4]
print(sum(l))
print(multiply(l))

task_number()
#===Task #3===
def reverse(_str):
    return _str[::-1]

a = "I am testing"
print(reverse(a))

task_number()
#===Task #4===
def is_palindrome(_str):
    return _str == _str[::-1]

a = "radar"
print(is_palindrome(a))

task_number()
#===Task #5===
def histogram(lst):
    for i in lst:
        print('*'*i)

l = [4,9,7]
histogram(l)

task_number()
#===Task #6===
def caesar_cipher(_str, key):
    for i in _str:
        print(chr(ord(i)+key),end='')
    print()

a = 'abcdefg'
n = 3
caesar_cipher(a,n)

task_number()
#===Task #7===
def diaginal_reverse(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for x in matrix:
        print(' '.join(map(str, x)))    

mat = [[1,2,3],[4,5,6],[7,8,9]]
diaginal_reverse(mat)

task_number()
#===Task #8===
def game(a, b):
    number = random.randint(a,b)
    while True:
        print('Input number you think was generated from {} till {} :'.format(a,b))
        if int(input()) == number:
            print("Finally, congratulations!")
            break
        else:
            print("Try again! Sorry")

game(2,5)

task_number()
#===Task #9===
def brackets_checker(_str):
    count = 0
    for i in _str:
        if i == '[':
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    if count != 0:
        return False
    else:
        return True

a = '[]][[]'
print(brackets_checker(a))

task_number()
#===Task #10===
def char_freq(_str):
    result = {}
    for i in _str:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    for key, value in result.items():
        print('{} = {}'.format(key,value))

char_freq('abbabcbdbabdbdbabababcbcbab')

task_number()
#===Task #11===
def dec_to_bin(_int):
    return "{0:b}".format(_int)

print(dec_to_bin(20))
