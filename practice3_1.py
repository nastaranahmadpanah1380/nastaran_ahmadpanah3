a = [8,0,3,0,4,1,8,8,10,7]
def delet_duplicate(itemes):
    b = []
    for item in itemes:
        if item not in b:
            b.append(item)
    return b
print(delet_duplicate(a))            