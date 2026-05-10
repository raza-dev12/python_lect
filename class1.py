students= ["raza","Ahsan","Ik","talha","Ahmed","Mohsin","Ali","faraz"]
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

for s in students:
    if s == "Ahmed":
        break
    else:
        print(s)