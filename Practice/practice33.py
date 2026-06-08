#write a recursive function to print all the elements in a list


def prin_list (list,idx=0):
    
    if (idx == len(list)):
        return
    print(list[idx])
    prin_list(list,idx+1)

fruits = ["mango","grapes","apple","banana"]

prin_list(fruits)
