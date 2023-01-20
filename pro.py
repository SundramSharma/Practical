def record():
    f = open(r'records.txt','w')
    f.writelines(['roll no ' ,'name ' , 'class '])
    f.write('\n')
    rno =  input('Enter rollno. ')
    name = input('enter name: ')
    class1 = input('Enter class')
    m= [rno,name,class1]
    for i in m:
         f.write(i)
         f.write(' ')
        # f.write('\n')
    f.close()
record()