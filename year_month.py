


date=int(input("enter the dat:"))
if date>=0 or date<=31:
    month=int(input("enter the month:"))
    if month>=0 or month<=12:
        year=int(input("enter the year:"))
        if year>=1800 or year<=2021:
            print(date+1,month,year)
        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("invalid")

# num=int(input("enter the number"))
# if num>=0:
#     print("positive")
#     num=int(input("enter the number"))
#     if num<=0:
#         print("negative")
#         num=int(input("enter the number"))
#         if num<=0:
#             print("zero")







