import fnmatch
import os
import shutil



def is_file_match(filename, patterns):
    """
    判断文件是否符合判定条件 patterns
    :param filename: 目标检测文件名
    :param patterns: 文件对比条件
    :return: 返回判断结果 匹配成功返回True 匹配失败返回False
    """
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


def find_special_files(root, patterns=['*'], exclude_dirs=[],exclude_patterns=[], exclude_files=['.DS_Store', 'Thumbs.db']):
    """
    寻找特定文文件夹中各个符合筛选条件文件的路径
    :param root: 文件路径
    :param patterns: 文件类别
    :param exclude_dirs: 排除特定文件夹
    :param exclude_files: 排除特定文件
    :return: 返回文件夹中各个符合筛选条件文件的路径（迭代器）
    """
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if filename not in exclude_files:
                if is_file_match(filename, patterns):
                    yield os.path.join(root, filename)
        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)





if __name__ == '__main__':
    """
    root_path: txt所在的路径
    root_new_path: 要添加txt文件的路径
    txt_list: 根据条件筛选所获取root_path路径下所有文件的url
    txt_list_new_path: 根据条件筛选所获取root_new_path路径下所有文件的url

    
    """
    root_path = r"{}".format(input('txt文件的路径: '))
    root_new_path = r"{}".format(input('要复制的文件的路径: '))
    # root_path = r''
    # root_new_path = r'\\dtc-fs\SmartCar\DMS_Train\Rear_Seat_Detection_General\1_源文件\0613'
    txt_list = list(find_special_files(root_path, patterns=['*.txt'], exclude_dirs=[], exclude_patterns=[],exclude_files=['.DS_Store', 'Thumbs.db', '*_keyframe.txt']))
    txt_list_new_path = list(find_special_files(root_new_path, patterns=['*.mp4'], exclude_dirs=[], exclude_patterns=[],
                                       exclude_files=['.DS_Store', 'Thumbs.db', '*_keyframe.txt']))

    for item_path in txt_list_new_path:                                                 # 遍历txt_list_new_path获得单个文件和url
        print('item_path', item_path)
        item_new_path = os.path.basename(os.path.splitext(item_path)[0])                # 截取文件的url获取文件的名字
        print('item_new_path', item_new_path)
        new_txt_path = os.path.join(root_new_path, item_new_path + '.txt')              # 重新组成新的路径
        for item_txt in txt_list:                                                       # 遍历 txt_list 获取 root_path 路径下所有满足条件的文件
            print('item_txt', item_txt)
            shutil.copyfile(item_txt, new_txt_path)                                   
    print('文件复制完成')                                       