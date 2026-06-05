######## python function:
# print()
# type()
# int()
# float()
# str()
# inpt()
# min()
# max
# sum 
# length etc ----
#-------python class function--------- 
# dict.pop
#str.lower()
# tuple.count()
# set.differerce()
# user defined functions
# def say_hello():
#     print("hello")
# say_hello()    

# def add():
#     a=10
#     b=20
#     print(a+b)
# add()    
# add()   # more time to print call it  the function

# definig a  parametrized function
# def say_hello(name):
#     print(f"Hello {name}")
# say_hello('ahmed')    

# def fahrenheit_to_celsius(fahrenheit):
#   return (fahrenheit - 32) * 5 / 9

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(95))
# print(fahrenheit_to_celsius(50))


# def my_function(name = "friend"):
#   print("Hello", name)

# my_function("ALi")
# my_function("Ahmed")
# my_function("farhan")
# my_function("zameer")

# creates a text analyzing checker with aplhabets,puntuation,spaces,numberl,lowercase, uppercase,vowels

def text_analyzer(txt):

    length = len(txt)
    words = len(txt.split())
    sentences = len(txt.split("."))
    paragraphs = len(txt.split("\n"))

    vowel_letters = "aeiouAEIOU"
    punc = ". , ? ! : ; ' \" ( ) [ ] { } - _ / \\ @ # $ % & * + = < > | ~ ^"

    alphabets = 0
    punctuation = 0
    spaces = 0
    number = 0
    lower_case = 0
    upper_case = 0
    vowels = 0
    others = 0

    for char in txt:

        if char.isalpha():
            alphabets += 1

            if char.isupper():
                upper_case += 1

            if char.islower():
                lower_case += 1

            if char in vowel_letters:
                vowels += 1

        elif char.isspace():
            spaces += 1

        elif char.isnumeric():
            number += 1

        elif char in punc:
            punctuation += 1

        else:
            others += 1

    print(f"""
Text length : {length}
Words : {words}
Sentences : {sentences}
Paragraphs : {paragraphs}
Upper Case : {upper_case}
Lower Case : {lower_case}
Spaces : {spaces}
Numbers : {number}
Alphabets : {alphabets}
Vowels : {vowels}
Punctuation : {punctuation}
Others : {others}
""")


text_analyzer("""
I’d come up with every excuse possible not to attend the dreaded family Christmas, this time held by my teetotaler Baptist brother. At least at our mother’s home, we’d be able to drink55555. How could we possibly get through the festivities without alcohol?

My complaint fell on deaf ears.

When I arrived, the house was empty, no cars, no lights. A present for me was left on the porch. “Merry Christmas, you got what you wished for.” Inside the wrapping was a bottle of bourbon whiskey. I sat on the porch feeling lost. And when the snow fell, I cried




 """)




















































