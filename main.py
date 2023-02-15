# f = open('test.txt', 'r')
# print(f.readlines())
# f.close()

# with open('test.txt','r') as f:
#   f_contents = f.readlines()
#   print(f_contents, end ="")

# employee_file = open('employees.txt', "r")
# for employee in employee_file.readlines():
#   print(employee)
# employee_file.close()
# this overwrites the original content
with open('readme.txt', 'w') as f:
  f.write('writeme')

#this adds to the original content
with open('readme.txt', 'a') as f:
  f.write("I don't care 3xxx")

with open('newfile.txt', 'a') as f:
  f.write("challenge")