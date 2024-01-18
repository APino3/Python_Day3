#Write a function to count the number of vowels in a given string 
str1 = input ("Enter the string: ")
vowels = "aAeEiIoOuU"
count=0
for i in str1:
    if i in vowels: 
        count=count+1

print("Count of vowels in the given string:", count)