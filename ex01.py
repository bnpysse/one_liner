# Using list comprehension to find top earners

employees = {'Alice': 100000,
             'Bob': 99817,
             'Carol': 122908,
             'Frank': 88123,
             'Eve': 93121,
             }
top_earners = []
for key, val in employees.items():
    if val >= 100000:
        top_earners.append([key, val])

print(top_earners)

print([(x, y) for x in range(3) for y in range(3)])

print([x ** 2 for x in range(10) if x % 2 > 0])

print([x.lower() for x in ['I', 'AM', 'NOT', 'SHOUTING']])

top_earners = [(k, v) for k, v in employees.items() if v >= 100000]
print(top_earners)