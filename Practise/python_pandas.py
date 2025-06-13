# name = 'hello   world  lol'

# ans = []

# names = name.split(' ')
# # for n in names:
# #     first = n[0].upper()
# #     last = n[1:]    
# #     new_name = first + last
# #     ans.append(new_name)

# print(' '.join(ans))
# print(' '.join([word.capitalize() for word in name.split(' ')]))

# print('mahi'.capitalize())

date = '$$$2025-06-06$$$'
print(date.strip('$'))

full_name = '968-Maria, ( D@t@ Engineer );; 27y '

name = full_name[4:9].lower()
role = full_name[12:25].replace('@','a').lower()
age = full_name[-4:-2]
final_name = f'name: {name} | role: {role} | age: {age}'

print(final_name)
