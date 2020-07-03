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


if __name__ == '__main__':
    # old_path = input("文件所在的路径:")
    # root_path = r"C:\Output"
    root_path = r"{}".format(input("视频旋转后的路径: "))
    root_new_path = r"{}".format(input("被替换的视频的路径: "))
    # root_new_path = r"\\dtc-fs\SmartCar\DMS_Test\Face_Video_Test_Set\1_raw_data\0526\A1\003"
    txt_list = list(find_special_files(root_path, patterns=['*.avi'], exclude_dirs=[], exclude_patterns=[],exclude_files=['.DS_Store', 'Thumbs.db', '*_keyframe.txt']))
    txt_list_new_path = list(find_special_files(root_new_path, patterns=['*.avi'], exclude_dirs=[], exclude_patterns=[],
                                       exclude_files=['.DS_Store', 'Thumbs.db', '*_keyframe.txt']))

    for item_path in txt_list_new_path:
        print("item_path", item_path)
        item_new_path = os.path.basename(os.path.splitext(item_path)[0])
        print("item_new_path", item_new_path)
        for item in txt_list:
            print('item', item)
            item_root = os.path.basename(os.path.splitext(item)[0])
            print("item_root", item_root)
            if item_root.find(item_new_path, 0, len(item_root)-1) == 0:
                shutil.move(item, item_path)
    print("移动结束")


