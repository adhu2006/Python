import copy

list1 = [1, [2, 3], 4]
list2 = list1.copy()  # Shallow Copy
list3 = copy.deepcopy(list1)  # Deep Copy
# Demonstrate the difference:
list1[0] = 10  # Modify an element in the outer list
list1[1][0] = 20  # Modify an element in the inner list
print("list1:", list1)
print("list2:", list2)  # <-- Key difference!
print("list3:", list3)  #
