hi="hello"
print (hi[1])

hi="hello"
print (hi[-1])
    #square brakets are for select a single letter for a worid

  #+
hi="hello"
bye="bye"
print (hi+ " " +bye)
print ("hi" + "bye", sep= "  ")

print(3*"abc")

number_of_words= 0
sentence= input("give me a sentence")
for letter in sentence:
    if letter == " ":
        number_of_words = number_of_words+1
print ("there are", number_of_words+1, "words")
