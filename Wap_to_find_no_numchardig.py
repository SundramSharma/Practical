def countchars():
    f = open('STORY.txt','r')
    countdig = 0
    countalpha = 0
    countspec = 0
    countspace = 0
    data = f.readlines()
    for i in data:
        for j in i:
            if j.isdigit():
                countdig += 1
            elif j.isspace():
                countspace += 1
            elif j.isalpha():
                countalpha += 1
            else: 
                countspec += 1
    print(data)
    print("Number of chars: ",countalpha)
    print('Number of SpecC: ',countspec)
    print("Number of Digit: ",countdig)
    print("Number of Space: ",countspace)
    f.close()

countchars()