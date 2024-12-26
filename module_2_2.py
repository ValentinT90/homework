first = 151
second = 149
third = 188
if first == second and second == third:
    print(int(3))
elif first == second or second == third or first == third:
    print(int(2))
else:
    if not (first == second or second == third or first == third):
     print(int(0))

