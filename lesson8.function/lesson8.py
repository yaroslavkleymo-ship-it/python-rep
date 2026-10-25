# # # # # # # def draw_symbol(text,count):
   

# # # # # # #        print(text * count)

# # # # # # # draw_symbol("*",5)
# # # # # # 1.HOME
# # # # # # def amanfilm(name,film):
# # # # # #     print(name,film)
# # # # # # amanfilm("ticket1","Marvel")
# # # # # # amanfilm("ticket2","Host")
# # # # # # # amanfilm("ticket3","Spiderman")

# # # # # def double(m):
# # # # #     return m * 10
# # # # # result = double(6)
# # # # # print(result  + 34)
# # # # # 2.HOME
# # # # # def get_square(number):
# # # # #     return number ** 2

# # # # # result = get_square(6)
# # # # # print(result + 10)

# # # # # 3.HOME

# # # # # def check_age(age):
# # # # #     if age > 12:
# # # # #         return "Kid"
# # # # #     if 12 < age > 17:
# # # # #         return "Teen"
# # # # #     if age > 18:
# # # # #         return "Adult"
    
# # # # # print(check_age(19))

# # # # # def print_alexander():
# # # # #     birth_year = 356 
# # # # #     print("Alexander the Great was born in", birth_year,"BC.")

# # # # # print_alexander()

# # # # 4.HOME
# # # # city = 'Moscow'
# # # # def show_city():
# # # #     city = "London"
# # # #     print(city)
# # # # show_city()
# # # # print(city)

# # # def get_sum(*args):
# # #     print(f"Переданные аргументы: {args}")
# # #     totalsum = 0
# # #     for num in args:
# # #         totalsum += num
# # #     return totalsum
# # # print(get_sum(1,2))
# # # print(get_sum(1,255))
# # # print(get_sum(1,24))

# # def print_info(name, *args,**kwargs):
# #     print(name)
# #     print(args)
# # #     print(kwargs)
# # # print_info("Amantur",1,4,4,3,34,country="greece", age="31",city="pella")
# # # 5.HOME
# # def get_average(*args):
# #     return sum(args) / len(args)
# # print(get_average(4,6,4,23))


# def calculate_total(price: int,quantity: int,has_dicsount: bool):
#     total = price + quantity
#     if has_dicsount:
#         total -= 10

#     return total
# print(calculate_total(price=15,quantity=40,has_dicsount=True))