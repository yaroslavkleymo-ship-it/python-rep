# # # # try:
# # # #     number = int(input("Введите число"))
# # # #     print(10 / number)
# # # # except ZeroDivisionError:
# # # #     print("Произошла ошибка")
# # # # except ValueError:
# # # #     print("Бро введи число")

# # # try:
# # #     number = int(input("Введи число"))
# # #     print(10 / number)
# # # except Exception as error:
# # #     print(f'Произошла какая то ошибка: {error}')
# # # else:
# # #     print("Ошибка не произошла")
# # # finally:
# # #     print("Этот текст будет выведен всегда")
# # age = int(input("Введите возраст"))
# # if age < 0:
# #     raise ValueError("Введите корректный возраст")
# # HOMEWORk
# user = {'name': 'Amantur','age': 19}
# try:
#     email = user['email']
    
# except ValueError:
#     raise ValueError("Ключа Email нет")
