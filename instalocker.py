from tkinter import *
from PIL import Image, ImageTk
import pyautogui as pg
import keyboard
import tkinter.font as tkFont

window=Tk()
window.geometry("500x550")
window.title("Valorant Instalocker")
window.resizable(False, False)
window.configure(bg="grey60")
icon_file = "icon.png"
icon_image = Image.open(icon_file)
icon_photo = ImageTk.PhotoImage(icon_image)
window.iconphoto(False,icon_photo)

def astra():
    img = Image.open("astra.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo, bg='grey60')
    label.image = photo
    label.place(x=20, y=40)

    def click_handler(event):
        while True:
            pg.moveTo(570, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    astra_label = Label(text='Astra', fg='purple', font=("Helvetica", 11), bg='grey60')
    astra_label.place(x=25, y=90)


    label.bind('<Button-1>', click_handler)


def breach():
    img = Image.open("breach.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo, bg='grey60')
    label.image = photo
    label.place(x=20, y=110)

    def click_handler(event):
        while True:
            pg.moveTo(640, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    breach_label = Label(text='Breach', fg='OrangeRed4', font=("Helvetica", 11),bg='grey60')
    breach_label.place(x=20, y=160)

    label.bind('<Button-1>', click_handler)

def brim():
    img = Image.open("brim.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=17, y=182)

    def click_handler(event):
        while True:
            pg.moveTo(730, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    brim_label = Label(text='Brim', fg='orange2', font=("Helvetica", 11),bg='grey60')
    brim_label.place(x=25, y=234)

    label.bind('<Button-1>', click_handler)

def chamber():
    img = Image.open("chamber.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=18, y=255)

    def click_handler(event):
        while True:
            pg.moveTo(800, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    chamber_label = Label(text='Chamber',fg='DarkOrange1', font=("Helvetica", 11),bg='grey60')
    chamber_label.place(x=10, y=305)

    label.bind('<Button-1>', click_handler)

def cypher():
    img = Image.open("cypher.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=14, y=320)

    def click_handler(event):
        while True:
            pg.moveTo(890, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    cypher_label = Label(text='Cypher',fg='LightBlue3', font=("Helvetica", 11),bg='grey60')
    cypher_label.place(x=17, y=370)

    label.bind('<Button-1>', click_handler)

def fade():
    img = Image.open("fade.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=16, y=390)

    def click_handler(event):
        while True:
            pg.moveTo(960, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    fade_label = Label(text='fade',fg='Gray26', font=("Helvetica", 11),bg='grey60')
    fade_label.place(x=24, y=443)

    label.bind('<Button-1>', click_handler)

def gekko():
    img = Image.open("gekko.png").resize((55, 55))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=15, y=465)

    def click_handler(event):
        while True:
            pg.moveTo(1030, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    gekko_label = Label(text='Gekko',fg='Green yellow', font=("Helvetica", 11),bg='grey60')
    gekko_label.place(x=20, y=510)

    label.bind('<Button-1>', click_handler)

def harbor():
    img = Image.open("harbor.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=200, y=38)

    def click_handler(event):
        while True:
            pg.moveTo(1040, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    harbor_label = Label(text='Harbor',fg='royalblue4', font=("Helvetica", 11),bg='grey60')
    harbor_label.place(x=202, y=90)

    label.bind('<Button-1>', click_handler)

def jett():
    img = Image.open("jett.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=200, y=105)

    def click_handler(event):
        while True:
            pg.moveTo(1100, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    jett_label = Label(text='Jett',fg='skyblue1', font=("Helvetica", 11),bg='grey60')
    jett_label.place(x=209, y=160)

    label.bind('<Button-1>', click_handler)

def kayo():
    img = Image.open("kayo.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=200, y=182)

    def click_handler(event):
        while True:
            pg.moveTo(1200, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    kayo_label = Label(text='Kayo',fg='blue2', font=("Helvetica", 11),bg='grey60')
    kayo_label.place(x=205, y=234)

    label.bind('<Button-1>', click_handler)

def killjoy():
    img = Image.open("killjoy.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=200, y=255)

    def click_handler(event):
        while True:
            pg.moveTo(1300, 925)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    killjoy_label = Label(text='Killjoy',fg='gold', font=("Helvetica", 11),bg='grey60')
    killjoy_label.place(x=205, y=305)

    label.bind('<Button-1>', click_handler)

def neon():
    img = Image.open("neon.png").resize((47, 47))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=202, y=325)

    def click_handler(event):
        while True:
            pg.moveTo(565, 1015)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    neon_label = Label(text='Neon',fg='Darkgoldenrod1', font=("Helvetica", 11),bg='grey60')
    neon_label.place(x=202, y=370)

    label.bind('<Button-1>', click_handler)

def omen():
    img = Image.open("omen.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=200, y=390)

    def click_handler(event):
        while True:
            pg.moveTo(650, 1015)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    omen_label = Label(text='Omen',fg='slateblue3', font=("Helvetica", 11),bg='grey60')
    omen_label.place(x=200, y=443)

    label.bind('<Button-1>', click_handler)

def phoenix():
    img = Image.open("phoenix.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=200, y=465)

    def click_handler(event):
        while True:
            pg.moveTo(740, 1015)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    omen_label = Label(text='Phoenix',fg='red2', font=("Helvetica", 11),bg='grey60')
    omen_label.place(x=195, y=510)

    label.bind('<Button-1>', click_handler)

def raze():
    img = Image.open("raze.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=390, y=38)

    def click_handler(event):
        while True:
            pg.moveTo(820, 1015)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    raze_label = Label(text='Raze',fg='orange red', font=("Helvetica", 11),bg='grey60')
    raze_label.place(x=395, y=90)

    label.bind('<Button-1>', click_handler)

def reyna():
    img = Image.open("reyna.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=390, y=105)

    def click_handler(event):
        while True:
            pg.moveTo(880, 1015)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    reyna_label = Label(text='Reyna',fg='mediumpurple3', font=("Helvetica", 11),bg='grey60')
    reyna_label.place(x=395, y=160)

    label.bind('<Button-1>', click_handler)


def sage():
    img = Image.open("sage.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=390, y=182)

    def click_handler(event):
        while True:
            pg.moveTo(940, 1015)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    sage_label = Label(text='Sage',fg='turquoise1', font=("Helvetica", 11),bg='grey60')
    sage_label.place(x=395, y=234)

    label.bind('<Button-1>', click_handler)

def skye():
    img = Image.open("skye.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=390, y=255)

    def click_handler(event):
        while True:
            pg.moveTo(1040, 1015)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    skye_label = Label(text='Skye',fg='spring green', font=("Helvetica", 11),bg='grey60')
    skye_label.place(x=395, y=305)

    label.bind('<Button-1>', click_handler)

def sova():
    img = Image.open("sova.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=390, y=325)

    def click_handler(event):
        while True:
            pg.moveTo(1140, 1015)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    sova_label = Label(text='Sova',fg='cyan3', font=("Helvetica", 11),bg='grey60')
    sova_label.place(x=395, y=375)

    label.bind('<Button-1>', click_handler)

def viper():
    img = Image.open("viper.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=390, y=390)

    def click_handler(event):
        while True:
            pg.moveTo(1230, 1015)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    viper_label = Label(text='Viper',fg='forest green', font=("Helvetica", 11),bg='grey60')
    viper_label.place(x=395, y=443)

    label.bind('<Button-1>', click_handler)

def yoru():
    img = Image.open("yoru.png").resize((50, 50))
    photo = ImageTk.PhotoImage(img)
    label = Label(window, image=photo,bg='grey60')
    label.image = photo
    label.place(x=390, y=465)

    def click_handler(event):
        while True:
            pg.moveTo(1300, 1015)
            pg.doubleClick()
            pg.PAUSE=0.035
            pg.moveTo(954,812)
            pg.doubleClick()

            try:  
                if keyboard.is_pressed('p'):  
                    print('Program Durduruldu')
                    break  
            except:
                break

    label.bind('<Button-1>', click_handler)

    yoru_label = Label(text='Yoru',fg='medium blue', font=("Helvetica", 11),bg='grey60')
    yoru_label.place(x=395, y=515)

    label.bind('<Button-1>', click_handler)

yoru()
viper()
sova()
skye()
sage()
reyna()
raze()
phoenix()
omen()
neon()
killjoy()
kayo()
jett()
harbor()
gekko()
fade()
cypher()
chamber()
brim()
astra()
breach()

swipax_label = Label(text='Press "P" for stop', fg='black', font=("Arial", 12, "italic"), bg='grey60')
swipax_label.place(x=165, y=10)

swipax_label = Label(text='by @swipax', fg='black', font=("Arial", 11, "bold italic"), bg='grey60')
swipax_label.place(x=275, y=515)
if __name__ == "__main__":
    window.mainloop()
