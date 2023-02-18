import os
import cv2
import time
import numpy as np
from datetime import datetime
import pyautogui as pg
import pyscreenshot as ps
import pytesseract as pt


def test_screenshot():
    img = ps.grab(bbox = (0,0,300,300))
    return img


def get_screenshot():
    try:
        time.sleep(5)
        li = []

        pg.alert("Start, select two points diagonally but wait!\n(npress Esc for closing msg box)")


        time.sleep(2)
        pg.alert("Now!\n(npress Esc for closing msg box)")
        li.append(list(pg.position()))

        time.sleep(2)
        pg.alert("Now!\n(npress Esc for closing msg box)")
        li.append(list(pg.position()))
        time.sleep(2)
        pg.alert("Done!\n(press Esc for closing msg box)")

        img = ps.grab(bbox = (li[0][0],li[0][1],(li[0][0]+li[1][0]),(li[0][1]+li[1][1])))
        img.show()
        return img
    except:
        print("Coordinates not found")

def get_files(dir_path):
    res_a = []

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            res_a.append(path.replace(".png",""))
    return res_a
    
    # print(max(res_a))

def save_file(img,dir_path):
    now = str(datetime.now().time()).replace(":","_").replace(".","_")
    dt = str(datetime.now().date())

    file_name = "image" + dt + "_"+ now
    if(file_name in get_files(dir_path)):
        file_name += "_"
    
    path = dir_path + '\\' + file_name+ ".png"
    img.save(dir_path + '\\' + file_name+ ".png",dpi=(300,300))


    check = get_files(dir_path)
    if(file_name in check):
        print("Image Saved!")

    # return str(file_name)

def reading_img():

    time.sleep(2)
    li = get_files(dir_path)
    fiile = dir_path + "\/" + li[-1]

    img = cv2.imread(fiile+".png")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img,100,255,cv2.THRESH_BINARY)[1]


    cv2.imshow("",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows

    text = pt.image_to_string(img)
    print(text)

dir_path = r'C:\enter\yourpath\here'

def final_one():
    save_file(get_screenshot(),dir_path)
    reading_img()