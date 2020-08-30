import pytesseract
import pandas as pd
from PIL import Image
import os

read_path = "I:/cache/年报/年报/09/"
names = ["北京市","涉县","磁县","阳城县","沈阳市","大连市","鞍山市","本溪市","哈尔滨道里区","哈尔滨南岗区","上海市","金坛市","苏州市","启东市","海门市","淮安市楚州区","建湖县","大丰市","扬中市","杭州市","嘉兴市","嘉善县","海宁市","马鞍山市","长乐市","临朐县","肥城市","林州市","武汉市","广州市","四会市","中山市","扶绥县","盐亭县",]

if __name__ == "__main__":
    os.chdir(read_path)
    csv_name_list = os.listdir()
    ll2 = []

    for i in range(len(csv_name_list)):
        # imagePath ="I:/cache/年报/年报/06/psReport_10.png"
        imagePath = read_path + csv_name_list[i]
        im = Image.open(imagePath)
        (x,y) = im.size
        a = 0.3
        b = 0.5
        box = (0, y*a, x, y*b)
        im = im.crop(box)
        # val = pytesseract.image_to_string(im, lang='eng',config= "-psm 6")
        val = pytesseract.image_to_string(im, lang='eng',
                                          config="--psm 4")

        l = val.split("Lung")
        print(val)
        if len(l) >= 2 :
            ll = l[1].split(" ")
            if len(ll) >= 4:
                ll2.append(ll[1:5])
            else:
                ll2.append("NAN")
        else:
            l = val.split("Bronchus")
            if len(l) >= 5:
                ll2.append(ll[2:6])
            else:
                ll2.append("NAN")

        # print(names[i])
        print(ll2[i])
    # df = pd.DataFrame(ll2)
    # df["city"] = names
    df.to_excel('./结果.xlsx')