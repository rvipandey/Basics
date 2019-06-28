#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: libraravipandey@gmail.com


Here i am covering few python basics
"""

#Question1
planet = "Earth"
diameter = 12742
#first way
print("The diameter of {} is {} kilometers.".format(planet,diameter))
#second way
print("The diameter of %s is %s kilometers."%(planet,diameter))


#Question2 : Nested list and grab your name

nestedlist = [1,2,[3,4],[7,8],[5,[100,200,['Ravi Pandey']],23,11],1,7]
print(nestedlist[4][1][2][0])


#Question3:  nest dictionary  and grab your name

d = {'key1':[1,2,3,{'grabthename':['oh','hello','inception',{'target':[1,2,3,'Ravi Pandey']}]}]}
print(d['key1'][3]['grabthename'][3]['target'][3])


#Question4: 

email='libraravipandey@gmail.com'
sl=email.split('@')
print(sl[1])


#Question5: find if name exist in the doc or not

document="Hello this is ravi , i am reading newspaper. and my brother calling my name ravi ."
def findname(doc):
    return 'ravi' in doc.lower().split()
findname(document)


#Question6: Count the name in document 

def countName(doc,wrd):
    count = 0
    for word in doc.lower().split():
        if word == wrd:
            count += 1
    return count

countName(document,'ravi')

#Question7: Lambda Expression

series=['Ravi','Rahul','Kaushal','Madhav','Mohan','Krishna']
list(filter(lambda word: word[0].lower()=='r',series))

