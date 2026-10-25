# # # # # for i in range(7):
# # # # #     print(i,"Hello-hi")\
    
# # # # for i in range(4, 10):
# # # #        text = "Hooo"
# # # #        print(i,text)

# # # for i in range(1,50,11):
# # #     text = "hiiiiii"
# # #     print(i,text)

# # number = int(input("enter: "))
# # while number < 10:
# #     print("trueeee")

# count = 0
# while count <= 5:
#     print(count, "hiiiii")
#     count += 1

target = 1000
current_sum = 0
count = 0
while current_sum < target:
    deposit = int(input("enter number: "))
    current_sum += deposit
    count += 1
print("current ", current_sum) 
print("count ", count) 