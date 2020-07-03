import os, re, sys

print('please input the path')
Searchpath = input()
list = os.listdir(Searchpath)
os.chdir(Searchpath)
print('请输入文件类型，如 \'.txt\'')
type = input()
print(list)
for filename in list:
    # print(filename)
    Allsuffix = os.path.splitext(filename)
    file, suffix = Allsuffix
    # print(suffix)
    for root, dirs, files in os.walk(Searchpath, topdown=False):
        # print(root, '1')
        # print(dirs, '2')
        # print(files, '3')
        for dir in dirs:                    # dir  获取最后一级文件的名字
            mulu = root + '\\' + dir        # mulu为组合后的最后一级文件路径
            # os.chdir(mulu)                 #改变目录，不改变到文件所在目录的话，无法给文件重新命名
            files = os.listdir(mulu)
            if suffix == str(type):
                print(filename, 1)
                file = open(filename)
                data = file.read()
                print(data)

        print('**********input the re rule*********')
        ReRule = input()
        regex = re.compile(r'' + ReRule + '')
        # redata = regex.findall(data)

        # print(redata)
        print('----------------------------')
        file.close()