def next(n):
    if n % 6 == 1:
        return n + 4
    if n % 6 == 5:
        return n + 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    

factors = [2]
i = 2
while i < 1000*0.5:
    i = next(i)
    factors.append(i)
    

def simplify(num, denom):
    x, y = num, denom
    if y == 0:
        return 'UNDEFINED'
    for i in factors:
        while x % i == 0 and y % i == 0 and y != 0:
            x, y = int(x/i), int(y/i)
            if x < i or y < i:
                break
    return [x, y]


def false_simplify(num, denom):
    str1, str2 = str(num), str(denom)
    common_list = list(set(str1) - (set(str1) - set(str2)))
    if common_list == [] or set(str1) == set(str2):
        return 'NO'
    list1, list2 = list(str1), list(str2)
    for char in common_list:
        list1.remove(char)
        list2.remove(char)
    if int(''.join(list2)) != 0:    
        return simplify(int(''.join(list1)), int(''.join(list2)))
    else:
        return 'UNDEFINED'
    
nom_product = 1
denom_product = 1

for i in range(10, 100):
    for j in range(i+1, 100):
        if simplify(i, j) == false_simplify(i, j) and (i % 10 != 0 or j % 10 != 0):
            nom_product *= i
            denom_product *= j
            
print(simplify(nom_product, denom_product)[1])
