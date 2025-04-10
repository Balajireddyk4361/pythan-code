# for file handling as four key words are there 
# 1)try        =>raising code
#  2) expect   =>handling code
#  3)finally   =>mandatory code
# 4) raise     =>For handling custom Eror




# a=int(input('Enter first number ::'))
# b=int(input('Enter second number ::'))

# # print(a/b)
# # print('gm')

# try:
#     print(a/b)
# except ZeroDivisionError as Err:
#     print(a/1)
    
# print('hi balaji')


try:
    a=int(input('Enter First Number ::'))
    b=int(input('Enter second Number ::'))
    print(a/b)

    fp=open('abc.txt','r')
    print(fp.read())
except ZeroDivisionError as Err:
    print(a/1)
print('Hello balaji reddy')
