rawString = input("PLease enter your sentence: ")
normalisedString = rawString.strip().lower()
print (normalisedString)

print (normalisedString.split (' ')[::-2])
