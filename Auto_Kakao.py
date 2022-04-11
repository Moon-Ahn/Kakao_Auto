import sys
import pyautogui
import time
import pyperclip
import os
import random


def send_msg(my_msg, repeat_number):
    for i in range(int(repeat_number)):
        time_wait = random.uniform(3, 5)
        print('Repeat Number : ', i + 1, end='')
        print(' // Time wait : ', time_wait)
        time.sleep(time_wait)
        pyautogui.keyDown('enter')
        pyperclip.copy(my_msg)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.keyDown('enter')
        pyautogui.keyDown('esc')
        pyautogui.keyDown('down')


def filter_friend(filter_keyword, init_number):
    # 사람 아이콘 클릭
    try:
        click_img(img_path + 'chat2.png')
        try:
            click_img(img_path + 'chat.png')
        except Exception as e :
            print('e ', e)
            print('why')
    except Exception as e :
        print('no')
    # X 버튼이 존재한다면 클릭하여 내용 삭제
    try:
        click_img(img_path + 'newX.png')
    except:
        pass
    time.sleep(1)
    # 돋보기 아이콘 오른쪽 클릭
    click_img(img_path + 'newSearch.png')
    click_img_plus_x(img_path+'search_icon.png', 30)
    if filter_keyword == '':
        pyautogui.keyDown('esc')
    else:
        pyperclip.copy(filter_keyword)
    pyautogui.hotkey('ctrl', 'v')
    for i in range(int(init_number)-1):
        pyautogui.keyDown('down')
    time.sleep(2)


def click_img(imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x, y)


def click_img_plus_x(imagePath, pixel):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    print(location)
    x, y = location
    pyautogui.click(x + pixel, y)


def doubleClickImg (imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x, y, clicks=2)


def set_delay():
    delay_time = input("How many seconds do you want the program to run? : ")
    print("Run the program after "+ delay_time + "seconds.")
    for remaining in range(int(delay_time), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rProgram start!\n")
    os.system('"C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"')


def logout():
    try:
        click_img(img_path + 'menu.png')
    except Exception as e:
        print('e ', e)
    try:
        click_img(img_path + 'logout.png')
    except Exception as e:
        print('e ', e)


def bye_msg():
    input('Program ended.')


def set_import_msg():
    with open("send_for_text.txt", "r", encoding='UTF-8') as f:
        text = f.read()
        print('======== 아래는 전송할 텍스트입니다. ========\n', text)
        return text


def initialize():
    print('Monitor size : ', end='')
    print(pyautogui.size())
    print(pyautogui.position())
    filter_keyword = input("The friend name to filter on. If not, just enter.  ex) Middle Student : ")
    init_number = input("Starting Point by Friends Filtered (ex. 2) : ")
    repeat_number = input("number of repetitions (ex. 3) : ")
    my_msg = input("The message to send. When enter is pressed, send_for_text.txt is sent : ")
    print('=================')
    print('Message send start!')
    print('=================')
    #os.system('"C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"')
    return (filter_keyword, init_number, repeat_number, my_msg)


# config
img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'
conf = 0.90
pyautogui.PAUSE = 0.5

if __name__ == "__main__":
    (filter_keyword, init_number, repeat_number, my_msg) = initialize()
    if len(my_msg) > 2:
        os.system('"C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"')
        filter_friend(filter_keyword, init_number)
        send_msg(my_msg, repeat_number)
        bye_msg()

    else:
        long_msg = set_import_msg()
        set_delay()
        filter_friend(filter_keyword, init_number)
        send_msg(long_msg, repeat_number)
        logout()
        bye_msg()
