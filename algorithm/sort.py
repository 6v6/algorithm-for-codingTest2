array = [7, 5, 9, 0 , 4, 1, 3, 5]

result = sorted(array)
print(result)

array2 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array2, key=setting)
print(result)