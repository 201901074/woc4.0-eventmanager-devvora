#Task 2


file = open('sample1.txt','r')

for each in file:
  print(each)

file.close();

file = open('sample1.txt','w')
file.write('Naruto Uzumaki is the strongest Hokage to have ever lived.')
file.close();

file = open('sample1.txt','r')

for each in file:
  print(each)

file.close();