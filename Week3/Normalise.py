#Program that reads in a string and strips any leading or trailing spaces.
#Program will also convert the string to lower case.
#Program should will output the length of the input and output strings.
#Author: Brendan Tunney

rawString = input("Please enter a string: ")
normalisedString = rawString.strip() .lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

print("The normalised string is: {} " . format(normalisedString))
print("We reduced the input string from {} to {} characters ".format(lenghtOfRawString, lenghtOfNormalised))

