# -*- coding:utf-8 -*-
import os
import sys
import time
import datetime
import shutil

def renamePocket2(path):

    for file in os.listdir(path):
        file_full_path = os.path.join(path,file)
        raw_file_cTime = os.path.getmtime(file_full_path)
        file_cTime = datetime.datetime.fromtimestamp(raw_file_cTime)


        if os.path.isdir(file_full_path):
            continue
        name = "DJI_"
        name += str(file_cTime.date())
        name += "_"
        name += str(file_cTime.time().hour)
        name += "_"
        name += str(file_cTime.time().minute)
        name += "_"
        name += str(file_cTime.time().second)
        name = name.replace("-","_")
        name += "."
        name += file.split(".")[1]
        # name += str(file[-4:])
        # print(file.split(".")[1])
        # print(name)


        os.rename(file_full_path,os.path.join(path,name))


def createDir(path):
    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir(path)
        # print("create success! %s"%path)
        return path
    else:
        # print("Existed!")
        return -1

def combineDir(path):
    for file in os.listdir(path):
        file_full_path = os.path.join(path,file)
        raw_file_cTime = os.path.getmtime(file_full_path)
        file_cTime = datetime.datetime.fromtimestamp(raw_file_cTime)
        if os.path.isdir(file_full_path):
            continue
        dirName = createDir(os.path.join(path,str(file_cTime.date())))
        shutil.move(file_full_path, os.path.join(path, str(file_cTime.date())))

if __name__ == "__main__":
    path = r"D:\2021_9_27_backup"
    renamePocket2(path)
    print("----------Rename Success------------")
    print("----------Combine The Video------------")

    combineDir(path)
    print("----------Success Combine------------")

    # print("start")
    # print(os.listdir(path))

#print(datetime.datetime.fromtimestamp(os.path.getmtime(f)))
#print(datetime.datetime.fromtimestamp(os.path.getctime(f)))