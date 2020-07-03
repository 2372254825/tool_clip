import fnmatch
import os



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


def find_special_files(root, patterns=['*'], exclude_dirs=[], exclude_files=['.DS_Store', 'Thumbs.db']):
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

if __name__ == "__main__":
    root = r"\\dtc-fs\SmartCar\DMS_Test\Face_Video_Test_Set\1_raw_data\0526"
    txt_list = list(find_special_files(root,  patterns=['*.txt'], exclude_dirs=[], exclude_files=['.DS_Store', 'Thumbs.db','*_keyframe.txt']))
    print(txt_list,'1')
    avi_list = [os.path.splitext(os.path.basename(item))[0] for item in find_special_files(root,  patterns=['*.avi'], exclude_dirs=[], exclude_files=['.DS_Store', 'Thumbs.db','*_keyframe.txt'])]
    clip_list = []
    for txt in txt_list:
        print(txt, '2')
        with open(txt, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                print("---", line.split(' '))
                if line != '\n':
                    clip_start = line.split(' ')[0]
                    clip_end = line.split(' ')[1]
                    clip_name = os.path.splitext(os.path.basename(txt))[0] + "_{}_{}".format(clip_start, clip_end)
                    print(clip_name)
                    clip_list.append(clip_name)
    with open("clip_list.txt", 'w', encoding='utf-8') as f:
        for line in clip_list:
            f.write("{}\n".format(line))
    print(" 在 avilist  不在 clip list")
    print([x for x in avi_list if x not in clip_list])
    with open("存在AVI不存在TXT_01.txt", 'w', encoding='utf-8') as f:
        for line in [x for x in avi_list if x not in clip_list]:
            f.write("{}\n".format(line))

    print(" 在 clip list  不在 avi list")
    print([y for y in clip_list if y not in avi_list])
    with open("不存在AVI存在TXT_02.txt", 'w', encoding='utf-8') as f:
        for line in [y for y in clip_list if y not in avi_list]:
            f.write("{}\n".format(line))
