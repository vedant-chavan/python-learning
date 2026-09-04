courses = ['python', 'java', 'c++', 'javascript', 'html', 'css']
courses1 = ['sql', 'c#', 'ruby']
# print(type(courses), courses)
# print(type(courses1), courses1)

# print(courses[0])
# print(courses[-1])
# print(courses[1:4])
# print(courses[:3])

# courses.append('sql')
# print(courses)

# courses.extend(courses1)
# print(courses)

# courses.insert(2, 'c#')
# print(courses)

# courses.remove('c++')
# print(courses)

# popped = courses.pop()
# print(courses)
# print(popped)

courses.reverse()
print(courses)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number.sort(reverse=True)
print(number)
courses.sort()
print(courses)
print(min(number))
print(max(number))
print(sum(number))


print(courses.index('html'))

print('fsvfdsv' in courses)
print('fgdt' not in courses)

for index, item in enumerate(courses, start=1): # for item in courses:
    print(index, item)

courses_str = ', '.join(courses)
print(courses_str)