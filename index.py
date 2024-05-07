def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])
    
my_list = [1,4,6,4]
a = sum(my_list)
print(a)