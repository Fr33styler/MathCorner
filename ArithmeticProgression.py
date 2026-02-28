#This is an expansion to Carl Friedrich Gauss's method to work for any k ≠ 0 (k ∈ R, k ∈ C)'

n, s = 1, 1

k = input("Specify k: ")
k = complex(k) if "j" in k else float(k)

for _ in range(int(input("Specify range: ")) - 1):
  n += k
  s += n

print(f"Via programming: {s}")
print(f"My Formula: {((n + 1) * (n + k - 1)) / (2 * k)}")
