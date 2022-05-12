import numpy as np
import time
import random
import pyautogui as auto
from matplotlib import pyplot as plt
import glob
import smtplib
from verify_email import verify_email
import re

truth_website = np.load("website_verif.npy") 
number_pages = 8

def send_email(b_list_email, email, password):
    documents = glob.glob("./files/*.html")
    list_emails = []
    emails1 = []


    for document in documents:
        with open(document) as f:
            text = f.read()
            emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
            emails = list(set(emails))
            emails1 += emails
            emails1 = list(set(emails1))
            if b_list_email == None:
                b_list_email = []
            for b_email in b_list_email:
                if b_email in emails:
                    emails.remove(b_email)

            for email in emails:
                if verify_email(email):
                    list_emails.append(email)

    gmail_user = email 
    gmail_password = password 

    sent_from = gmail_user
    to = gmail_user 
    subject = 'Interested in Working for you! Informal Job Application'
    body = 'Greetings,\n\nMy name\'s name. I am currently looking for a job as a Bartender/Bar-Back/Waiter in city. I\'ve come across your place multiple times. I have sufficient experience both behind the bar and in front of customers. I would love to show you my customer service capabilities and work ethic. I am currently available for interviews and trials.\nThus, If any position is available at the moment, don\'t hesitate to notify me.\n\nSincerely, name.'

    for email in list_emails:
        try:
            email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(email), subject, body)
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, email, email_text)
            server.sendmail(sent_from, email, email_text)
            server.close()

            print('Email sent!')
        except:
            print('Something went wrong...')

        time.sleep(random.uniform(180.0,300.0)) 
    return emails1



def pause(t):
    time.sleep(random.uniform(t*0.8, t*1.2))


def write(word):
    pause(0.7)
    for letter in word:
        auto.hotkey('shift', letter)
        pause(0.3)

def comparaison(t, p):
    a = t.shape[0]
    b = t.shape[1]
    c = t.shape[2]
    for i in range(a):
        for j in range(b):
            for z in range(c):
                if t[i,j,z] != p[i,j,z]:
                    print(i,j,z)
    return True
def click_bar():
    auto.moveTo(279,463)
    pause(0.5)
    auto.click()
    pause(2.0)
    website_array = np.array(auto.screenshot())[362:401,510:603]
    if (website_array == truth_website).all():
        auto.moveTo(555, 395)
        pause(0.7)
        auto.click(button = 'right')
        pause(0.5)
        auto.moveTo(565,405)
        auto.click()
        pause(1.0)
        return True
    else:
        return False

def website(present_website, number_bar):
    if present_website:
        auto.hotkey('alt', '2')
        pause(2.0)
        auto.hotkey('ctrl', 's')
        pause(2.0)
        write(number_bar)
        pause(0.7)
        auto.press('enter')
        pause(18.0)
        auto.hotkey('ctrl', 'w')
        pause(1.0)
        auto.moveTo(1348,736)
        auto.click()
        pause(1.0)
    auto.moveTo(484,762)
    pause(0.2)
    for i in range(4):
        auto.click()
        pause(0.2)
    
email_thing = []


email_user = input("Email: ")
email_password = input("Password: ")

for page in range(number_pages):
    for bar_per_page in range(19):
        website(click_bar(), str(bar_per_page+page*19))
        email_thing = send_email(email_thing, email_user, email_password)
    auto.moveTo(484,762)
    pause(0.2)
    for i in range(10):
        auto.click()
        pause(0.2)
    auto.moveTo(395,564)
    pause(0.3)
    auto.click()
    pause(3.0)
