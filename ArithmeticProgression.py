#This is an expansion to Carl Friedrich Gauss's method to work for any k (k ∈ R, k ∈ C)'

n, s = 1, 1

k = input("Specify k: ")
k = complex(k) if "j" in k else float(k)

for _ in range(int(input("Specify range: ")) - 1):
  s += n + k
  n += k

print(f"Via programming: {s}")
print(f"My Formula: {((n + 1) * (n + k - 1)) / (2 * k)}")
