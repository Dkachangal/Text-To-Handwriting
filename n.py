# a = ["hello", 'world']
# # for i in range(len(a)):
# #     print(a[i])
# b = [2]
# def add(a, b):
#     for i in range(len(a+b)):
#         print(i+1)
# print(add(a, b))

user_data = "This is some user data"
user_data_list = list(user_data)

# word len finder

def wlf(char, user_data_list):
    word_len = 5
    
    for i in range(len(user_data_list)):
            
            if (user_data_list[i] != " "):
                    word_len += 5
            else:
                break
    return word_len
char = "This"

print(wlf(char, user_data_list))

for i in range(len(user_data_list)):
    print(user_data_list[i])
