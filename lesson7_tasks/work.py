ddir = 'D:\\GVV_Viseven\\ITHUB\\lesson7_tasks\\'
file1 = open(ddir+'user_info.txt','r+')

data = file1.read()
#a = exec(data)
mod = 35
print(mod, file = file1)

#lst = ['First\n', 'Second\n']
#file1.writelines(lst)
#file1.seek(10)
#aaaa = file1.tell()
file1.write(input())
file1.close()