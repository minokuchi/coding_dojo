import random                             # import random module

def coin_toss(iter):                      # declare function coin_toss with 1 parameter - number of iterations
    attempt_count = 1                     # set attempt_count to 1
    heads_count = 0                       # heads_count to 0
    tails_count = 0                       # tails count to 0
    result = ""                           # set result to an empty string

    for i in range(1, iter):              # for loop using range function starting from 1 to defined iteration
        new_toss = random.randint(0,1)    # random.randint() will randomly output either 0 or 1
#       print new_toss                    # print statement to view result of above function
        if new_toss == 1:                 # if output is 1 then count 1 heads and print line below
            heads_count += 1
            result = "heads"
            print "Attempt #", attempt_count, ": Throwing a coin... It's  ", result, "! Got ", heads_count, "heads so far and", tails_count, "tails so far"
        else:
            tails_count += 1              # if output is 0 count 1 tails and print line below
            result = "tails"
            print "Attempt #", attempt_count, ": Throwing a coin... It's  ", result, "! Got ", heads_count, "heads so far and", tails_count, "tails so far"
        attempt_count += 1                # keep running count of the number of attempts

coin_toss(5001)                           # call function coin_toss with 5001 iterations
