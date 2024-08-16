# # # Ex1
# text = 'sina neak'
# for i in range (len(text)):
#     print (text[i])
# # Ex2
# text = 'sina neak'
# for i in range (len(text)):
#     print(i)

 # EX3
# text = input("Enter text: ")
# contains_capital = False
# for char in text:
#     if char.isupper():
#         contains_capital = True
# if contains_capital:
#     print("Yes")
# else:
    # print("No")


# # ex4

# text = "3 4 5 6"
# new_text = ""
# sum = 0 
# for char in text:
#     if char != ' ':
#         new_text += char
#         sum += int(char)
# print(new_text)
# print(sum)

    



# # Q1 : 
 
# text = '454639'
# countOdd = 0 
# countEven = 0 
# for char in range (len(text)):
#      if char % 2 == 0:
#           countOdd += 1
#      else:
           
#           countEven += 1
# print('Odd number is =',countOdd)
# print('Even number is =',countEven)
 
      
 
# # # # Q2
# text = "454639"
# sum = 0 
# for char in text:
#     if char != ' ':
#         sum += int(char)
# print('Sum all number ',sum)       
 

        
 
    
 

# # Q3
# text = '454639'
# sum = 0 
# for char in text:
#      if int(char) % 2 == 0:
#         sum += int(char)
# print('only even number is ',sum)

 
 
# # Q4
# text = "454639"
# reversed_text = text[::-1]
# print(
# reversed_text)

 

# # Ex6
# num = int(input('enter your number : '))
# if num % 2 == 1:
#     print('odd ')
# else:
#     print('Even')

# Ex7
# isFoundNum = False
# while not isFoundNum:
#      number =  int (input('Enter your number: '))
#      if number == 10 and number <= 20:
#         isFoundNum = True
#      else:
#        print('Number ot of range')
# print('countinue')         

# # ex8
# # Q1
# num = "9394884039"
# count_8 = 0 
# for char in range (len(num)):
#     if num[char] == '8':
#         count_8 += 1
# print(count_8)
# #  Q2
# num = "9394884039"
# isFound_First = False
# i = 0 
# while not isFound_First:
#      if num[i] == '8':
#         isFound_First = True
#         print(i)
#      i += 1


 
# # Ex9

# string = "3 4 5 6"
# text = ''
# for char in string:
#     if char != ' ':
#         text += char
# print(text)

# # Q2 
# num = input('enter your text of num: ')
# for i  in range (6, 14, 2 ):
#     print(i,end=' ')


  
# # ex9
num = int(input("Enter a number: "))
max_value = num
min_value = num
for  char in range(4):
    num = int(input("Enter a number: "))
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print("Max =", max_value)
print("Min =", min_value)

 

 

