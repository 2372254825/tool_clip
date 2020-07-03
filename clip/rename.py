import os


def file_name(outer_path):
        """
        :param outer_path: 要检测的路径
        :param folderlist: 获取路径下文件夹的名称
        :param
        :param

        :return:
        """
        folderlist = os.listdir(outer_path)                         #获取路径下文件夹的名称
        for folder in folderlist:
            inner_path = os.path.join(outer_path, folder)
            total_num_folder = len(folderlist)                      #文件夹的总数
            print("total have %d folders" % (total_num_folder))     #打印文件夹的个数

            filelist = os.listdir(inner_path)                       #路径下包含的子文件夹的名称
            print(folderlist)
            print(filelist)
            print(folder, 1)

            # for item in filelist:
            #     total_num_file = len(filelist)
            #     print(total_num_file)
            #     if item.endswith('.avi'):
            #         src = os.path.join(os.path.abspath(inner_path), item)
            #         print(str)
            #         dst = os.path.join(os.path.abspath(inner_path, str(folder)))
            #








if __name__ == '__main__':
    outer_path =r"\\dtc-fs\SmartCar\DMS_Train\Face_Video_Train_Set\7_had_commited\Face_Video_Train_Set_20200519"
    file_name(outer_path)







