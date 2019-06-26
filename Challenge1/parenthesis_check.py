#Problem Statement: Given a combination of any of these three types of paranthesis as inputs: (){}[]
# Write a program to make sure that the expression entered is balanced i.e number of closing paranthesis 
# is equal to the number of opening parenthesis and the parenthesis are in the right order ( opening ones before the closing ones)
# Blank strings are also valid strings

def solution(input):
    str = list(input)
    arr = []
    if(input == ''):
        return True;
    for i in range(0, len(str)):
        if(str[i] == '(' or str[i] == '{' or str[i] == '['):
            arr.append(str[i])
            print("Array after adding is:",arr)
            continue
        elif(len(arr) == 0):
            return False
        elif(str[i] == ')'):
            top = arr[-1]
            arr.pop()
            print("Array after popping is:",arr)
            if(top == '{' or top == '['):
                return False
            else:
                continue
        elif(str[i] == '}'):
            top = arr[-1]
            arr.pop()
            print("Array after popping is:",arr)
            if(top == '(' or top == '['):
                return False
            else:
                continue
        elif(str[i] == ']'):
            top = arr[-1]
            arr.pop()
            if(top == '(' or top == '{'):
                return False
            else:
                continue
        else:
             continue
    if(len(arr) == 0):
        return True
    else:
        return False

str = input()
print(solution(str))
