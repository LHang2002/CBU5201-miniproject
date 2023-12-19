import os
import shutil
import random

def split_into_three():
    # 指定拆分比例
    split_ratio = [0.6, 0.2, 0.2]

    # 创建输出文件夹
    output_folder = ["genki4k/files(gender&color)/train", "genki4k/files(gender&color)/test", "genki4k/files(gender&color)/val"]
    for folder in output_folder:
        os.makedirs(os.path.join(folder, "man_b"), exist_ok=True)
        os.makedirs(os.path.join(folder, "man_w"), exist_ok=True)
        os.makedirs(os.path.join(folder, "man_y"), exist_ok=True)
        os.makedirs(os.path.join(folder, "woman_w"), exist_ok=True)
        os.makedirs(os.path.join(folder, "woman_b"), exist_ok=True)
        os.makedirs(os.path.join(folder, "woman_y"), exist_ok=True)

    # 拆分 man_b 文件夹
    man_b_files = os.listdir("genki4k/files(gender&color)/man_b")
    random.shuffle(man_b_files)
    total_man_b_files = len(man_b_files)
    split_index_man_b = [int(total_man_b_files * split_ratio[0]), int(total_man_b_files * (split_ratio[0] + split_ratio[1]))]

    for i, file in enumerate(man_b_files):
        if i < split_index_man_b[0]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/man_b", file), os.path.join("genki4k/files(gender&color)/train", "man_b", file))
        elif i < split_index_man_b[1]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/man_b", file), os.path.join("genki4k/files(gender&color)/test", "man_b", file))
        else:
            shutil.copy(os.path.join("genki4k/files(gender&color)/man_b", file), os.path.join("genki4k/files(gender&color)/val", "man_b", file))

    # 拆分 man_w 文件夹
    man_w_files = os.listdir("genki4k/files(gender&color)/man_w")
    random.shuffle(man_w_files)
    total_man_w_files = len(man_w_files)
    split_index_man_w = [int(total_man_w_files * split_ratio[0]), int(total_man_w_files * (split_ratio[0] + split_ratio[1]))]

    for i, file in enumerate(man_w_files):
        if i < split_index_man_w[0]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/man_w", file), os.path.join("genki4k/files(gender&color)/train", "man_w", file))
        elif i < split_index_man_w[1]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/man_w", file), os.path.join("genki4k/files(gender&color)/test", "man_w", file))
        else:
            shutil.copy(os.path.join("genki4k/files(gender&color)/man_w", file), os.path.join("genki4k/files(gender&color)/val", "man_w", file))

    # 拆分 man_y 文件夹
    man_y_files = os.listdir("genki4k/files(gender&color)/man_y")
    random.shuffle(man_y_files)
    total_man_y_files = len(man_y_files)
    split_index_man_y = [int(total_man_y_files * split_ratio[0]), int(total_man_y_files * (split_ratio[0] + split_ratio[1]))]

    for i, file in enumerate(man_y_files):
        if i < split_index_man_y[0]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/man_y", file), os.path.join("genki4k/files(gender&color)/train", "man_y", file))
        elif i < split_index_man_y[1]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/man_y", file), os.path.join("genki4k/files(gender&color)/test", "man_y", file))
        else:
            shutil.copy(os.path.join("genki4k/files(gender&color)/man_y", file), os.path.join("genki4k/files(gender&color)/val", "man_y", file))

    # 拆分 woman_b 文件夹
    woman_b_files = os.listdir("genki4k/files(gender&color)/woman_b")
    random.shuffle(woman_b_files)
    total_woman_b_files = len(woman_b_files)
    split_index_woman_b = [int(total_woman_b_files * split_ratio[0]), int(total_woman_b_files * (split_ratio[0] + split_ratio[1]))]

    for i, file in enumerate(woman_b_files):
        if i < split_index_woman_b[0]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/woman_b", file), os.path.join("genki4k/files(gender&color)/train", "woman_b", file))
        elif i < split_index_woman_b[1]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/woman_b", file), os.path.join("genki4k/files(gender&color)/test", "woman_b", file))
        else:
            shutil.copy(os.path.join("genki4k/files(gender&color)/woman_b", file), os.path.join("genki4k/files(gender&color)/val", "woman_b", file))

    # 拆分 woman_w 文件夹
    woman_w_files = os.listdir("genki4k/files(gender&color)/woman_w")
    random.shuffle(woman_w_files)
    total_woman_w_files = len(woman_w_files)
    split_index_woman_w = [int(total_woman_w_files * split_ratio[0]), int(total_woman_w_files * (split_ratio[0] + split_ratio[1]))]

    for i, file in enumerate(woman_w_files):
        if i < split_index_woman_w[0]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/woman_w", file), os.path.join("genki4k/files(gender&color)/train", "woman_w", file))
        elif i < split_index_woman_w[1]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/woman_w", file), os.path.join("genki4k/files(gender&color)/test", "woman_w", file))
        else:
            shutil.copy(os.path.join("genki4k/files(gender&color)/woman_w", file), os.path.join("genki4k/files(gender&color)/val", "woman_w", file))

    # 拆分 woman_y 文件夹
    woman_y_files = os.listdir("genki4k/files(gender&color)/woman_y")
    random.shuffle(woman_y_files)
    total_woman_y_files = len(woman_y_files)
    split_index_woman_y = [int(total_woman_y_files * split_ratio[0]), int(total_woman_y_files * (split_ratio[0] + split_ratio[1]))]

    for i, file in enumerate(woman_y_files):
        if i < split_index_woman_y[0]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/woman_y", file), os.path.join("genki4k/files(gender&color)/train", "woman_y", file))
        elif i < split_index_woman_y[1]:
            shutil.copy(os.path.join("genki4k/files(gender&color)/woman_y", file), os.path.join("genki4k/files(gender&color)/test", "woman_y", file))
        else:
            shutil.copy(os.path.join("genki4k/files(gender&color)/woman_y", file), os.path.join("genki4k/files(gender&color)/val", "woman_y", file))
    
    print("split into train,test or val done!")

if __name__ == "__main__":
    split_into_three()