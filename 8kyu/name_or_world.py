# Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).


def hello(name = ''):
    if len(name) > 0:
        name = name.capitalize()
    else:
        name = 'World'

    return "Hello, {}!".format(name)


print(hello())
print(hello('john'))
