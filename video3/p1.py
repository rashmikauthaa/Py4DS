# remove a character from a string-
# s=(input('enter the string: '))
# term=(input('what would u like to remove: '))

# res=''
# for i in s:
#     if i!=term:
#         res+=i

# print(res)



# check if a string is palindrome or not
# s=input('enter a string: ')
# flag=True
# for i in range(0,len(s)//2):
#     if s[i]!=s[len(s)-i-1]:
#         flag=False
#         print('not a palindrome')
#         break

# if flag:
#     print('Yea a palindrome')  



# count no. of words without split() fun
# s=input('enter a string: ')
# word=0
# for i in s:
#     if i==' ':
#         word+=1

# print(word)        



# print words in a string
# s=input('enter a string: ')
# temp=''
# list=[]
# for i in s:
#     if i!=' ':
#         temp=temp+i
#     else:
#         list.append(temp)
#         temp=''
# list.append(temp)
# print(list)        



# convert a string title to upper case without title()
# s=input('enter a string: ')
# L=[]
# for i in s.split():
#     L.append(i[0].upper()+i[1:].lower())

# print(" ".join(L))    