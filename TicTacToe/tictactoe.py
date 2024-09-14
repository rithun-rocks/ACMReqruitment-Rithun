import random

def over(t):
  if t[0]==t[1]==t[2] or t[4]==t[5]==t[3] or t[7]==t[8]==t[6]:
    print(f"{t[0]} {t[1]} {t[2]}\n{t[3]} {t[4]} {t[5]}\n{t[6]} {t[7]} {t[8]}\n")
    print("Game over")
    return False
  if t[0]==t[3]==t[6] or t[4]==t[1]==t[7] or t[2]==t[8]==t[5]:
    print(f"{t[0]} {t[1]} {t[2]}\n{t[3]} {t[4]} {t[5]}\n{t[6]} {t[7]} {t[8]}\n")
    print("Game over")
    return False
  if t[0]==t[4]==t[8] or t[2]==t[4]==t[6]:
    print(f"{t[0]} {t[1]} {t[2]}\n{t[3]} {t[4]} {t[5]}\n{t[6]} {t[7]} {t[8]}\n")
    print("Game over")
    return False
  else:
    return True

t=[1,2,3,4,5,6,7,8,9]
while True:
  print(f"{t[0]} {t[1]} {t[2]}\n{t[3]} {t[4]} {t[5]}\n{t[6]} {t[7]} {t[8]}\n")
  print("You are X, Choose your move: ", end="")
  p=int(input(""))
  try:
    if p!=0 and isinstance(t[p-1], int) and t[p-1]!='O':
      t[p-1]="X"
    else:
      print("Invalid Move")
      continue
  except IndexError:
    print("Invalid Move")
    continue
  if not over(t):
    break
  while True:
    x=random.randint(0,8)
    if isinstance(t[x],int):
      t[x]="O"
      break