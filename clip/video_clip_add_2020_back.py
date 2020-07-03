import cv2
import fnmatch
import os

def read_frame_info(txt_path):
    txt_frame_dict = []
    with open(txt_path, 'r') as f:
        for line in f.readlines():
            if line != "\n" or line != "":
                row_start = line.split(' ')[0].replace('\n', '').replace('\t', '')
                if row_start != "":
                    start_frame = int(row_start)
                    end_frame = int(line.split(' ')[1].replace('\n', '').replace('\t', ''))
                    action_num = line.split(' ')[2].replace('\n', '').replace('\t', '')
                    txt_frame_dict.append([start_frame, end_frame, action_num])
                else:
                    txt_frame_dict = {}
            else:
                txt_frame_dict = {}
    # print(txt_frame_dict)
    return txt_frame_dict


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

face_dict= {"1":"angry", "2":"angry", "3":"angry", "4":"happy", "5":"happy", "6":"sad", "7":"surprise", }
def create_clip_info_dict(root):
    count = 0
    for item in find_special_files(root, patterns=['*.txt'], exclude_dirs=[], exclude_patterns=['*_keyframe.txt'],
                                   exclude_files=['.DS_Store']):
        item_info_dict = read_frame_info(item)
        if item_info_dict != {}:
            for frame_info in read_frame_info(item):
                target_row_path = item.replace('_txt', '').split('.')[0]
                print(target_row_path)
                print(frame_info)
                # """\\dtc-fs\SmartCar\DMS_Train\Face_Video_Train_Set\4_tobereviewed\0428\a1\0428_8\V_20200428_135338_ES1"""
                clip_name = os.path.join(os.path.dirname(target_row_path), face_dict[frame_info[2]], os.path.basename(target_row_path) + "_{}_{}.avi".format(frame_info[0], frame_info[1]))
                # clip_name = os.path.join(root, os.path.basename(target_row_path) + "_{}_{}.avi".format(frame_info[0], frame_info[1]))
                if not os.path.exists(os.path.dirname(clip_name)):
                    os.makedirs(os.path.dirname(clip_name))
                print(str(count), clip_name)
                count += 1
                # if os.path.exists(target_row_path+".mp4"):
                #     transform_avi(frame_info[0], frame_info[1], target_row_path+".mp4", clip_name)
                if os.path.exists(target_row_path+".mp4"):
                    if not os.path.exists(clip_name):
                        transform_avi(frame_info[0], frame_info[1], target_row_path+".mp4", clip_name)
    print(count)
    # print(clip_info_dict)


def get_info_from_v(cap):
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 获得总帧数
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # w, h
    print('frames',frames)
    print('fps',fps)
    print('size',size)
    # print('cap',cap)
    return frames, fps, size

def transform_avi(start_frame, end_frame, target_file_path, transformed_clip_path):
    cap = cv2.VideoCapture(target_file_path)
    print('cap',cap)
    print('target_file_path',target_file_path)
    print('transformed_clip_path',transformed_clip_path)
    frames, fps, size = get_info_from_v(cap)
    print("{}  w {}   h {}".format(target_file_path, size[0], size[1]))
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    videoWriter = cv2.VideoWriter(transformed_clip_path, apiPreference=0, fourcc=fourcc, fps=fps, frameSize=size)

    cap.set(cv2.CAP_PROP_POS_FRAMES,start_frame)  #设置要获取的帧号
    i = start_frame
    while i <= end_frame:
        success, img = cap.read()
        if success:
            videoWriter.write(img)
        else:
            continue
        i = i + 1

    # for i in range(frames):
    #     success, img = cap.read()
    #     print(i,'1')
    #     if success and i > end_frame :
    #         if i >= start_frame:
    #             videoWriter.write(img)
    #     else:
    #         break


if __name__ == '__main__':
    root = r"D:\555\001"

    # root = r"{}".format(input('视频路径：  '))

    create_clip_info_dict(root)

    print("转换结束")
    print()
    # input("按任意键关闭窗口")