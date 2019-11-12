from selenium import webdriver
import time


def amsend(url):

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(40)
    i = 0
    danmu = ["你的操作666","阿奇我爱你","你就是深职第一ADC?","冲冲冲","明天早点起床跟我吃早餐哦","爱你么么哒","众星因你，皆化为尘。独尘因你，而化为星","水能载舟，亦能覆舟。江河万载，逆浪千秋","错的不是我，是这个世界",".这一世，我终将加冕为王!","给烟不给火，纯属调戏我。","我不说你不懂这便是距离。"]
    while(1):
        input = driver.find_element_by_class_name("ChatSend-txt")
        input.send_keys(danmu[i%12])

        btn = driver.find_element_by_class_name("ChatSend-button")
        btn.click()
        i = i+1
        print(i)
        time.sleep(2)
