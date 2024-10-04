import requests
import re
import os
from bs4 import BeautifulSoup

PIC_PATH = "pic_files"


def picture_download(url, pic_name):
    r = requests.get(url)

    pic_name = pic_name + '.jpg'
    if not os.path.exists(PIC_PATH):
        os.makedirs(PIC_PATH)
    pic_path = os.path.join(PIC_PATH, pic_name)
    with open(pic_path, 'wb') as f:
        f.write(r.content)


def run():
    res = requests.get(url="https://s.10010.com/bj/mobilelist-0-0-0-0-0-0-0-603-0-0-0/")
    data = res.content.decode('utf-8')

    soup_object = BeautifulSoup(data, "html.parser")

    new_area_object = soup_object.find(name='ul', attrs={"class": "goodsListInfor"})

    li_area_object_list = new_area_object.find_all(name='li', attrs={"class": "goodsLi"})

    file_object = open("db.txt", "a", encoding="utf-8")

    for li_object in li_area_object_list:
        name = li_object.find(name='a', attrs={"class": "name"}).text
        price = li_object.find(name='label', attrs={"class": "priceD"}).text
        price_number = int(re.findall(r"￥(\d+)", price)[0])
        comment = li_object.find(name='p', attrs={"class": "evalNum"}).text
        comment_number = int(re.findall(r"已有(\d+)人评价", comment)[0])
        img_url = li_object.find(name='img').attrs["data-original"]
        print("商品名：{}\n价格：{}\n评论数：{}\n图片：{}".format(name, price_number, comment_number, img_url))
        print("====================")

        file_object.write("{} | {} | {} | {} \n".format(name, price_number, comment_number, img_url))
        picture_download(img_url, name)

    file_object.close()

if __name__ == '__main__':
    run()