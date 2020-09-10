# CAMERON WALCOTT,  cwalcott@usc.edu
# ITP 115, Spring 2020
# Lab 6-2

# palindrome: the same word or phrase forwards and backwards

user = input("Enter a phrase: ")

# lowercase
phrase = user.lower()
print(phrase)

# get rid of spaces
phrase = phrase.replace(" ","")
print(phrase)

# convert to a list
phraseList = list(phrase)

# reverse
phraseList.reverse()
print(phraseList)

# convert back to a string
# string = delimeter.join(list)
delimiter = ""
reverse = delimiter.join(phraseList)
print(reverse)

# check if a phrase and reverse are same
if phrase == reverse:
    print("You entered a palindrome!")
else:
    print("Your phrase is not a palindrome.")