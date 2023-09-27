#URL:-
# A URL means UNIFORM RESOURCE LOCATOR it is address on the web is a reference

#URL_Shortener:-
# An URL shortener is awebsite that reduces the length of the URL
#minimizing the web page address into easier to remember and track
# the popular Url shortener are
#1)bit.ly
#2)tinyurl.com
#3)Goog.le...etc


import pyperclip
import pyshorteners
from tkinter import * # tkinter for GUI(GRAPHICAL USER INTERFACE) design

#define GUI for shortner
import urlshortener as urlshortener
root=Tk()
# set the geometry 
# root.geometry("40x20")
#give a title
root.title("URL shortener")
# set the background color
root.configure(bg="blue")

# taking two string variable for keep long and short url
url = StringVar()
url_address = StringVar()

# define function for shorting the url and copy the url
def urlshortener():
    urladdress=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="My url shortner" , font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate short url",command=urlshortener).pack(pady=10)
Entry(root,  textvariable=url_address).pack(pady=10)
Button(root, text="copy URL",command=copyurl).pack(pady=10)

root.mainloop()