'''
Created on Jul 20, 2015

@author: Riley

This program solves project Euler problem #15 - counting lattice
paths. This is the same formula for finding the nth central binomial
coefficient, where n is the size in an n * n grid 

formula for finding central binomial coefficients: (2n)! / n!^2
'''
import math

num = int(input("Enter number for n * n grid: "))

my_var = math.factorial(num * 2) / math.factorial(num) ** 2

print (my_var)