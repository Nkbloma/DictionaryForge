from DictionaryMaker import DictionaryForge
import csv

choices=('a', 'd', 'm', 'l', 'f', 'e', 'h')
choice = ""
DF = DictionaryForge('bob','jill')
print("Welcome to the Dictionary Forge.")
DF.Help()
while choice != 'e':
    choice = input("Forge: ")
    if choice not in choices:
        print("\'" + choice + "\'" + " isn't an option. Type h for help")
    else:
        if (choice == 'a'):
            DF.AddWord()
        elif (choice == 'd'):
            DF.DeleteWord()
        elif (choice == 'm'):
            DF.ModifyWord()
        elif (choice == 'l'):
            DF.ListWords()
        elif (choice == 'f'):
            DF.FindWord()
        elif (choice == 'h'):
            DF.Help()

print("Exiting Dictionary Forge.")