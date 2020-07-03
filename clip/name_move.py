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



if __name__ == "__main__":
    root = r"\\dtc-fs\SmartCar\DMS_Train\Rear_Seat_Body_Detection_Taxi\8_cal_child\RS_Train_2020_0409_0506_20200526\202004_02_03\child\002"
    root_new = r"\\dtc-fs\SmartCar\DMS_Train\Rear_Seat_Body_Detection_Taxi\8_cal_child\RS_Train_2020_0409_0506_20200526\202004_02_03\child\002"
    txt_list = list(find_special_files(root, patterns=["*.txt"], exclude_dirs=[], exclude_patterns=[], exclude_files=['.DS_Store', 'Thumbs.db']))
    jpg_list = list(find_special_files(root, patterns=["*.jpg"], exclude_dirs=[], exclude_patterns=[], exclude_files=['.DS_Store', 'Thumbs.db']))
    for txt_name in txt_list: 
        txt = os.path.basename(os.path.splitext(txt_name)[0])
        for jpg_name in jpg_list:
            if os.path.basename(os.path.splitext(txt_name)[0]) == os.path.basename(os.path.splitext(jpg_name)[0]):
                new_path = os.path.join(os.path.split(txt_name)[0] + "\\" + txt.split('_')[0] + '_'+ txt.split('_')[1] +'_'+ txt.split('_')[2])
                print(txt_name)
                if not os.path.exists(new_path):
                    os.makedirs(new_path)   
                shutil.move(txt_name, os.path.join(os.path.split(txt_name)[0] + "\\" + txt.split('_')[0] + '_'+ txt.split('_')[1] +'_'+ txt.split('_')[2]))    
    print('同名文件移动结束')            


#移动同名文件