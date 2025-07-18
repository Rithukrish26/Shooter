num = int(input('Enter any number:'))
print(num)

copy_num = num
copy_num = str(copy_num)


list_num = [] #empty list

for i in copy_num:
    val = int(i)
    list_num.append(val)

print(list_num)