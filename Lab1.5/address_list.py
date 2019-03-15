import glob

PATTERN = 'ip address'

file_list = glob.glob('config_files\*')
address_list=[]

for filename in file_list:
    #print(filename)
    with open(filename, 'r') as file:
        for line in file:
            if line.find(PATTERN) != -1:
                address_list.append(line.strip())
                #print(line)

list1 = list(set(address_list))
list2 = []
for line in list1:
    if line.find(PATTERN) == 0:
        if line[11] in "0123456789":
            list2.append(line)

display_list = list2

for line in display_list:
    print(line)

