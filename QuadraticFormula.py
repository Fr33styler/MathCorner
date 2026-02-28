import re

quadratic = input("Supply quadratic: ")
match = re.match(r"([+-]? ?\d+(?:\.\d+)?)x\^2 ([+-]? ?\d+(?:\.\d+)?)x ([+-]? ?\d+(?:\.\d+)?) = 0", quadratic)

if match:
  a = float(match.group(1).replace(" ", ""))
  b = float(match.group(2).replace(" ", ""))
  c = float(match.group(3).replace(" ", ""))

  delta = b * b - 4 * a * c;
  print(f"First solution: {(-b + delta ** (1/2)) / 2}")
  print(f"Second solution: {(-b - delta ** (1/2)) / 2}")
else:
  print("Invalid quadratic format.")
