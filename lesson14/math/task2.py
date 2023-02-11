import math

print(0.1 + 0.2 == 0.3)
result = math.isclose(0.1 + 0.2, 0.3)
print(result)

result = math.isclose(0.1, 0.1000000000009)
print(result)