import os
def get_files(path):
    file_lists = []
    for home,dirs,files in os.walk(path):
        for file in files:
            if file.endswith('.avi'or '.mp4'):
                # file_lists.append(os.path.join(home,file))
                src_file = os.path.join(home,file)
                if '_Rotated' in src_file:
                    print(src_file, "src_file")
                    remove_ = '_'+src_file.split('_')[-1]
                    print(remove_, "remove_")
                    rename_file = src_file.replace(remove_,'.avi')
                    print(rename_file, "rename_file")
                    if os.path.isfile(rename_file):
                        os.remove(rename_file)
                        print('exit')
                    os.rename(src_file,rename_file)
    return file_lists

if __name__ == '__main__':
    # path = r'D:\h_ruan\junxi\5.28\test'
    path = input('请输入文件位置：')
    files = get_files(path)
    # os.system('pause')
