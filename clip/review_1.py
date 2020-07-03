import fnmatch
import os



def is_file_match(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


def find_special_files(root, patterns=['*'], exclude_dirs=[], exclude_patterns=[], exclude_files=['.DS_Store']):
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if filename not in exclude_files:
                if is_file_match(filename, patterns):
                    if is_file_match(filename, exclude_patterns) == False:
                        yield os.path.join(root, filename)
        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)


if __name__ == '__main__':
    root = r"\\dtc-fs\SmartCar\DMS_Train\Face_Video_Train_Set\7_had_commited\Face_Video_Train_Set_20200523"
    content = []
    for item in find_special_files(root ,  patterns=['*.txt'], exclude_dirs=[], exclude_patterns=["*_keyframe.txt"], exclude_files=['.DS_Store', "item.txt"]):
        print(item)
        with open(item , 'r', encoding='utf8') as f:
            for line in f.readlines():
                line = line.replace("\n", "").replace("\t", "")
                if not line == "":
                    # print(line)
                    # print(int(line.split(" ")[2]))
                    print(line)
                    print(line.split(" "))
                    if int(line.split(" ")[2]) > 7:
                        if item not in content:
                            print(item)
                            content.append(item)

    with open("item.txt", "w", encoding="utf8") as f:
        for item in content:
            f.write(item)
            f.write("\n")
