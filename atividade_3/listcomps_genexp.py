line_list = ['  line 1\n', 'line 2  \n', ' \n', '']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)

# List comprehension -- returns list
stripped_list1 = [line.strip() for line in line_list]
stripped_list2 = [line.strip() for line in line_list
                 if line != ""]
print(stripped_list1)
print(stripped_list2)
print(stripped_iter.__next__())
print(stripped_iter.__next__())