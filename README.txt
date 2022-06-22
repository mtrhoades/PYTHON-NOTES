PYTHON NOTES:

***********************************************************************************
Module 1:



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

****************************************************************************************************************************
Module 2:


Multiple returns ---> 
    Python functions are able to return multiple values.
    Multiple return values should be listed after the return keyword and separated by a comma.
    When multiple values are returned, they are returned in a tuple.
        
        def two_returns (param1, param2) :
            value1 = param1 + param2
            value2 = param2 - param1

            return value1, value2

    When a function returns multiple values, there are two ways to handle it: 
        As a single tuple object, or as multiple objects.
        By using the same number of variables as returned values, we can "catch" each value independently, instead of iterating to grab each value.


Nested Functions --->
    Just as in JS, Python functions may contain one or more internal (or nested) functions.

Default Arguments --->
    As in JS, Python functions may accept default arguments when declaring a function by using the assignment operator (=).
    Important! Once a default argument has been declared, all subsequent arguments must also have default values in Python.

Arbitrary Arguments(*args) ---> 
    Python functions may accept an arbitrary number of arguments through use of the unpacking operator (*).

    The unpacking operator (*) creates an iterable tuple.

    Any parameter name may be used after the unpacking operator (*). *args is the standard when passing in a function argument.

    The unpacking operator can be used in other places besides passing in function arguments.


Recursion --->
    when a function calls itself over and over until it reaches a a specified stopping condition.
        Base case: When a condition has been reached, calls to the same function stop.
        Recursive case: When the function calls itself again and again until the desired base case is met.

            4! = 4*3*2*1 = 24
            7! = 7*6*5*4*3*2*1 = 5040 || 7*6*5*24 = 5040

    def recur_fact(n):
        if n <= 1:
            return n
        
    * two parts in a recursive function:
        - base case
        - recursive case


Recursive --->

        def find_fact(num):
            if num == 1:
                return 1

            return (num * find_fact(num-1))

        n=4
        print(find_fact(n))

    VS.

Iterative --->

        def find_fact(num):
            factorial = 1

            for i in range(1, num+1):
                factorial = factorial * i
            return factorial

        n=4
        print(find_fact(n))


When should I use recursion?
    •When the problem can be broken down into smaller and smaller repetitive problems.
    •When a problem is defined in terms of itself.

* use Direct Recursion as suppoped to Indirect Recursion most of the time...

* Remember, a recursive function must have a base case, or the condition under which recursion should stop.
    It must also have a recursive case that will go deeper into the call stack.

kwargs --->
    operates in a similar way to *args, but for keyword or named arguments.

        def concat(**kwargs):
            concatted = ""
            for i in kwargs.values():
                concatted += i
            return concatted

        concat (a="Writing", b="Python", c="Functions", d="Is, e="Great")

    The function is defined using the keyword unpacking operator (**).
    At call time, the function is ready to receive any number of named arguments.

    **kwargs converts all arguments passed at call time to a dictionary.
    This is why **kwargs only works with named arguments.

Combining Features --->
    These argument types we've covered so far may be combined within functions:
        •Default arguments
        •Arbitrary arguments
        •Keyword arguments

* Python has a number of incredibly useful functions that the interpreter already knows.
    It is often best to find out if something you want to do already exists as a built-in function (such as finding the 
    maximal element of a list).

    Refer to Python documentation for a comprehensive list.

Python Review (so far):
    •**kwargs allows functions to accept any number of named arguments.
    •Python has a number of very helpful built-in functions that can be called at will.
    •Recursive logic in Python functions mirrors that of other languages, such as JS.