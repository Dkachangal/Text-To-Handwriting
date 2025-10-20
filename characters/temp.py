dict = {
    'a': "this is some text1",
    'b': "this is some text2",
    'c': "this is some text3"
}
dict["o"] = 'a'
for i in range(0, 10):
    dict["i"] = "a"

# x = 'x'
# dict[f'{x}'] = 'this is x'
# print("Keys")
# for i in dict:
#     print(i)
# print("values")
# for i in dict:
#     print(dict[i])

for i in dict:
    # img = Image.open(f"{i}.jpg").convert("L")
    # chars[f"{i}"] = img
    print(f"{i}")
# print(i) -> keys
# print(dict[i]) -> values