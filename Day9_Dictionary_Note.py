
#Note: It is really important that you have str for keys and description
"""
in a dictionary we have a key value pair {key:value}

in nested we can also combine such as
{
  Key:[list],
  Key2: value2,
  key3: {Dict}
}
"""
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

#dictionary identify by their key..
print(programming_dictionary["Function"])

#adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#create an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in an dictionary
programming_dictionary["Bug"] = "A moth in your computer"

#Loop through a dictionary

This code just give us the key
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#Exercise Challenge 1
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {} #this is where we gonna fill up using our programme

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  score = student_scores[student]# just the key, which are their names
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)

##########################################################################
#Nesting
capitals = {
  "France":"Paris",
  "Germany":"Berlin"
}
#Nesting a list in a dictionary
travel_log = {
  "France":["Paris","Lille","Dijon"]
  "Germany":["Berlin", "Hamburg"]
}
# Nesting dictionary in a dictionary

travel_log = {
  "France":{"cities_visited":["Paris","Lille","Dijon"], "total_visits":12},
  "Germany":{"cities_visited":["Berlin", "Hamburg"], "total_visits":2},
}
#Nesting Ddictionary in a list
travel_log = [
  {
  "Country":"France",
  "cities_visited":["Paris","Lille","Dijon"], 
  "total_visits":12
  },
  {"Country":"Germany","cities_visited":["Berlin", "Hamburg"], "total_visits":2},
]

# Exercise Challenge 2
"""
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.

add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])

"""

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country) #Use the append method, so we grab hold of the inputs and insert it


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

"""
print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])
"""