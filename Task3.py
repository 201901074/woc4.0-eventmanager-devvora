#Task3
thisdict = {}


print("Please enter your name ")
user = input()
print("Hello ", user)
print("Press 1 to store a new contact ")
print("Press 2 to view a stored contact ")
print("Press 3 to view all contacts ")
print("Press -1 to exit the process at any given time ")

t = input()

if t == "1":
  n = input("Please enter the name of the person ")
  print("Please enter the contact number(s) of ", n)
  print("To exit the process, press -1")

  number = input()
  while number != "-1":
    if n in thisdict.keys():
      thisdict[n].append(number)
    else:
      thisdict[n] = []
      thisdict[n].append(number)
    number = input()
    
  
elif t == "2":
  n = input("Please enter the name (partial/complete) of the user whose contacts you want to check ")
  print("Now, we will provide a list of users who have this name (completely/partially).")

  for x in thisdict.keys():
    if n in x:
      print(x)
  
  n = input("Please select the user you desire or -1 to exit the process")
  if n == "-1":
    exit()
  
  for x in thisdict[n]:
    print(x)

elif t == "3":
  
  for x in thisdict.keys():
    print(x)
    for n in thisdict[x]:
      print(n)
    print("\n")
