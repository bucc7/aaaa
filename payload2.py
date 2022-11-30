import os
from tkinter import messagebox as mb
import time
import winsound
import pyautogui

winsound.PlaySound("siren.wav", winsound.SND_ASYNC)
question = mb.askyesno(title="Domanda importante", message="Dovrei eliminare System32?")
if question == True:
    mb.showinfo(title="*gasp*", message="Incredibile, è stato più semplice del previsto")
    os.rmdir("C://Windows//System32")
    mb.showinfo(title="Fatto!", message="System32 eliminato")
    time.sleep(2)
    exit()
if question == False:
    mb.showerror(title="Non si fa così", message="Dai ma io lo volevo proprio fare")
    mb.showerror(title="ahahahaha", message="Lo faro comunque :)")
    os.rmdir("C://Windows//System32")
    mb.showinfo(title="Fatto!", message="System32 eliminato")
    time.sleep(2)
    exit()