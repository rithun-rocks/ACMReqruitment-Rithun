d = 2
n=600851475143
while d * d <= n:
  if n % d == 0:
    n//= d
  else:
    d += 1
print(n)