# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:46:05 2018
Muhammad Mashwani
Assignmnet #8 
PeopleSoft ID: 1378052
"""
def helper(a,b):
    result = []
    for i in a:
        for j in b:
            result.append(i + j)
    return result

def helper2(num,look_up):
    result = [""]
    for x in num:
        result = helper(result,look_up[x].copy())
    return result
    
    
words = []
with open("words.txt") as file:
    for word in file.readlines():
        word = word.strip()
        if len(word) == 3 or len(word) == 4:
            words.append(word)
            
print(words)


phone = input("Please enter a phone number: ")
#phone = '223-5653'
number = ""
for letter in phone:
    if letter.isdigit():
        number += letter
        
        
look_up = {'0' : ['O'], 
           '1' : ['I','L'], 
           '2':['A','B','C'], 
           '3':['D','E','F'], 
           '4':['G','H','I'],
           '5':['J','K','L'], 
           '6':['M','N','O'], 
           '7':['P','Q','R','S'], 
           '8':['T','U','V'],
           '9':['W','X','Y','Z']}

num = number[:3]
result3 = helper2(num,look_up)
      
num = number[3:]
result4 = helper2(num,look_up)

print("Results include....")

for a in result3:
    for b in result4:
        if a in words and b in words:
            print("{}-{}".format(a,b))
"""for a_word in result:
    if a_word in words:
        print(a_word)"""