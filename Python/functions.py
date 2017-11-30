def odd_even():
    for i in range(1,2001):
        if i %  2 is 0:
            print  i, "This is an even number."
        else:
            print  i, "This is an odd number."  

odd_even()


def multiply(list, num):
    for i in range(0, len(list)):
        list[i] *= num
    return list

numbers_list = [2,4,10,16]

print multiply(numbers_list, 5)

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
