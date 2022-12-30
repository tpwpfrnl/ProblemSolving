'''
A036 Pick out Numbers
Problem : https://www.codeground.org/practice
Date : 20221230
'''

T = int(input())
for i in range(T):
    N = int(input())
    numb = list(map(int, input().split()))
    xor = []
    for j in numb:
        if j not in xor:
            xor.append(j)
        else:
            xor.remove(j)
    ans = xor[0]
    for k in xor[1:]:
        ans = ans ^ k
    print("Case #%d" %(i + 1))
    print(ans)


# '''
# You should use the statndard input/output

# in order to receive a score properly.

# Do not use file input and output

# Please be very careful. 
# '''

# import sys

# '''
# 	The method below means that the program will read from input.txt, instead of standard(keyboard) input.
# 	To test your program, you may save input data in input.txt file,
# 	and call below method to read from the file when using open() method.
# 	You may remove the comment symbols(#) in the below statement and use it.
# 	But before submission, you must remove the open function or rewrite comment symbols(#).
# '''

# #inf = open('input.txt');
# inf = sys.stdin 

# T = inf.readline();

# for t in range(0, int(T)):
    
#     Answer=0;
    
# 	N = int(inf.readline();)
#     numb = list(map(int, inf.readline().split()))
#     xor = []
#     for j in numb:
#         if j not in xor:
#             xor.append(j)
#         else:
#             xor.remove(j)
#     Answer = xor[0]
#     for k in xor[1:]:
#         Answer = Answer ^ k
        
#     print('Case #%d' %(int(t)+1))    
#     print(Answer)
# inf.close()