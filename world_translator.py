"""
Write a function named hello_world that:
* takes 1 argument, a language code (e.g. "es", "pt", "en")
* returns "Hello, World" for the given language
It should return English if an invalid language code is specified.
"""
def hello_world(language_code):
    """
    >>> hello_world("en")
    'Hello, World'
    >>> hello_world("es")
    'Hola, Mundo'
    >>> hello_world("pt")
    'Olá, Mundo'
    """
    # YOUR CODE HERE
    if language_code=="en":
        return "Hello, World"
    elif language_code=="es":
        return "Hola, Mundo"
    elif language_code=="pt":
        return "Olá, Mundo"
    elif language_code=="cn":
        return "你好，世界"
    else:
        return "English"    
print(hello_world("cn"))
# I encourage you to add a favorite language and check it works in the console!
