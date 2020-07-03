import os,shutil                                            #导入模块
def copy_files():                                           #定义函数名称
    for foldName, subfolders, filenames in os.walk(path):     #用os.walk方法取得path路径下的文件夹路径，子文件夹名，所有文件名
           for filename in filenames:                         #遍历列表下的所有文件名
                if filename.endswith('.txt'):                #当文件名以.txt后缀结尾时
                        new_name=filename.replace('.txt','_new.txt')               #为文件赋予新名字
                        shutil.copyfile(os.path.join(foldName,filename), os.path.join(path2,new_name))    #复制到新路径下，并重命名文件
                        print(filename,"copied as",new_name)           #输出提示

if __name__ == '__main__':
        path = r''   #运行程序前，记得修改主文件夹路径！
        path2 =r''  #存放文件的新路径，不要放在原路径下，不然会多复制两份
        copy_files()         #调用定义的函数，注意名称与定义的函数名一致
