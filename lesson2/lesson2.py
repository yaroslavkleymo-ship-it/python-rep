# # # commander = input("input the best commander: ")

# # # if commander == 'Makedonskiy':
# # #     print('True')
# # # else:
# # #     print('False')


# # num = int(input("enter the number: "))
# # if num % 2 == 0:
# #    print("Even")
# # else:
# #      print("odd")

# # HOMEWOPK
# is_sunny = True
# is_weekend = False
# if is_sunny and is_weekend:
#     print('Идеальный день прогулки')
# elif is_sunny and not is_weekend :
#     print('Погода хорошая но нужно поработать')
# elif not is_sunny and is_weekend :
#     print('Можно остаться дома и отдохнуть')
# elif not is_sunny and not is_weekend == False:
#     print("Рабочий день с плохой погодой")

#  HOMEWOPK2

person = int(input("введите свой возраст: "))

if 0 <= person <= 7:
    print("Ticket is free")
elif 8 <= person <= 17:
    print("Ticket is 150 som")
elif 18 <= person <= 64:
    print("ticket is 300 som")
elif person >= 65:
    print("Ticket is 200 som")
else:
    print("возраст неправильный")