list = [1,5, 8, 9]
target = 10

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] + list[j] == target:
            print(i,j)