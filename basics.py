


print("""Hello!
my name is 
zoro!""")
name = "vedant"

print(f"hiii {name} how are you?" )
print("hiii {} how are you ?". format(name))


numbers = [1,2,3,4,5,9,8,6,11]
high = 0
second_high = 0
for num in numbers:
    if num > high:
        second_high = high
        high = num
    elif num > second_high and num != high:
        second_high = num
print(high)
print(second_high)
sorted_num = sorted(list(set(numbers)))
print(sorted_num[-2])

