dict = {"name:": "Mark", "age:": 39, "country of birth:": "USA", "favorite programming language:": "Python"}

def about_me(dict):
    for key,value in dict.iteritems():
        print "My" + " " + key + " " + "is" + " " + str(value)

about_me(dict)
