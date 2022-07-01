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

**************************************************************************************************************************
Module 3:

OOP ---> Object Oriented Programming
    4 pillars:
        •Encapsulation - bundling information together
        •Abstraction - hiding unnecessary information
        •Inheritance - reusing code where possible
        •Polymorphism - using the same interface for different classes

    * represent objects through classes in python


**************************************************************************************************************************
Module 4:

Lambda functions --->
    A small, anonymous function.
    Sometimes, it is useful to define a small function on the go without naming it. This is where lambda functions come in handy.
        •lambda - the keyword to start a lambda function
        •parameters - a list of parameters 
        •: - a colon to separate the parameters from the expression 
        •expression - the expression to resolve
        •Note that any lambda function can also be written as a standard function

    * ^ very similar to anonymous function in javascript.

List Comprehensions --->
    •list - the variable to save the list to
    •[] - encasing an expression and loop, denotes the start of a list comprehension
    •expression - what to do to each element before putting it in the list
    •for...in - loop through the iterable to make the new list

Set Comprehensions --->
    •set - the variable to save the set to
    •{} - encasing an expression and loop, denotes the start of a set comprehension
    •expression - what to do to each element before putting it in the set
    •for...in - loop through the iterable to make the new set
    •if... - optional expression to filter the elements

Dictionary Comprehensions --->
    •dict - the variable to save the dictionary to
    •{} - encasing a key, expression, and loop; denotes the start of a dict comprehension
    •key: expression - what to name the key and do to the element before saving it in the dict
    •for...in - loop through the iterable to make the new dict


Error Handling --->
    3 main types of errors:
        Syntax (logic) errors
        Execution bugs
        Runtime exeptions


************************************************************************************************************************
Module: 5

* for web development, Python is only used for the back-end.

WSGI --->
    the convention describing how python web applications interact with the web.

Python web frameworks --->
    Flask: a lightweight framework, install functionality as you need it, faster learning curve.
        - considered a micro and unopinionated framework, similar to Express, Flask leaves everything in our hands.
        - can easily be installed with pip. (be sure to install it within a project's activated virtual environment.)
            $ pip install Flask
        - flask apps are created as an instance of the flask class.
            configuration and routes can then be created on that instance.
        - routes in flask are written using .route() on the app instance.
            it accepts the routes endpoint as its first argurment and what the route will do should be defined directly underneath it.
        - the @app.route('/') uses the @ which denotes the use of a decorator, which is a function that extends the functionality of an existing function.

    Django: a more opinionated framework, comes with "batteries included", such as in ORM, slower learning curve.


Flask Routes and the Application Factory --->
    Routes are defined by calling .route on an app instance.

    By default, Flask will assume it is a GET route.

    To specify an HTTP method, use the methods parameter:
        @app.route('/', methods='POST')
    .route accepts optional parameters.

    The methods parameter expects a list of methods.
        More than one can be defined for a single endpoint.

    Flask can check an incoming request type by utilizing the request object keyword.
        Routes receive the request body object when a request is made to it.

    Route parameters can be defined in Flask by wrapping them in <>
        •They must be passed as arguments to the route function to be accessible.
        •The expected datatype can be defined if desired.

The problem with a global app instance:
    Global app instances don't scale.
    •Flask apps are dependent on the instance.
    •Modularizing logic requires importing the instance multiple times.
    •Modularizing logic can cause circular dependencies.

Flask application factory:
    A common pattern to solve the previous problems.
    •Creates the instance inside a function.
    •Handles any configuration and initialization required for the app.
    •Imports modularized logic into one place.

    Application Factory Function ---> 
        
        def create_app():
            #create the app instance
            app = Flask(__name__)

            # write any config required here

            # return the app instance
            return app

* Rather than having a root app.py file, the entire project's logic is held inside a nested project directory.
    The application factory should be created in an __init__.py file so the entire app can be imported into the entry file.

How to modularize logic in Flask applications?
    Blueprints organize related routes and views together.
    Similar to creating controllers in Express.

    Blueprint Syntax --->
        •bp = Blueprint(...): Create an instance of the Blueprint class.
        •"posts': Defines the blueprint's name.
        •__name__: Tells the blueprint where in the project it's defined.
        •url_prefix: Defines the blueprint's url prefix.


            # import the blueprint classs
            from flask import Blueprint

            # intstantiate the blueprint
            bp = Blueprint (
                'posts',\
                __name__,
                url_prefix='/posts'
            )


    Defining routes on a blueprint is the same as defining routes directly on the app.
    Each route defined on the blueprint will use the previously defined url_prefix.

    Registering Blueprints: 
        Importing and registering it to the app with the built-in register_blueprint() method.

How to return views?!
    Jinja --->
        Flask facilitates server-side rendering through Jinja.
        It is a templating engine that allows embedding Python code into HTML files.

        render_template() is the built-in method used to render Jinja templates.

        •'index.html': This is the template to render. It will look for templates in a folder called templates.
        •title='...': After the first argument, it accepts any amount of arguments of variables to pass to the template.

            There are two different ways:
                1.Embedding variables: Encase the variable name in two curly braces.
                2.Embedding logic: Encase the logic in curly braces and percent signs.


**************************************************************************************************************************
Module 6:

The Request Object --->
    The request object holds all necessary information about a request, including any data given by the user.
        •It must be imported from the flask package to be used.
        •It contains built-in methods and attributes that hold all necessary data about the request.

    request.method
        - provides the HTTP method with which the request was sent.
    request.form
        - Holds all user-given data in a dictionary. 
        - Individual values can be accessed with keys using bracket notation.

    After handling action methods like POST, sometimes we'll want to redirect afterwards.
    To do so, simply use the redirect() method.
    It accepts the URL for redirection.

Database Integration with Flask --->
    
