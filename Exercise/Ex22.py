namelist={}

with open('nameslist.txt', 'r') as open_file:
    x = open_file.readlines()
    for name in x:
        if name in namelist:
            namelist[name] += 1
        else:
            namelist.update({name:1})


print(namelist)