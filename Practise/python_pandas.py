name = 'hello   world  lol'

ans = []

names = name.split(' ')
# for n in names:
#     first = n[0].upper()
#     last = n[1:]    
#     new_name = first + last
#     ans.append(new_name)

print(' '.join(ans))
print(' '.join([word.capitalize() for word in name.split(' ')]))

print('mahi'.capitalize())
