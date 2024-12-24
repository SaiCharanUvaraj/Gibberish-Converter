import random

def generate_random_characters(pool, count):
    return random.choices(pool, k=count)

def convertToGibberish(word):
    vowels = "aeiou"
    consonants = "bdfghjklmnprstvy"
    
    length = random.randint(len(word),len(word)+2)
    vowelCount = length // 2
    consonantCount = length - vowelCount

    randomVowels = generate_random_characters(vowels, vowelCount)
    randomConsonants = generate_random_characters(consonants, consonantCount)

    gibberishWord = []
    useVowel = random.choice([True, False]) 
    while randomVowels or randomConsonants:
        if useVowel and randomVowels:
            gibberishWord.append(randomVowels.pop())
        elif not useVowel and randomConsonants:
            gibberishWord.append(randomConsonants.pop())
        useVowel = not useVowel 
    
    return ''.join(gibberishWord)