# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:15:47 2021

@author: girish
"""

#area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

class Triangle():
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    

class Area_of_Tri(Triangle):
    def __init__(self,a,b,c):
        Triangle.__init__(self,a,b,c)

    def tri_area(self):
        s = (self.a+self.b+self.c)/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return area
    



x = Area_of_Tri(4,4,4)
print(x.tri_area())


'''

def tri_area(s,a,b,c):
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area

x = input("Enter 3 sides of triangle  ").split(',')
print(x)
a,b,c = [int(i) for i in x]
s = (a+b+c)/2

area = tri_area(s,a,b,c)
print(area)

'''

def filter_long_words(n,x):
    a = []
    for i in x:
        if(len(i)>n):
            a.append(i)
    return a

x = ['asdas','dfsd','dsdsds','dddddd','ada']
a = filter_long_words(4, x)
print(a)

def map_words_len(words):
    j = {word:len(word) for word in words}
    return j

k = map_words_len(x)
print(k.values())  


def isvowel(a):
    if a in ('a','e','i','o','u'):
        return True
    else:
        return False
    
print(isvowel('a'))
    
