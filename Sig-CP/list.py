def insert(l):
  e=eval(input("Enter element to insert: "))
  l.append(e)
  return l
def delete(l):
  i=int(input("Enter index to delete: "))
  del l[i]
  return l
def search(l):
  e=eval(input("Enter element to search: "))
  for i in range(0,len(l)):
    if l[i]==e:
      print(f"Element found at index: {i}")
l=[]
while True:
  print(f"List: {l}")
  c=input(f"i - Insert\nd - Delete\ns - Search\ne - Exit\n")
  if c=="i":
    insert(l)
  if c=="d":
    delete(l)
  if c=="s":
    search(l)
  if c=="e":
    break
