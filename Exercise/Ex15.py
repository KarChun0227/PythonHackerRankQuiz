sentance = input("Give me a sentence:")

splitSentence = sentance.split(" ")

sentenceLen = len(splitSentence)

newSentence = ""

i = 1

while i < sentenceLen+1:
    newSentence = newSentence + splitSentence[sentenceLen-i] + " "
    i = i + 1

print (newSentence)

