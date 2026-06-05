# def abc():
#     print("Hello")
# abc()
# # overloading
# def abc(name):
#     print("Bye" ,name)
# abc()

# def add_nums(num1, num2):
#   return num1 + num2 
# add_nums(2,3) 
# add_nums(45,78) 

# arbitory number of arguments:

# def add_nums(*num):
#     return sum(num) 
# add_nums(1,2,3,4,5,6,7,8)

# def add_even_nums(a, b, c , *nums):
#     res = 0
#     for n in nums:
#         if n%2==0:
#             res+=n
#     return res,a,b,c
# print(add_even_nums(100,200,300,1,2,3,4,5,6,7,8,10,50,99))    
  

# Positional Arguments & keyword Arguments:
# def say_full_name(first_name,midde_name,last_name):
#     return f"{first_name} {midde_name} {last_name}"
# print(say_full_name('hafiz','shirjeel','ali'))

# default parameter values:

# def say_full_name(first_name,midde_name,last_name):
#       return f"{first_name} {midde_name}{last_name}"
# print(say_full_name('hafiz','shirjeel' ))

# Arbitrary Keyword Arguments:
def make_my_profile(name,subject,last_qualification,experience,**other_info):
    return {"Name":name,"Subject":subject,"Qualification":last_qualification,"Experience":experience}
print(make_my_profile('nasir','DataScience','Ms','20'))
