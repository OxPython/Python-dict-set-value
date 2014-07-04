'''
Created on Jul 2, 2014

@author: viejoemer

HowTo create and set a value in a dict in python?

¿Cómo crear e insertar un valor en un diccionario en Python?

'''

#Creating a dict with data
d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }
print(d)

#Set a value
d["red"] = 111
print(d)

#Create a key and set a value
d["black"] = 400
print(d)
