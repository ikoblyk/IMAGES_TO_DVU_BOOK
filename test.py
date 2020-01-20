import urllib.request
from selenium import webdriver
import subprocess, sys



driverLocation = '/usr/bin/chromedriver'
driver = webdriver.Chrome(driverLocation)
path_to_save = '/home/ivan/Documents/Vovk'


def write_djvu(name):
    print("starting ...")
    subprocess.Popen(f'/home/ivan/jpg_to_djvu.sh {name}',cwd=path_to_save, shell=True)
    print("All Done!")

def connect():
    driver.get('https://elib.nlu.org.ua/view.html?&id=10930')

# get the image source
def get_src_original():
    img = driver.find_element_by_xpath('//center/div//img')
    src = img.get_attribute('src')
    modif = src.split('/')
    modif = modif[:len(modif)-1]
    return modif

def size():
    a =driver.find_element_by_xpath('//tr[@valign="center"]/td[4][1]').text[1:]
    return a

def name_of_file():
    temp = driver.find_element_by_xpath('//body//div[2]//a').text.split(' ')
    return '_'.join(temp)


def main(num):
    try:
        m = get_src_original()
        name = None
        if num < 10:
            name = f'000{num}.jpg'
        elif num >= 10 and num < 100:
            name = f'00{num}.jpg'
        elif num >= 100 and num <= 1000:
            name = f'0{num}.jpg'
        m.append(name)
        src = "/".join(m)
        m.pop()

        print("Downloading"+" "+src)

        urllib.request.urlretrieve(src, f"{path_to_save}/{name}")


    except:
        print("too much requests")

if __name__ == '__main__':
    connect()
    a = int(size())
    for  i in range(1,a+1):
        main(i)

    write_djvu(name_of_file())
    driver.close()