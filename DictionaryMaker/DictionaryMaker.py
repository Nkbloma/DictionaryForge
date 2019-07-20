import csv, os
class DictionaryForge:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def AddWord(self):
        NewWord = input("Add the new word. ")
        Definition = input("Enter the word's definition. ")
        IdNum = self.CountRows() + 1
        with open("dict.csv", "a", newline='') as f:
            a = csv.writer(f, delimiter=",")
            a.writerow([IdNum, NewWord, Definition])
        print(NewWord + " has been added as number " + str(IdNum))

    def DeleteWord(self):
        SearchWord = input("Which word are you deleting? ")
        NewDict = []
        ID=1
        FoundWord = False
        with open("dict.csv", "r", newline='') as f:
            r = csv.reader(f, delimiter=',')
            for row in r:
                if SearchWord == row[1]:
                    FoundWord = True
                    continue
                else:
                    CurrentWord = [ID, row[1], row[2]]
                    NewDict.append(CurrentWord)
                    ID+=1
        if FoundWord == True:
            os.rename("dict.csv", "dict.csv.temp")
            with open("dict.csv", "w", newline='') as f:
                a = csv.writer(f, delimiter=",")
                a.writerows(NewDict)
                print("Word has been deleted.")
            os.remove("dict.csv.temp")
        else:
            return ("Word was not found.")

    def FindWord(self):
        print("What word are you trying to find?")
        SearchWord = input()
        with open("dict.csv", "r", newline='') as f:
            r = csv.reader(f, delimiter=',')
            for row in r:
                if SearchWord == row[1]:
                    return print(SearchWord + " has been found as ID " + row[0] + "\nDefinition: " + row[2])
                else:
                    continue

        return print(SearchWord + " couldn't be found")
        #Look second column in row if it equals SearchingWord

    def ListWords(self):
        with open("dict.csv", "r", newline='') as f:
            r = csv.reader(f, delimiter=',')
            for row in r:
                print("ID " + row[0] + ": " + row[1] + "\n" + row[2] + "\n")

    def ModifyWord(self):
        SearchWord = input("What word are you modifying? ")
        NewDict = []
        FoundWord = False
        with open("dict.csv", "r", newline='') as f:
            r = csv.reader(f, delimiter=',')
            for row in r:
                if SearchWord == row[1]:
                    FoundWord = True
                    NewWord = input("What is the new word?: ")
                    NewDefinition = input("What is the new definition: ")
                    new_row = [row[0], NewWord, NewDefinition]
                    NewDict.append(new_row)
                else:
                    NewDict.append(row)
        if FoundWord == True:
            os.rename("dict.csv", "dict.csv.temp")
            with open("dict.csv", "w", newline='') as f:
                a = csv.writer(f, delimiter=",")
                a.writerows(NewDict)
                print("Word has been changed.")
            os.remove("dict.csv.temp")
        else:
            return  "Word was not found."
    #Make temp file, write file, delete temp file

    def CountRows(self):
        row_count = 0
        with open("dict.csv", "r", newline='') as f:
            r = csv.reader(f, delimiter=',')
            row_count = sum(1 for row in f)
        return row_count

    def Help(self):
        print("""
    a - Add a word to the dictionary.
    d - Delete a word from the dictionary.
    m - Modify a word in the dictionary.
    f - Find a word in the dictionary.
    l - List all word to the dictionary.
    e - Exit from the program.
    h - Help.
    """)
