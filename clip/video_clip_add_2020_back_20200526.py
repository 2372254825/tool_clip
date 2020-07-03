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
    print(filename, '1')
    print(pattern, '2')


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


#? face_dict= {"1":"Angry", "2":"Angry", "3":"Angry", "4":"Happy", "5":"Happy", "6":"Sad", "7":"Surprise", }
face_dict = {"1": "Happy", "2": "Happy", "3": "Sad", "4": "Angry", "5": "Angry", "6": "Angry", "7": "Surprise",
             "8": "Surprise", "9": "Nurture", "10": "Nurture", "11": "Nurture", "12": "Nurture", "13": "Nurture",
             "14": "Nurture", "15": "Nurture", "16": "Nurture", "17": "Nurture"}
face_Second = {"1": "微笑", "2": "咧嘴笑", "3": "嘴角向下", "4": "皱眉+耸鼻子", "5": "皱眉+耸鼻子+咬牙切齿", "6": "皱眉+紧抿嘴", "7": "抬眉+小张嘴",
               "8": "抬眉+大张嘴", "9": "嘟嘴", "10": "左撇嘴+右撇嘴", "11": "左撇嘴+右撇嘴", "12": "鼓嘴", "13": "小张嘴", "15": "抿嘴",
               "14": "口罩", "16": "抬眉", "17": "张嘴闭合牙齿", }


def create_clip_info_dict(root):
    count = 0
    for item in find_special_files(root, patterns=['*.txt'], exclude_dirs=[], exclude_patterns=['*_keyframe.txt'],
                                   exclude_files=['.DS_Store']):
        item_info_dict = read_frame_info(item)
        if item_info_dict != {}:
            for frame_info in read_frame_info(item):
                target_row_path = item.replace('_txt', '').split('.')[0]
                print(target_row_path, 'target_row_path')  # 原始视频名称
                print(frame_info, 'frame_info')  # txt里面的片段编号
                # """\\dtc-fs\SmartCar\DMS_Train\Face_Video_Train_Set\4_tobereviewed\0428\a1\0428_8\V_20200428_135338_ES1"""
                clip_name = os.path.join(os.path.dirname(target_row_path), face_dict[frame_info[2]],
                                         face_Second[frame_info[2]],
                                         os.path.basename(target_row_path) + "_{}_{}.avi".format(frame_info[0],
                                                                                                 frame_info[1]))
                print(clip_name, 'clip_name')  # 视频抽出后总的路径
                # clip_name = os.path.join(root, os.path.basename(target_row_path) + "_{}_{}.avi".format(frame_info[0], frame_info[1]))
                if not os.path.exists(os.path.dirname(clip_name)):
                    os.makedirs(os.path.dirname(clip_name))
                print(str(count), clip_name)
                count += 1
                # if os.path.exists(target_row_path+".mp4"):
                #     transform_avi(frame_info[0], frame_info[1], target_row_path+".mp4", clip_name)
                if os.path.exists(target_row_path + ".mp4"):
                    if not os.path.exists(clip_name):
                        transform_avi(frame_info[0], frame_info[1], target_row_path + ".mp4", clip_name)
    print(count)
    # print(clip_info_dict)


def get_info_from_v(cap):
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 获得总帧数
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # w, h

    return frames, fps, size


def transform_avi(start_frame, end_frame, target_file_path, transformed_clip_path):
    cap = cv2.VideoCapture(target_file_path)
    frames, fps, size = get_info_from_v(cap)
    print("{}  w {}   h {}".format(target_file_path, size[0], size[1]))
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    videoWriter = cv2.VideoWriter(transformed_clip_path, fourcc=fourcc, fps=fps, frameSize=size)
    # cv2.namedWindow("Image")
    # cap.set(cv2.CAP_PROP_POS_FRAMES,start_frame)  #设置要获取的帧号
    # i = start_frame
    # while i <= end_frame:
    #     success, img = cap.read()
    #     if success:
    #         videoWriter.write(img)
    #     else:
    #         continue
    #     i = i + 1

    # # Read until video is completed
    # count = 0
    # while (cap.isOpened()):
    #     # Capture frame-by-frame
    #     ret, frame = cap.read()
    #     count += 1
    #     print(count)
    #     if ret == True:
    #
    #         # Display the resulting frame
    #         # cv2.imshow('Frame', frame)
    #
    #         if count <= end_frame:
    #             if count >= start_frame:
    #                 # cv2.imshow('Frame', frame)
    #                 videoWriter.write(frame)
    #                 # cv2.waitKey(0)
    #         else:
    #             break
    #
    #         # Press Q on keyboard to  exit
    #         # if cv2.waitKey(25) & 0xFF == ord('q'):
    #         #     # When everything done, release the video capture object
    #         #     cap.release()
    #         #
    #         #     # Closes all the frames
    #         #     cv2.destroyAllWindows()
    #         #     break
    #
    #     # Break the loop
    #     else:
    #         # When everything done, release the video capture object
    #         cap.release()
    #
    #         # Closes all the frames
    #         cv2.destroyAllWindows()
    #         break

    # print("{} {}".format(frames, target_file_path))
    for i in range(frames):
        success, img = cap.read()
        # print(success, i)
        if success:
            if i <= end_frame:
                if i >= start_frame:
                    # cv2.imshow("Image", img)
                    videoWriter.write(img)
                    # cv2.waitKey(0)
            else:
                # cv2.destroyAllWindows()
                cap.release()
                break
        else:
            with open("write_error.txt", 'a', encoding='utf8') as f:
                f.write(target_file_path)
                f.write("\n")
            # cv2.destroyAllWindows()
            cap.release()
            break


if __name__ == '__main__':
    root = r"\\dtc-fs\SmartCar\DMS_Test\Face_Video_Test_Set\1_raw_data\0526\B4"

    # root = r"{}".format(input('视频路径：  '))

    create_clip_info_dict(root)

    print("转换结束")
    print()
    # input("按任意键关闭窗口")
