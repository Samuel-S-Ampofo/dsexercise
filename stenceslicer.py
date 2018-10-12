#stence slicer get a sentence fron 25% to 75 %
sentence = input( "type here you sentence")

sentenelen = len(sentence)
sent25 = round(25/100 * sentenelen)
sen75 = round(75/100 * sentenelen)

newsentence = sentence[sent25:sen75]
print(newsentence)
