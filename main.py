
import sys

num1 = list(map(int, input("Enter the subset: ").split()))
num2 = list(map(int, input("Enter the primary set: ").split()))

if len(num1) > len(num2):
	print ('False')
	sys.exit(0)
# ******************************
# Make your Code
# ******************************
count = 0
for i in range(len(num2) - len(num1) + 1): 
   for j in range(len(num1)):
      if num1[j] == num2[i+j]:
         count = count + 1
if count == 3:
	print('True')
else:
	print('False')		
# print ('True') or ('False')
