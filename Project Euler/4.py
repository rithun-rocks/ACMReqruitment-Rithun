p=1
for i in range(100,1000):
  for j in range(100,1000):
    if str(j*i)==str(j*i)[::-1]:
      p=j*i
print(p)