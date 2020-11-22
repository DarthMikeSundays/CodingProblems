string=input("Chose a string.")
string=string.upper()
alphabet=["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","S","T","U","V","W","X","Y","Z"]
letterList=""
for letter in alphabet:
    if letter in string:
        occurences=string.count(letter)
        for x in range(0,occurences):
             letterList+=letter
print(letterList.lower())
    
    
