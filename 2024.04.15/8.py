inp_list = input().split('; ')
i = 0


while i < len(inp_list):
    n = 1
    
    for k in range(i+1, len(inp_list)):
        if inp_list[i] == inp_list[k]:
            # breakpoint()
            inp_list[k] = ''.join(inp_list[k].partition('.')[0] + '_' + str(n) + '.' + inp_list[k].partition('.')[2])
            n += 1
    i += 1
   
inp_list = sorted(inp_list)
for elem in inp_list:
    print(elem)

# Пример вывода

# 2.py; 2.py; 2.py; 1.re; 1.exe; 1.exe; 1.exe; abc.exe.org; abc.exe.org; abc.exe; bac.py; caz.py

# 1.exe
# 1.re
# 1_1.exe
# 1_2.exe
# 2.py
# 2_1.py
# 2_2.py
# abc.exe
# abc.exe.org
# abc_1.exe.org
# bac.py
# caz.py
