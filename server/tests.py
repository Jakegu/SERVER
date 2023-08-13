from config import me


def read():
    print(me["name"])

def modify():
    me["age"] = 98
    print(me)

def create():
    me["prefered_color"] = "blue"
    print(me)

def remove():
    me["hobbies"].pop()
    print(me)







read()
modify()
create()
remove()