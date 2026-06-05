# students= ["raza","Ahsan","Ik","talha","Ahmed","Mohsin","Ali","faraz"]
# for n in range(10):
#     print(n, students[n])
# for n in range(10):
#     print(n,students[n])

# for i in students:
#     print(f"-hello {i}")
# for n,s in enumerate(students[::-1]):
#     print(n,s)


# fruits = ['apple','orange','banana']
# for n,f in enumerate(fruits):
#     print(n,f)
# print(students)

# for a in range(1,100):
# #     print(a)
# -------- continue , break ----
# for s in students:
#    if len(s)<5:
#        print(f"Dear Mr .{s}, kal apki chutti hy")
#    else:
#        print(f"dear Ms.{s}, kal class mai ana hy") 

# for s in students:
#     if s == "Ahmed":
#         break
#     else:
#         print(s)





# guests = []
# for barati in range(5):
#     name = input("Enter guest name")
#     guests.append(name)
# guests

# for a in range(10):
#     if a ==5:
#         continue
#     else:
#         print(a)

# menu = []
# for a in range(5):
#     dish = input("enter your dish name")
#     if dish == "fish":
#         continue
#     menu.append(dish)
# menu
# rates = {}
# items = ["biryani","Karahi","Qorma","fish","kheer"]
# for i in items:
#     price = input(f"{i} for 300 people")
#     rates[i] =price
# print(rates)   
# shop = ['charger','handfree','usb','powerbank','mouse','keyboard']
# cart = {}
# for i in shop:
#     price = input(f"what is the price of  {i}")
#     cart[i] = price
# print(cart)
# import random 
# secretNumber = random.randint(1,10)
# chances = 3
# while chances > 0:
#     guess= int(input("Guess a number between 1 and 10:"))
#     if guess == secretNumber:
#         print("you win")
#         break
#     else:
#         chances-=1
#         print("wrong guess")
#         print("chances left:",chances)
# if chances == 0:
#     print("Game Over:")
#     print("Chances Number was",secretNumber)
            
# pizza_names = ['fagita', 'macroni','peproni']
# for a in pizza_names:
#     print(a)

# million = list(range(1,1000000))
# # print(million)
# print(min(million))
# print(max(million))
# print(sum(million))

# odd_num = list(range(1,20,2))
# print(odd_num)

# for i in list(range(3,31,3)):
#     print(i)
# cubes =[]
# for a in range(1,12):
#     cubes.append (a**3)
# print(cubes)

# print(f"first three item in the list are : {cubes[:3]}")
# print(f"first three item from the middle of the list are:{cubes[4:8]}")
# print(f"last three item of the list are:{cubes[-3:]}")


# resurent_buffet = ('biryani','pulao','karahi','mutton kunna','cream kasata')
# for f in resurent_buffet:
# #     print(f"- {f}")

# alien_color = input('Enter alien color:').lower()
# if alien_color =='green':
#     print("the pklayer just earned 5 points")
# elif alien_color !='green':
#     print(f"the palyer just earned 10 points")

names = [['n1','n2','n3'],['n4','n5','n6'],['n7','n8','n9']]
print(names[2][2])
print()
names[2].append("hassan")