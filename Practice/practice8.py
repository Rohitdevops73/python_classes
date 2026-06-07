#wap to check if a list contains a palindrome of elements. (hint: use copy() method)

#[1,2,3,2,1]
list1 = [1,2,3,2,1]
list2 = [1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()
if (copy_list1 == list1):
    print("this list is a palindrome")
else:
    print("its not a palindrome")

copy_list2=list2.copy()
copy_list2.reverse()
if (copy_list2 == list2):
    print("this list is a palindrome")
else:
    print("its not a palindrome")

