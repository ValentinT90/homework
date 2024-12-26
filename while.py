my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0
kol_vo = len(my_list)
while zero < kol_vo:
    if my_list[zero] == 0:
        zero = zero + 1
        continue
    elif my_list[zero] > 0:
        print(my_list[zero])
        zero = zero + 1
    elif my_list[zero] < 0:
        break
print('Good')