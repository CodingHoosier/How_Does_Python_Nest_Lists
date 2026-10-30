# https://www.youtube.com/watch?v=4VjaLPpTzVM
# How Does Python Nest Lists?
# Create a nested list
# It's a list of lists.
nested = [["bass", 
           "trout", 
           "perch"],
          ["walleye",
           "bluegill", 
           "crappie"],
          ["salmon",
          "catfish", 
          "carp"]
         ]
# Let's check some data types...
print(f"nested is a {type(nested)}")
print(f"nested[0] is a {type(nested[0])}")
# We can drill into a nested
#  list with indexing syntax.
print(f"nested[0][0]: {nested[0][0]}")
# We can loop through a nested list
for i, my_list in enumerate(nested):
    print(f"my_list {i}: {my_list}")
    for j, my_fish in enumerate(my_list):
        print(f"  my_fish {j}: {my_fish}")
# Let's add a new list 
#  to the nested list.
new_list = ["pike", 
            "muskie", 
            "sturgeon"]
nested.append(new_list)
# Now we have four lists 
#  in the nested list.
print(f"nested: {nested}")
print(f"length of nested is {len(nested)}")
# Now make a ragged nested list.
# That means the nested lists
#  are not all the same length.
ragged = [["bass", 
           "trout", 
           "perch"],
          ["walleye",
           "bluegill"],
          ["salmon",
          "catfish", 
          "carp"]
         ]
print(f"ragged[0] length: {len(ragged[0])}")
print(f"ragged[1] length: {len(ragged[1])}")
print(f"ragged[2] length: {len(ragged[2])}")
