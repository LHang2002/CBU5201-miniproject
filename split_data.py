import os
import shutil
import random

def split_into_two():
    # 设置数据文件夹路径
    data_folder = "genki4k/files(preprocess)"

    # 创建输出文件夹
    os.makedirs("genki4k/files(splitdata)/smile", exist_ok=True)
    os.makedirs("genki4k/files(splitdata)/unsmile", exist_ok=True)

    # 获取数据文件夹下的所有文件
    files = os.listdir(data_folder)

    # 将前2125个数据放入smile文件夹下，其他的放入unsmile文件夹下
    for i, file in enumerate(files):
        if i < 2125:
            shutil.copy(os.path.join(data_folder, file), "genki4k/files(splitdata)/smile")
        else:
            shutil.copy(os.path.join(data_folder, file), "genki4k/files(splitdata)/unsmile")
    
    print("split into smile or unsmile done!")

def split_into_three():
    # 指定拆分比例
    split_ratio = [0.6, 0.2, 0.2]

    # 创建输出文件夹
    output_folder = ["genki4k/files(splitdata)/train", "genki4k/files(splitdata)/test", "genki4k/files(splitdata)/val"]
    for folder in output_folder:
        os.makedirs(os.path.join(folder, "smile"), exist_ok=True)
        os.makedirs(os.path.join(folder, "unsmile"), exist_ok=True)

    # 拆分 smile 文件夹
    smile_files = os.listdir("genki4k/files(splitdata)/smile")
    random.shuffle(smile_files)
    total_smile_files = len(smile_files)
    split_index_smile = [int(total_smile_files * split_ratio[0]), int(total_smile_files * (split_ratio[0] + split_ratio[1]))]

    for i, file in enumerate(smile_files):
        if i < split_index_smile[0]:
            shutil.copy(os.path.join("genki4k/files(splitdata)/smile", file), os.path.join("genki4k/files(splitdata)/train", "smile", file))
        elif i < split_index_smile[1]:
            shutil.copy(os.path.join("genki4k/files(splitdata)/smile", file), os.path.join("genki4k/files(splitdata)/test", "smile", file))
        else:
            shutil.copy(os.path.join("genki4k/files(splitdata)/smile", file), os.path.join("genki4k/files(splitdata)/val", "smile", file))

    # 拆分 unsmile 文件夹
    unsmile_files = os.listdir("genki4k/files(splitdata)/unsmile")
    random.shuffle(unsmile_files)
    total_unsmile_files = len(unsmile_files)
    split_index_unsmile = [int(total_unsmile_files * split_ratio[0]), int(total_unsmile_files * (split_ratio[0] + split_ratio[1]))]

    for i, file in enumerate(unsmile_files):
        if i < split_index_unsmile[0]:
            shutil.copy(os.path.join("genki4k/files(splitdata)/unsmile", file), os.path.join("genki4k/files(splitdata)/train", "unsmile", file))
        elif i < split_index_unsmile[1]:
            shutil.copy(os.path.join("genki4k/files(splitdata)/unsmile", file), os.path.join("genki4k/files(splitdata)/test", "unsmile", file))
        else:
            shutil.copy(os.path.join("genki4k/files(splitdata)/unsmile", file), os.path.join("genki4k/files(splitdata)/val", "unsmile", file))

    print("split into train,test or val done!")

if __name__ == "__main__":
    split_into_two()
    split_into_three()