# SECTION 1: LISTS (Methods & Slicing)

#  QUESTION 1
market = ["Yam", "Tomato", "Onion"]
market.append("Fish")
print(market)  

#  QUESTION 2
grades = [80, 90, 70]
grades.insert(1, 85)
print(grades) 

#  QUESTION 3
gadgets = ["Laptop", "Phone", "Tablet", "Phone"]
gadgets.remove("Phone")
print(gadgets) 

#  QUESTION 4
colors = ["Red", "Blue", "Green"]
colors.clear()
print(colors)  

#  QUESTION 5
votes = ["Yes", "No", "Yes", "Yes", "No"]
count_yes = votes.count("Yes")
print(count_yes)

#  QUESTION 6
alphabets = ["a", "b", "c", "d", "e", "f"]
sliced = alphabets[2:5]
print(sliced)  

#  QUESTION 7
students = ["Kofi", "Ama", "Yaw"]
students.reverse()
print(students) 

#  QUESTION  8
list_a = [1, 2]
list_b = [3, 4]
list_a.extend(list_b)
print(list_a) 

#  QUESTION  9
cities = ["Accra", "Kumasi", "Tamale"]
removed_city = cities.pop(2)
print(removed_city) 
print(cities)  
#  QUESTION 10
items = ["Pen", "Ruler", "Eraser"]
index = items.index("Ruler")
print(index)  

# SECTION 2: TUPLES & DATA TYPES

#  QUESTION 1
student_info = ("Araba", 20)
print(student_info)
print(type(student_info))

# QUESTION  2
tup = (1, 2, 3)
tup_list = list(tup)
tup_list.append(4)
tup = tuple(tup_list)
print(tup) 

#  QUESTION  3
data = (10, 20, 10, 30, 10)
count_10 = data.count(10)
print(count_10)  

#  QUESTION  4
colors = ("Red", "Blue", "Green")
index_blue = colors.index("Blue")
print(index_blue) 

# QUESTION  5
coords = (5.6, -0.1)
lat, lon = coords
print(lat, lon)  

#  QUESTION 6
nest = [(5, 10)]
print(len(nest)) 

# QUESTION 7
numbers = (10, 20, 30, 40, 50)
last_two = numbers[-2:]
print(last_two) 

# QUESTION 8
my_list = [1, 2]
my_list.extend((3, 4))
print(my_list) 

#  QUESTION 9
#  del my_tup 

#  QUESTION 10
x = (5)
y = (5,)
print(type(x)) 
print(type(y))