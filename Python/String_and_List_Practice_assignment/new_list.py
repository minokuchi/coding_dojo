x = [19,2,54,-2,7,12,98,32,10,-3,6]
print "starting list", x
x.sort()
print "starting list sorted", x
first_list = x[:len(x)/2]
second_list = x[len(x)/2:]
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print "new list", second_list
