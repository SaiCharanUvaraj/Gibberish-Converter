fileName="dictionary.txt"

def addGibbrish(word,gibberish):
    s=word+"-"+gibberish
    with open(fileName, "a") as file:
        file.write(s+"\n")

def readAllGibbrish():
    dictionary={}
    try:
        with open(fileName, "r") as file:
            lines = file.readlines()  
        for line in lines:
            line=line.replace("\n","")
            word,gibberish=map(str,line.split("-"))
            dictionary[word]=gibberish
    except FileNotFoundError:
        with open(fileName, "w"):
            pass 
    return dictionary