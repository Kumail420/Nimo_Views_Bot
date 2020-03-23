from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request as urllib2
import tkinter as tk
from tkinter import messagebox
import requests

root=tk.Tk()
root.withdraw()
root.wm_iconbitmap('logo.ico')
chrome_options = webdriver.ChromeOptions()




def connection_check():
    try:
        urllib2.urlopen('http://google.com', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def get_date():
    r=requests.get('https://www.calendardate.com/todays.htm')
    soup = BeautifulSoup(r.text ,'html.parser')
    a=soup.find_all(id='tprg')[6].get_text()
    a=a.replace('-','')
    a=a.replace(' ','')
    return a


def views_open(website,browser,i):

    try:
        browser[i].get(website)
    except:
        messagebox.showinfo('Link is unreachable')
    try:
        time.sleep(1)
        click_button = browser[i].find_element_by_xpath('//*[@id="nimo-player"]/div[4]/div/span').click()
    except:
        print(' ')
    try:
        play_button = browser[i].find_element_by_xpath('//*[@id="nimo-player"]/div[3]').click()
    except:
        print(' ')
    try:
        link = browser[i].find_element_by_xpath('//*[@id="hy-nimo-player-room"]/video').get_attribute('src')
    except:
        print("")

def run():

    website = e1.get()
    try:
        proxy_file = open('proxies.txt', 'r')
        proxies = proxy_file.readlines()
    except:
        messagebox.showinfo('Check proxy file in Directory')
        proxies = ''
    # e1 = str(input('Enter the url of the livestream: '))

    # e2 = int(input('How many views do you want to send: '))
    browser = []
    i = 0
    while i < num_count:
        for proxy in proxies:
            hostname = proxy.split(':')[0]
            port = proxy.split(':')[1]
            print('Using current IP:', hostname)
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_options.add_argument('--proxy-server=%s' % hostname + ":" + port)
            browser.append(webdriver.Chrome(options=chrome_options))
            views_open(website,browser, i)
        i += 1

def main():
    global e1
    global browser
    master = tk.Tk()

    tk.Label(master,
             text="Link of website").grid(row=0)
    tk.Label(master,
             text="Nimo View Bot").grid(row=1)

    e1 = tk.Entry(master)
    e1.grid(row=0, column=1)
    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master,
              text='Run',command=run).grid(row=3,
                                       column=1,
                                       sticky=tk.W,
                                       pady=4)

    tk.mainloop()


if connection_check() == True:
    serial_file = open('Serial.txt','r')
    global num_count
    numer = serial_file.readline()
    num_count = int(numer.split(',')[0])

    limit= int(numer.split(',')[1])
    current_date = int(get_date())

    if current_date <= limit:
        messagebox.showinfo("Enjoy Nimo View Bot \n","For contact and support for our products;\nDiscord:YaShiro#1907\nTeamSpeak server; yashiro.ts3omg.xyz\nhttps://www.youtube.com/c/POPGamerTVone\n")
        main()
    else:
        messagebox.showinfo("Expired","Sorry!!\n Your program is Expired")

else:
    messagebox.showinfo("Please ", "Check your internet connection")
