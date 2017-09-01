#!/usr/bin/env python3

#===Task #1===
def hello_string(arg):
    print('Hello, {}'.format(arg))

a = "Vasya"
hello_string(a)

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

#===Task #3===
def reverse(_str):
    return _str[::-1]

a = "I am testing"
print(reverse(a))
