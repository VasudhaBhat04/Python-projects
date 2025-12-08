#LISTS METHODS

# Starting list
nums = [10, 20, 30]

# append() – add an item at the end
nums.append(40)
# nums -> [10, 20, 30, 40]

# insert() – add item at a specific position
nums.insert(1, 15)
# nums -> [10, 15, 20, 30, 40]

# extend() – add elements from another iterable
nums.extend([50, 60])
# nums -> [10, 15, 20, 30, 40, 50, 60]

# remove() – remove first occurrence
nums.remove(30)
# nums -> [10, 15, 20, 40, 50, 60]

# pop() – remove item by index & return it
removed_value = nums.pop(2)
# removed_value -> 20
# nums -> [10, 15, 40, 50, 60]

# index() – find first index of value
pos = nums.index(40)
# pos -> 2

# count() – count occurrences
count_10 = nums.count(10)
# count_10 -> 1

# copy() – get a copy
nums_copy = nums.copy()
# nums_copy -> [10, 15, 40, 50, 60]

# reverse() – reverse list in-place
nums.reverse()
# nums -> [60, 50, 40, 15, 10]

# sort() – sort ascending
nums.sort()
# nums -> [10, 15, 40, 50, 60]

# clear() – empty list
nums.clear()
# nums -> []

#DICTIONARY METHODS

# Starting dictionary
student = {"name": "Arjun", "age": 21, "grade": "A"}

# copy() – returns a  copy
student_copy = student.copy()
# student_copy -> {'name': 'Arjun', 'age': 21, 'grade': 'A'}

# get() – safely fetch a value without error
name_val = student.get("name")
# name_val -> 'Arjun'

missing_val = student.get("address")
# missing_val -> None

# items() – returns key-value pairs as tuples
pair_list = list(student.items())
# pair_list -> [('name', 'Arjun'), ('age', 21), ('grade', 'A')]

# keys() – returns all keys
all_keys = list(student.keys())
# all_keys -> ['name', 'age', 'grade']

# values() – returns all values
all_values = list(student.values())
# all_values -> ['Arjun', 21, 'A']

# pop() – remove a key and return its value
removed_age = student.pop("age")
# removed_age -> 21
# student -> {'name': 'Arjun', 'grade': 'A'}

# popitem() – remove the last inserted key-value pair
last_removed = student.popitem()
# last_removed -> ('grade', 'A')
# student -> {'name': 'Arjun'}

# setdefault() – return existing value OR insert if missing
res1 = student.setdefault("name", "Default")
# res1 -> 'Arjun'

res2 = student.setdefault("city", "Bangalore")
# res2 -> 'Bangalore'
# student -> {'name': 'Arjun', 'city': 'Bangalore'}

# update() – add or modify multiple key-value pairs
student.update({"age": 22, "course": "CSE"})
# student -> {'name': 'Arjun', 'city': 'Bangalore', 'age': 22, 'course': 'CSE'}

# fromkeys() – create new dictionary from keys
new_dict = dict.fromkeys(["a", "b", "c"], 0)
# new_dict -> {'a': 0, 'b': 0, 'c': 0}

# clear() – empty the dictionary
student.clear()
# student -> {}

#TUPLE  METHODS

# Starting tuple
nums = (10, 20, 30, 20, 40, 20)

# count() – number of times a value occurs
count_20 = nums.count(20)
# count_20 -> 3

count_100 = nums.count(100)
# count_100 -> 0

# index() – first index of a value
first_20_index = nums.index(20)
# first_20_index -> 1

first_30_index = nums.index(30)
# first_30_index -> 2

#  using index() on a value not in tuple → error
# nums.index(999)  # ValueError

#SET  METHODS

# Starting sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# add() – add a single element
A.add(10)
# A -> {1, 2, 3, 4, 10}

# copy() – returns a shallow copy
A_copy = A.copy()
# A_copy -> {1, 2, 3, 4, 10}

# difference() – items in A but not in B
diff_AB = A.difference(B)
# diff_AB -> {1, 2, 10}

# difference_update() – remove common items permanently  
C = {1, 2, 3, 4}
C.difference_update({3, 4})
# C -> {1, 2}

# discard() – remove element if present (no error if missing)
D = {1, 2, 3}
D.discard(2)
# D -> {1, 3}

# intersection() – common elements
intersect_AB = A.intersection(B)
# intersect_AB -> {3, 4}

# intersection_update() – keep only common items
E = {1, 2, 3, 4}
E.intersection_update({2, 3, 10})
# E -> {2, 3}

# isdisjoint() – True if no common items
res_disjoint = {1, 2}.isdisjoint({3, 4})
# res_disjoint -> True

# issubset() – check subset
res_subset = {1, 2}.issubset({1, 2, 3, 4})
# res_subset -> True

# strict subset (<)
res_strict_subset = {1, 2} < {1, 2, 3, 4}
# res_strict_subset -> True

# issuperset() – check superset
res_superset = {1, 2, 3}.issuperset({1, 2})
# res_superset -> True

# strict superset (>)
res_strict_superset = {1, 2, 3} > {1, 2}
# res_strict_superset -> True

# pop() – remove and return a random element
F = {10, 20, 30}
popped_value = F.pop()
# popped_value -> (one of 10,20,30)
# F -> remaining two elements

# remove() – remove element (error if not present)
G = {1, 2, 3}
G.remove(3)
# G -> {1, 2}

# symmetric_difference() – elements NOT common
sym_diff = A.symmetric_difference(B)
# sym_diff -> {1, 2, 5, 6, 10}

# symmetric_difference_update() – replace with symmetric diff
H = {1, 2, 3}
H.symmetric_difference_update({3, 4})
# H -> {1, 2, 4}

# union() – join sets (all unique elements)
union_AB = A.union(B)
# union_AB -> {1, 2, 3, 4, 5, 6, 10}

# update() – add all elements from another set
I = {1, 2}
I.update({3, 4})
# I -> {1, 2, 3, 4}

# clear() – empty the set
I.clear()
# I -> set()

