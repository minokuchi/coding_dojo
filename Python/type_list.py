# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
#
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate 
# it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and 
# an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

mix_list = ['Holiday shopping madness','traffic',101,85,280]
int_list = [17,880,80,5,1]
str_list = ["presents", "snow", "skiing"]

def identify_list_type(list):
    new_string = ''
    total = 0

    for value in list:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The list you entered is of mixed type"
        print "String:", new_string
        print "The sum total of the numbers is:", total

    elif new_string:
        print "The list you entered is of string type"
        print "String:",new_string

    else:
        print "The list you entered is of number (int or float) type"
        print "The sum total is:", total

print identify_list_type(mix_list)
print identify_list_type(int_list)
print identify_list_type(str_list)
