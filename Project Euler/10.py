s, f = [0, [True] * 2000000]
for p in range(2, 2000000):
  if f[p]:
    s += p
    for i in range(p*p, 2000000, p):
      f[i] = False
print(s)