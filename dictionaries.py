programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected."
    , "Function": "A piece of code that you can easily call over and over again."
    ,
}

#print("first print", programming_dictionary)

#adding new items to dictionary:
programming_dictionary["loop"] = "The action of doing something over snd over again"

#Create an empty dictionary:
empty_dictionary = {}

#Wipe existing dictionary:
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary:
programming_dictionary["Bug"] = "A moth in your computer"
#print("second print", programming_dictionary["Bug"])

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#print("third print", programming_dictionary)

#nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in dictionary:
#Nest a dictionary in a dictionary:
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"] },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Mexico": {"cities_visited": ["Cancun", "Riviera Maya"] }, "number_of_visits": 2,
}

#print(travel_log["Mexico"]["cities_visited"][1])
#print(travel_log["number_of_visits"])

#Nesting Dictionaries in a list:

travel_log_2 = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"] 
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"] 
    },
    {
        "country": "Mexico", 
        "cities_visited": ["Cancun", "Riviera Maya"] , 
        "number_of_visits": 2, 
    },
]

print(travel_log_2[0]["cities_visited"][1])