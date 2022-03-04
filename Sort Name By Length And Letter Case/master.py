def sortByLength(names:list):
    
    """
    this function sort names of array by length and the alphabet

    params:
        names: the list of names you need to sort it
    """
    for i in range(len(names)):
        smalestPos = i
        for j in range(i+1, len(names)):
            if len(names[j]) < len(names[smalestPos]):
                smalestPos = j
            elif len(names[j]) == len(names[smalestPos]):
                if names[smalestPos] > names[j]:
                    smalestPos = j
        if(smalestPos != i):
            temp = names[i]
            names[i] = names[smalestPos]
            names[smalestPos] = temp
def sort(names:list):
    """
    this function return only names sort by letter 'a'

    params:
        names: the list of names you need to sort it

    return:
        return new sorted list by letter 'a'
    """
    small_side = []
    big_side = []
    for name in names:
        if name[0] == "A":
            big_side.append(name)
        elif name[0] == 'a':
            small_side.append(name)

    sortByLength(small_side)
    sortByLength(big_side)


    return small_side + big_side


# test
print(sort(["Ameer", "alsayed", "Mahmoud", "Ahmed", "ayman", "Israa", "Anas", "amal", "amr", "aml"]))

# output
# ['aml', 'amr', 'amal', 'ayman', 'alsayed', 'Anas', 'Ahmed', 'Ameer']


