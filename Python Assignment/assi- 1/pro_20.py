''' Write a Python function that takes a list of words and returns the
length of the longest one '''

list1=["apple","mango","bannana","cherry"]

mx=0
long_word=0

print(list1)


for i in list1:
    if len(i)>mx:
        long_word=i
        mx=len(i)

print("the length of longest one:- ",mx)
print("the longest word is:- ",long_word)
