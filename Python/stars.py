def stars(arr):                                        # declare array stars with 1 parameter "arr"
    for x in arr:                                      # for loop iterating through array
        print "*" * x                                  # prints "*" the number of times specified in the array

nums = [6,2,5,7,9]                                     # array declared
stars(nums)                                            # star function is called and the array nums is passed to it 

def stars2(arr):                                       # declare function stars2 with 1 parameter "arr"
    for x in arr:                                      # for loop iterating through the array
        if isinstance(x, int):                         # if x is of type "int"
            print "*" * x                              # print "*" times x
        elif isinstance(x, str):                       # else if x is of type "str"
            length = len(x)                            # retrieve the length of x
            letter = x[0].lower()                      # convert the first element of the string to lower case
            print letter * length                      # print "*" times length

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]      # list x declared
stars2(x)                                              # function start2 called 
