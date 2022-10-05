import json
import os
import requests
from bs4 import BeautifulSoup
import time
import cv2

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.114 YaBrowser/22.9.1.1095 Yowser/2.5 Safari/537.36"
}
def save_img(img_data,img_type,img_number):
    with open(f'images/{img_type}/{str(img_number).zfill(4)}.jpg','wb') as file:
                file.write(img_data)

def resave_img(img_data,img_type,img_number):
    for img_data in img_datas:
        os.makedirs('dataset1/{img_data}')
        os.makedirs('dataset1/{img_data}')
    for i in range(1,1020):
        img=cv2.imread(f'dataset/{name}/{str(i).zfill(4)}.jpg')
        cv2.imwrite(f'dataset1/{name}/{str(i).zfill(4)}.jpg', img)

def create_file(img_type):
    if not os.path.exists(f'images/{img_type}'):
        os.makedirs(f'images/{img_type}')

def search_images(img_type):
    create_file(img_type)
    page_number=0
    img_number=1
    while True:
        url=f'https://yandex.ru/images/search?p={page_number}&text={img_type}&uinfo=sw-1536-sh-864-ww-760-wh-754-pd-1.25-wp-16x9_1920x1080&lr=51&rpt=image'
        time.sleep(2)
        response=requests.get(url,headers=headers).text
        soap= BeautifulSoup(response,"html.parser")
        links=soap.find_all("img",class_="serp-item__thumb justifier__thumb")
        for link in links:
            link = link.get("src")
            urls='https:'+ link
            img_data=requests.get(urls,verify=False).content
            save_img(img_data,img_type,img_number)
            img_number+=1
            print(f'Image {str(img_number).zfill(4)}.jpg is downloaded')
        page_number+=1 
        if img_number>999:
            break    

def main():
    #search_images('tiger')
    search_images('leopard')
    print('Successfully done!')
    
if __name__ == '__main__':
    main()