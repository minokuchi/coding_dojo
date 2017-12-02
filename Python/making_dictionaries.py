# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary. The first list contains 
# keys and the second list contains the values. Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings. Here are two example lists:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(list1, list2):
    new_dict = {}
    for i in range(0, len(list1)):
#        print i
        new_dict[list1[i]] = list2[i]
    print new_dict
    return new_dict

make_dict(name,favorite_animal)
