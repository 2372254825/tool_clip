import os
import fnmatch
import shutil


def is_file_match(filename, patterns):
    for pattern in patterns:
        print(pattern)
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


def find_special_files(root, patterns=['*'], exclude_dirs=[], exclude_patterns=[], exclude_files=['.DS_Store', 'Thumbs.db']):
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            print(filename)
            if filename not in exclude_files:
                if is_file_match(filename, patterns):
                    if is_file_match(filename, exclude_patterns) == False:
                        yield os.path.join(root, filename)
        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)


def get_files(root, name_txt):
    for item in find_special_files(root, patterns=['*.txt'], exclude_dirs=[], exclude_patterns=[],
                                       exclude_files=['.DS_Store', 'Thumbs.db', '*_keyframe.txt']):
        with open(item, 'r') as open_item:
            open_item_txt = open_item.read()
            print('open_item_txt', open_item_txt)
            # print('name_txt', name_txt)
            if name_txt in open_item_txt:
                des_path = input_path + "\\"+ name_txt
                print('des_path', des_path)
                if not os.path.exists(des_path):
                    os.makedirs(des_path)
                open_item.close()
                shutil.move(item, des_path)   
            else:
                continue


if __name__ == '__main__':
    # root = r'{}'.format(input('请输入文件位置:'))
    # name_txt = r"{}".format(input('属性名称:'))
    root = r"\\dtc-fs\SmartCar\DMS_Train\Rear_Seat_Body_Detection_Taxi\8_cal_child\RS_Train_2020_0409_0506_20200602\202004_02_03"
    name_txt = r"child"
    input_path = root
    get_files(root, name_txt)



#根据输入的属性名称查找相同属性的txt文件并移动到同一文件夹


