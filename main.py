# This is a sample Python script.
import random
# Press Shift+F10 to ecounterecute it or replace it with your code.
class person:
    name = 'john'
    age = 36
    country = "norway"
print(dir(person))

koloda = [6, 7, 8, 10, 8, 9, 10, 11] * 4
# if 6 in koloda:
#     print ("est' 6")
random.shuffle(koloda)
print(koloda)
counter = 0
# def vzytie():
#     koloda.pop(1)
x = True
while (True and counter <= 21):
    x = input("Would you like to take a card? y/n? " )
    #print(x.capitalize())
    if x == 'n':
        print("Your score is - " + str(counter))
        break
    #while counter <= 21:
    if counter <= 21:
        karta = koloda.pop(0)
        print("ty dostal kartu: " + str(karta))
        counter = counter + karta
        print("Your score is - " + str(counter))
    if counter == 21:
        print("you WON")
        print("Your score is - " + str(counter))
        break
    if counter > 21:
        print("you LOSE")
        #print("Your score is - " + str(counter))
        break



