# string functions

# print(len('hello world'))
# print(max('hello world'))
# print(min('hello world')) # space
# print(sorted('hello world'))
# print(sorted('hello world',reverse=True))

s='heLlo wOrlD'
# print(s.capitalize()) # first char of string is capitalized
# print(s.title()) # every word is capitalized
# print(s.upper()) # all char to upper case
# print(s.lower()) # all char to lower case
# print(s.swapcase()) # caps to low and visa versa

# print(s.count('l'))
# print(s.find('x')) # if pres then gives idx, otherwise -1
# print(s.index('h'))

# Gives boolen value
# print(s.endswith('sho'))
# print(s.startswith('he'))

# format() is used for filling
name='autha'
age=19

# print('Hi my name is {} and I am {} years old'.format(name,age))
# print('Hi my name is {1} and I am {0} years old'.format(name,age)) #also perform postining


print('autha211'.isalnum()) # isalnum() checks if string is alphanumeric??
print('autha21%1'.isalnum()) # if string is numeric

print('autha211'.isalpha()) # if string is alphabatic
print('211'.isdigit()) # if string is numeric
print('autha-211'.isidentifier()) # is string a valid identifier