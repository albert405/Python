from bs4 import BeautifulSoup
import requests
from tkinter import *
import tkinter.font as font
source_gpw = requests.get('https://www.biznesradar.pl/gielda/akcje_gpw').text
source_new_connect = requests.get('https://www.biznesradar.pl/gielda/newconnect').text
#data for cd projekt
soup = BeautifulSoup(source_gpw, 'lxml')
price = soup.find_all(class_='q_ch_act')
cena=(price[71].get_text())
zakup_akcji=22689
akcje_cdp="CDP",(float(cena)*100)-zakup_akcji

#date for onemorelevel
zakup_akcje2=14005
soup2 = BeautifulSoup(source_new_connect, 'lxml')
price2 = soup2.find_all(class_='q_ch_act')
cena2=(price2[238].get_text())
akcje_oml="OML",(float(cena2)*11000)-zakup_akcje2

RAZEM="RAZEM",(float(cena)*100)-zakup_akcji+(float(cena2)*11000)-zakup_akcje2
zmienna = 5
# aplikacja gui
root = Tk()
myLabel = Label(root, text=akcje_cdp, font='times 24 bold ', fg='green')
status = Label(root, text=akcje_oml, font='times 24 bold ', fg='green')
razem = Label(root, text=RAZEM, font='times 24 bold ', fg='green')
root.attributes("-topmost", True)
status.pack()
myLabel.pack()
razem.pack()
root.mainloop()
