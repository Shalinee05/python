from itertools import count


file = open('myfile.txt', 'r')
lines = file.readlines()

count = 0 

for index, line in enumerate(lines):
    count = count+1
    print("Line{}".format(count), line)
    
file.close()
   
    
