PYTHON NOTES:

***********************************************************************************

* one of the easiest and most powerful languages to learn.

What is python used for:
    web/app development
    data science/data handling
    IoT devices
    machine learning/AI
    building applications

Demand for Python --->
    Most of python's utility comes from its ease of use and flexibility.
        server-side programming
        rich package library
        API/data handling

Python --->
        - designed for readability, so its easy to read and write.
        - has strong capabilities for data anlytics (large data sets), server building, API handling, and back-end setups.
    vs.
JavaScript --->
        - The ease of front-end and UI development makes it a valuable language to learn.
        - Runs easily in the browser, so its intuitive to make changes in a live environment.

Variables --->
    - NO KEY WORD! (like var, let, const)
    - they are created when values are assigned to them.
        x = 5

print() ---> the print statement allows us to ouput variables, to the terminal.

functions --->
    The def keyword is required before the name of the function, and a colon (:) starts the function block.

        def intro(name)
            print("Hey " + name)

    The code that we want to run inside the function will be indented.

    Indents are how we separate blocks in Python (in JS we use {}) - all indents MUST be the same, either the same number of spaces or tabs.

comments --->
    single line comments denoted by #

        # This is a one line comment

    multiline comments denoted by """ or '''
        ''' This is a multi-line
            comment '''

lists --->
    similar to arrays in JavaScript

        Just like in JavaScript, the list items are indexed with the first item being at index [0].

        Python has list methods that can allow us to manipulate a list of data.

            months_list = ["Sept", "Oct", "Nov"]

strings --->
    Strings work similarly in Python and  JavaScript.

        my_string = "Hello World"

    Python has an advantage when working with strings; it allows strings to be indexed like a list!

    It may not seem like much, but the amount of flexibility that Python offers you is significant!

string methods ---> 
    capitalize turns the first character to uppercase.

    title turns the first character of each word to uppercase (typically a more strenuous task in JS).

    split splits a string into a list with a separator.

    Without a separator, it splits each word into a list item.

dictionary --->
    Dictionaries are the equivalent of objects in JavaScript.

    Like with JS objects, dictionaries store properties or data values in key:value pairs and are declared with curly brackets.

tuples --->
    similar to lists

    they are used to store mulitple items in a single variable.

    as a collection of data, tuples are ordered and immutable(unchangeable)

        flowers_tuple = ("roses", "sunflowers", "daisies")

        print(flowers_tuple)
        print(flowers_tuple[1])

sets ---> 
    Sets are another data type that allow us to store multiple elements together.
    
    Unlike tuples, sets are not ordered or indexed.
    
    Elements in a set must be immutable, but sets themselves are mutable (we can add and remove elements).
    
    Sets do not allow duplicates. If a duplicate element is added, it will be ignored.

Tuples --->
        Immutable (unchangeable)
        Accepts any data type
        Ordered and indexed
        Allows duplicates
        Written with parentheses ()
    vs.
Sets --->
        Mutable (changeable)
        Accepts any data type
        Unordered
        Does NOT allow duplicates
        Written with curly brackets {}

conditional statements ---> 
    
    weather = "rain"

    if weather == "rain":
        print("bring an umbrella")
    elif weather = "sunny":
        print("have a great day")
    else:
        print("look out the window!")



== ---> comparison
=  ---> is really equal to
!= ---> is really not equal to


while loops --->

    a = 1

    while a < 12:
        print(a)
        a += 1


For-each loops --->

    fav_movies = ["Departed", "Inception", "Aladdin"]

    for i in fav_movies:
        print(i)


Python Function Syntax --->
    Basic function anatomy:
        The keyword def declares the function. 
        The function name follows. Parentheses enclose all expected parameters, followed by a colon.
        The return statement signals the end of the function block.

            def my_function( parameters ):
                ...

                return [expression]


    * Caution! *
        Python function blocks must be indented (tabbed).

        Improper indenting in Python will throw a syntax error.

    Python functions may be called freely or within other Python functions.

    Functions should be called by name, followed by parentheses enclosing the function arguments.

        def print_name(firstname):
            print(firstname)

            print_name("Luke Skywalker")


