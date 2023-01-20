def countvowel():
    f = open('STORY.txt','r')
    countvowels = 0
    countconsonants = 0
    data = f.readlines()
    for i in data:
        for j in i:
            if j.isalpha():
                if j.lower() in ['a','e','i','o','u']:
                    countvowels += 1
                else :
                    countconsonants += 1

    print(data)
    print("Number of Vowels: ",countvowels)
    print('Number of Consonant: ',countconsonants)
    f.close()

countvowel()