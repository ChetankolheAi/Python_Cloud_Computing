# def issub(string, substring):
#     i =0;
#     j =0;
#     while i < len(string) and j < len(substring):
#         if string[i] == substring[j]:
#             j += 1 
#         i+=1
#     return j == len(substring)

# string = "Python Training"
# substring = "Python"
# result = issub(string, substring)

# if(result):
#     print("Substring found")
# else:   
#     print("Substring not found")


# text = "Score: 36"
# # if not text:
# #     print("Empty String")
# # else:
# #     for char in text.lower():
# #         if char in ("a" , "e" ,"i","o","u"):
# #             print(f"{char} is a vowel")
# #         elif not char.isalpha():
# #             print(f"{char} is not a letter")
# #         else:
# #             print(f"{char} is a consonant")  


# month = "February"

# month_31_days = ["January", "March", "May", "July", "August", "October", "December"]
# month_30_days = ["April", "June", "September", "November"]

# if month in month_31_days:
#     print(f"{month} has 31 days")
# elif month in month_30_days:
#     print(f"{month} has 30 days")
# else:
#     print(f"{month} has 28 or 29 days")


a =3
b =2
c =1

if a > b and b > c:
    print("Decreasing order")
elif a < b and b < c:
    print("Increasing order")
    