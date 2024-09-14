p=input("Password: ")
f=True
e=""
if len(p)<8:
  f=False
  e="Your password must be more than 8 characters"
c=s=q=False
for i in p:
  if i in "!@#$%^&*()-+?_=,<>/":
    q=True
  if i in "qwertyuiopasdfghjklzxcvbnm":
    s=True
  if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
    c=True
if not q:
  f=False
  e="Your password must contain a special character"
if not c or not s:
  f=False
  e="Your password must contain a small and capital letter"
if p[0] in "!@#$%^&*()-+?_=,<>/1234567890":
  f=False
  e="First character should not be a digit/special character"
if p in ["A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f"]:
  f=False
  e="Your password is blacklisted"
if f:
  print("Valid password")
else:
  print("Invalid password:",e)