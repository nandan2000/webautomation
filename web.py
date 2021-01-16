from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# browser exposes an executable file
# Through Selenium test we will invoke the executable file which will then invoke actual browser
from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import time

nandan = Tk()
nandan.title("MADE BY NANDAN")
# setting the geometry of GUI
nandan.geometry("1080x720+220+25")


def search_result():
    # creating a bot which will invoke firefox browser
    bot = webdriver.Firefox()
    # creating a bot that will redirect to google.com
    bot.get('https://www.google.com/')
    result = bot.find_element_by_name('q')
    result.clear()
    result.send_keys(entry1.get())
    result.send_keys(Keys.RETURN)


def youtube():
    # creating a bot which will invoke firefox browser
    bot = webdriver.Firefox()
    bot.get('https://www.youtube.com/')


def instagram():
    # creating a bot which will invoke firefox browser
    bot = webdriver.Firefox()
    bot.get('https://www.instagram.com/')


def facebook():
    # creating a bot which will invoke firefox browser
    bot = webdriver.Firefox()
    bot.get('https://www.facebook.com/')


# inserting background image of GUI
backgroundimg = Image.open(
    "D:\\Entertainment\\PHOTOS\\Nandan Kumar Singh\\WEB BROWSER AUTOMATION PROJECT\\background1.jpg")
# resize background image
backgroundimg = backgroundimg.resize((1600, 800), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(backgroundimg)
label1 = Label(nandan, image=photo)
label1.place(x=0, y=0)

# creating youtube button
myyoutube = PhotoImage(
    file="D:\\Entertainment\\PHOTOS\\Nandan Kumar Singh\\WEB BROWSER AUTOMATION PROJECT\\youtube.jpg")
youtube = Button(nandan, image=myyoutube, command=youtube, height=200, width=300)
youtube.place(x=45, y=180)

# creating facebook button
myfacebook = PhotoImage(
    file="D:\\Entertainment\\PHOTOS\\Nandan Kumar Singh\\WEB BROWSER AUTOMATION PROJECT\\facebook.png")
facebook = Button(nandan, image=myfacebook, command=facebook, height=200, width=300)
facebook.place(x=385, y=180)

# creating instagram button
myinstagram = PhotoImage(
    file="D:\\Entertainment\\PHOTOS\\Nandan Kumar Singh\\WEB BROWSER AUTOMATION PROJECT\\instagram2.png")
instagram = Button(nandan, image=myinstagram, command=instagram, height=200, width=300)
instagram.place(x=725, y=180)

# creating a text Google
search = Label(nandan, text="Google", font='times 30')
# place of text google
search.place(x=8, y=8)

# creating an entry for user to search on google
entry1 = Entry(nandan)
entry1.place(x=150, y=30)

# creating a button for search
b1 = Button(nandan, text="search", command=search_result, width=12, bg='SlateBlue2', fg="white")
b1.place(x=280, y=28)

nandan.mainloop()
