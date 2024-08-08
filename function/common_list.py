def find_common_elements(*args):
    common_elements = []
    for element in args[0]:
        print([lst for lst in args])
        if all(element in lst for lst in args):
            common_elements.append(element)
    return common_elements

# lists = [[1, 2, 3, 4], [2, 4, 6], [2, 3, 4]]
# element = 1
# all(element in lst for lst in lists)

"""
lists = [[1, 2, 3, 4], [2, 4, 6], [2, 3, 4]]
element = 1
is_present_in_all_lists = True

for lst in lists:
    if element not in lst:
        is_present_in_all_lists = False
        break

print(is_present_in_all_lists)

"""
list1 = [1, 2, 3, 4]
list2 = [2, 4, 6]
list3 = [2, 3, 4]
common_elements = find_common_elements(list1, list2, list3)
print(common_elements)