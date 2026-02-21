#Applying the infinite series of the square root for any radicand r (r ∈ R, r ∈ C)

s = 0
r = input("Specify radicand: ")
r = complex(r) if "j" in r else float(r)

for _ in range(int(input("Specify range: "))):
  s = (r - 1) / (2 + s)

print(f"The square root is {1 + s}")
