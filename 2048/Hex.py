__author__ = 'Jasiu'
import random #sluzy do randomowego wybierania pozycji
import time
from PyQt4 import uic, QtCore, QtGui
from PyQt4.QtGui import *
import sys

punkty=0
zmiana=0
kierunek=0
ruch=""
wygrales=0
zero=0
koniec=0
cofka=0


#------------------------------------Inicjalizacja--------------------------------------

plansza=[[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0,0],[0,0,0]] #tworzy plansze
check=[[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0,0],[0,0,0]]
numer=[[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0,0],[0,0,0]]
pozycjaY=[0,1,2,3,4]
pozycjaX1=[0,1,2]
pozycjaX2=[0,1,2,3]
pozycjaX3=[0,1,2,3,4]
wiersz=random.choice(pozycjaY)
if wiersz==0 or wiersz==4:
    kolumna=random.choice(pozycjaX1)
if wiersz==1 or wiersz==3:
    kolumna=random.choice(pozycjaX2)
if wiersz==2:
    kolumna=random.choice(pozycjaX3)
plansza[wiersz][kolumna]=2 # wstawienie pierwszej 2
#------------------------------------Koniec inicjalizacji-------------------------------


def nowa():
    global plansza
    global punkty
    global zmiana
    global kierunek
    global zero
    global koniec
    punkty=0
    zmiana=0
    kierunek=0
    wygrales=0
    zero=0
    koniec=0
    plansza=[[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0,0],[0,0,0]] #tworzy plansze
    check=[[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0,0],[0,0,0]]
    numer=[[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0,0],[0,0,0]]
    pozycjaY=[0,1,2,3,4]
    pozycjaX1=[0,1,2]
    pozycjaX2=[0,1,2,3]
    pozycjaX3=[0,1,2,3,4]
    wiersz=random.choice(pozycjaY)
    if wiersz==0 or wiersz==4:
        kolumna=random.choice(pozycjaX1)
    if wiersz==1 or wiersz==3:
        kolumna=random.choice(pozycjaX2)
    if wiersz==2:
        kolumna=random.choice(pozycjaX3)
    plansza[wiersz][kolumna]=2 # wstawienie pierwszej 2



#-----------------------------------Ruch w lewo(4)--------------------------------------
def lewo(plansza):   #funkcja ruchu w lewo

    j=0
    for i in range(0,5): #przechodzenie przez wszystkie wiersze

       if i==0 or i==4:   # dla wiersza z 3 elementami
           if plansza[i][j]!=0 or plansza[i][j+1]!=0 or plansza[i][j+2]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i][j]= plansza[i][j+1]
                       plansza[i][j+1]= plansza[i][j+2]
                       plansza[i][j+2]= 0



               if plansza[i][j+1]==0 and plansza[i][j+2]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+1]= plansza[i][j+2]
                       plansza[i][j+2]= 0




       if i==1 or i==3:  #dla wiersz z 4 elementami
           if plansza[i][j]!=0 or plansza[i][j+1]!=0 or plansza[i][j+2]!=0 or plansza[i][j+3]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i][j]= plansza[i][j+1]
                       plansza[i][j+1]= plansza[i][j+2]
                       plansza[i][j+2]= plansza[i][j+3]
                       plansza[i][j+3]= 0



               if plansza[i][j+1]==0 and (plansza[i][j+2]!=0 or plansza[i][j+3]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+1]= plansza[i][j+2]
                       plansza[i][j+2]= plansza[i][j+3]
                       plansza[i][j+3]= 0


               if plansza[i][j+2]==0 and plansza[i][j+3]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+2]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+2]= plansza[i][j+3]
                       plansza[i][j+3]= 0




       if i==2:    #dla wiersza z 5 elementami
           if plansza[i][j]!=0 or plansza[i][j+1]!=0 or plansza[i][j+2]!=0 or plansza[i][j+3]!=0 or plansza[i][j+4]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i][j]= plansza[i][j+1]
                       plansza[i][j+1]= plansza[i][j+2]
                       plansza[i][j+2]= plansza[i][j+3]
                       plansza[i][j+3]= plansza[i][j+4]
                       plansza[i][j+4]= 0



           if plansza[i][j+1]==0 and (plansza[i][j+2]!=0 or plansza[i][j+3]!=0 or plansza[i][j+4]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+1]= plansza[i][j+2]
                       plansza[i][j+2]= plansza[i][j+3]
                       plansza[i][j+3]= plansza[i][j+4]
                       plansza[i][j+4]= 0




           if plansza[i][j+1]==0 and (plansza[i][j+3]!=0 or plansza[i][j+4]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+2]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+2]= plansza[i][j+3]
                       plansza[i][j+3]= plansza[i][j+4]
                       plansza[i][j+4]= 0



           if plansza[i][j+2]==0 and plansza[i][j+4]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+3]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+3]= plansza[i][j+4]
                       plansza[i][j+4]= 0


#-------------------------------------Koniec ruchu w lewo------------------------------------------------

#------------------------------------Funkcja dodawania po lewym ruchu------------------------------------
def lewe_dodanie(plansza):
    j=0
    global punkty


    for i in range(0,5):
         if i==0 or i==4:   # dla wiersza z 3 elementami
             if plansza[i][j]==plansza[i][j+1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j]=plansza[i][j]+plansza[i][j+1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j]**2     #dodanie punktow
                plansza[i][j+1]=plansza[i][j+2]   # przypisanie trzeciego elementu jako drugi
                plansza[i][j+2]= 0     #przypisanie trzeciemu elementowi wartosci zerowej



             if plansza[i][j+1]==plansza[i][j+2]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+1]=plansza[i][j+1]+plansza[i][j+2]
                punkty+=plansza[i][j+1]**2
                plansza[i][j+2]=0



         if i==1 or i==3:   # dla wiersza z 4 elementami
             if plansza[i][j]==plansza[i][j+1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j]=plansza[i][j]+plansza[i][j+1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j]**2     #dodanie punktow
                plansza[i][j+1]=plansza[i][j+2]   # przypisanie trzeciego elementu jako drugi
                plansza[i][j+2]=plansza[i][j+3]
                plansza[i][j+3]= 0     #przypisanie czwartemu elementowi wartosci zerowej


             if plansza[i][j+1]==plansza[i][j+2]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+1]=plansza[i][j+1]+plansza[i][j+2]
                punkty+=plansza[i][j+1]**2
                plansza[i][j+2]=plansza[i][j+3]
                plansza[i][j+3]=0



             if plansza[i][j+2]==plansza[i][j+3]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+2]=plansza[i][j+2]+plansza[i][j+3]
                punkty+=plansza[i][j+2]**2
                plansza[i][j+3]=0


         if i==2:   # dla wiersza z 5 elementami
             if plansza[i][j]==plansza[i][j+1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j]=plansza[i][j]+plansza[i][j+1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j]**2     #dodanie punktow
                plansza[i][j+1]=plansza[i][j+2]   # przypisanie trzeciego elementu jako drugi
                plansza[i][j+2]=plansza[i][j+3]
                plansza[i][j+3]=plansza[i][j+4]
                plansza[i][j+4]= 0     #przypisanie piatemu elementowi wartosci zerowej



             if plansza[i][j+1]==plansza[i][j+2]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+1]=plansza[i][j+1]+plansza[i][j+2]
                punkty+=plansza[i][j+1]**2
                plansza[i][j+2]=plansza[i][j+3]
                plansza[i][j+3]=plansza[i][j+4]
                plansza[i][j+4]=0



             if plansza[i][j+2]==plansza[i][j+3]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+2]=plansza[i][j+2]+plansza[i][j+3]
                punkty+=plansza[i][j+2]**2
                plansza[i][j+3]=plansza[i][j+4]
                plansza[i][j+4]=0



             if plansza[i][j+3]==plansza[i][j+4]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+3]=plansza[i][j+3]+plansza[i][j+4]
                punkty+=plansza[i][j+3]**2
                plansza[i][j+4]=0

#------------------------------------Koniec funkcji dodawania po lewym ruchu----------------------------

#-----------------------------------Ruch w prawo(6)--------------------------------------
def prawo(plansza):   #funkcja ruchu w prawo
    j=0
    for i in range(0,5): #przechodzenie przez wszystkie wiersze

       if i==0 or i==4:   # dla wiersza z 3 elementami
           if plansza[i][j]!=0 or plansza[i][j+1]!=0 or plansza[i][j+2]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j+2]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j+2]==0:  #przesuwanie aby ostatni element nie byl zerowy
                       plansza[i][j+2]= plansza[i][j+1]
                       plansza[i][j+1]= plansza[i][j]
                       plansza[i][j]= 0



               if plansza[i][j+1]==0 and plansza[i][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+1]= plansza[i][j]
                       plansza[i][j]= 0




       if i==1 or i==3:  #dla wiersz z 4 elementami
           if plansza[i][j]!=0 or plansza[i][j+1]!=0 or plansza[i][j+2]!=0 or plansza[i][j+3]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j+3]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j+3]==0:  #przesuwanie aby ostatni element nie byl zerowy
                       plansza[i][j+3]= plansza[i][j+2]
                       plansza[i][j+2]= plansza[i][j+1]
                       plansza[i][j+1]= plansza[i][j]
                       plansza[i][j]= 0



               if plansza[i][j+2]==0 and (plansza[i][j+1]!=0 or plansza[i][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+2]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+2]= plansza[i][j+1]
                       plansza[i][j+1]= plansza[i][j]
                       plansza[i][j]= 0



               if plansza[i][j+1]==0 and plansza[i][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+1]= plansza[i][j]
                       plansza[i][j]= 0




       if i==2:    #dla wiersza z 5 elementami
           if plansza[i][j]!=0 or plansza[i][j+1]!=0 or plansza[i][j+2]!=0 or plansza[i][j+3]!=0 or plansza[i][j+4]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j+4]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j+4]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i][j+4]= plansza[i][j+3]
                       plansza[i][j+3]= plansza[i][j+2]
                       plansza[i][j+2]= plansza[i][j+1]
                       plansza[i][j+1]= plansza[i][j]
                       plansza[i][j]= 0



           if plansza[i][j+3]==0 and (plansza[i][j+2]!=0 or plansza[i][j+1]!=0 or plansza[i][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+3]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+3]= plansza[i][j+2]
                       plansza[i][j+2]= plansza[i][j+1]
                       plansza[i][j+1]= plansza[i][j]
                       plansza[i][j]= 0



           if plansza[i][j+2]==0 and (plansza[i][j+1]!=0 or plansza[i][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+2]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+2]= plansza[i][j+1]
                       plansza[i][j+1]= plansza[i][j]
                       plansza[i][j]= 0



           if plansza[i][j+1]==0 and plansza[i][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i][j+1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i][j+1]= plansza[i][j]
                       plansza[i][j]= 0
#-------------------------------------Koniec ruchu w prawo------------------------------------------------

#------------------------------------Funkcja dodawania po prawym ruchu------------------------------------
def prawe_dodanie(plansza):
    j=0
    global punkty


    for i in range(0,5):
         if i==0 or i==4:   # dla wiersza z 3 elementami
             if plansza[i][j+2]==plansza[i][j+1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j+2]=plansza[i][j+2]+plansza[i][j+1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j+2]**2     #dodanie punktow
                plansza[i][j+1]=plansza[i][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i][j]= 0     #przypisanie trzeciemu elementowi wartosci zerowej



             if plansza[i][j+1]==plansza[i][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+1]=plansza[i][j+1]+plansza[i][j]
                punkty+=plansza[i][j+1]**2
                plansza[i][j]=0



         if i==1 or i==3:   # dla wiersza z 4 elementami
             if plansza[i][j+3]==plansza[i][j+2]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j+3]=plansza[i][j+3]+plansza[i][j+2]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j+3]**2     #dodanie punktow
                plansza[i][j+2]=plansza[i][j+1]   # przypisanie trzeciego elementu jako drugi
                plansza[i][j+1]=plansza[i][j]
                plansza[i][j]= 0     #przypisanie czwartemu elementowi wartosci zerowej


             if plansza[i][j+2]==plansza[i][j+1]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+2]=plansza[i][j+2]+plansza[i][j+1]
                punkty+=plansza[i][j+2]**2
                plansza[i][j+1]=plansza[i][j]
                plansza[i][j]=0



             if plansza[i][j+1]==plansza[i][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+1]=plansza[i][j+1]+plansza[i][j]
                punkty+=plansza[i][j+1]**2
                plansza[i][j]=0


         if i==2:   # dla wiersza z 5 elementami
             if plansza[i][j+4]==plansza[i][j+3]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j+4]=plansza[i][j+4]+plansza[i][j+3]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j+4]**2     #dodanie punktow
                plansza[i][j+3]=plansza[i][j+2]   # przypisanie trzeciego elementu jako drugi
                plansza[i][j+2]=plansza[i][j+1]
                plansza[i][j+1]=plansza[i][j]
                plansza[i][j]= 0     #przypisanie piatemu elementowi wartosci zerowej



             if plansza[i][j+3]==plansza[i][j+2]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+3]=plansza[i][j+3]+plansza[i][j+2]
                punkty+=plansza[i][j+3]**2
                plansza[i][j+2]=plansza[i][j+1]
                plansza[i][j+1]=plansza[i][j]
                plansza[i][j]=0



             if plansza[i][j+2]==plansza[i][j+1]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+2]=plansza[i][j+2]+plansza[i][j+1]
                punkty+=plansza[i][j+2]**2
                plansza[i][j+1]=plansza[i][j]
                plansza[i][j]=0



             if plansza[i][j+1]==plansza[i][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i][j+1]=plansza[i][j+1]+plansza[i][j]
                punkty+=plansza[i][j+1]**2
                plansza[i][j]=0

#------------------------------------Koniec funkcji dodawania po prawym ruchu----------------------------

#-----------------------------------Ruch w gora-lewo(7)--------------------------------------
def gora_lewo(plansza):   #funkcja ruchu w lewo
    i=0
    for j in range(0,5): #przechodzenie przez wszystkie wiersze


       if j==0:   # dla wiersza z 3 elementami
           if plansza[i+2][j]!=0 or plansza[i+3][j]!=0 or plansza[i+4][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+2][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+2][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+2][j]= plansza[i+3][j]
                       plansza[i+3][j]= plansza[i+4][j]
                       plansza[i+4][j]= 0


               if plansza[i+3][j]==0 and plansza[i+4][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j]= plansza[i+4][j]
                       plansza[i+4][j]= 0



       if j==1 :  #dla wiersz z 4 elementami
           if plansza[i+1][j-1]!=0 or plansza[i+2][j]!=0 or plansza[i+3][j]!=0 or plansza[i+4][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+1][j-1]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+1][j-1]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+1][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+3][j]
                       plansza[i+3][j]= plansza[i+4][j]
                       plansza[i+4][j]= 0


               if plansza[i+2][j]==0 and (plansza[i+3][j]!=0 or plansza[i+4][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+3][j]
                       plansza[i+3][j]= plansza[i+4][j]
                       plansza[i+4][j]= 0


               if plansza[i+3][j]==0 and plansza[i+4][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j]= plansza[i+4][j]
                       plansza[i+4][j]= 0



       if j==2:    #dla wiersza z 5 elementami
           if plansza[i][j-2]!=0 or plansza[i+1][j-1]!=0 or plansza[i+2][j]!=0 or plansza[i+3][j]!=0 or plansza[i+4][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j-2]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j-2]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i][j-2]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+3][j]
                       plansza[i+3][j]= plansza[i+4][j]
                       plansza[i+4][j]= 0


           if plansza[i+1][j-1]==0 and (plansza[i+2][j]!=0 or plansza[i+3][j]!=0 or plansza[i+4][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+3][j]
                       plansza[i+3][j]= plansza[i+4][j]
                       plansza[i+4][j]= 0


           if plansza[i+2][j]==0 and (plansza[i+3][j]!=0 or plansza[i+4][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+3][j]
                       plansza[i+3][j]= plansza[i+4][j]
                       plansza[i+4][j]= 0


           if plansza[i+3][j]==0 and plansza[i+4][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j]= plansza[i+4][j]
                       plansza[i+4][j]= 0


       if j==3 :  #dla wiersz z 4 elementami
           if plansza[i][j-2]!=0 or plansza[i+1][j-1]!=0 or plansza[i+2][j]!=0 or plansza[i+3][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j-2]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j-2]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i][j-2]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+3][j]
                       plansza[i+3][j]= 0


               if plansza[i+1][j-1]==0 and (plansza[i+2][j]!=0 or plansza[i+3][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+3][j]
                       plansza[i+3][j]= 0


               if plansza[i+2][j]==0 and plansza[i+3][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+3][j]
                       plansza[i+3][j]= 0

       if j==4:   # dla wiersza z 3 elementami
           if plansza[i][j-2]!=0 or plansza[i+1][j-1]!=0 or plansza[i+2][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j-2]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j-2]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i][j-2]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= 0


               if plansza[i+1][j-1]==0 and plansza[i+2][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= 0

#-------------------------------------Koniec ruchu w gore-lewo------------------------------------------------

#------------------------------------Funkcja dodawania po gora-lewym ruchu------------------------------------
def gora_lewe_dodanie(plansza):
    i=0
    global punkty


    for j in range(0,5):
         if j==0:   # dla wiersza z 3 elementami
             if plansza[i+2][j]==plansza[i+3][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+3][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+2][j]**2     #dodanie punktow
                plansza[i+3][j]=plansza[i+4][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+4][j]= 0     #przypisanie trzeciemu elementowi wartosci zerowej



             if plansza[i+3][j]==plansza[i+4][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j]=plansza[i+3][j]+plansza[i+4][j]
                punkty+=plansza[i+3][j]**2
                plansza[i+4][j]=0


         if j==1:   # dla wiersza z 4 elementami
             if plansza[i+1][j-1]==plansza[i+2][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+1][j-1]=plansza[i+1][j-1]+plansza[i+2][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+1][j-1]**2     #dodanie punktow
                plansza[i+2][j]=plansza[i+3][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+3][j]=plansza[i+3][j]
                plansza[i+4][j]= 0     #przypisanie czwartemu elementowi wartosci zerowej


             if plansza[i+2][j]==plansza[i+3][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+3][j]
                punkty+=plansza[i+2][j]**2
                plansza[i+3][j]=plansza[i+4][j]
                plansza[i+4][j]=0



             if plansza[i+3][j]==plansza[i+4][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j]=plansza[i+3][j]+plansza[i+4][j]
                punkty+=plansza[i+3][j]**2
                plansza[i+4][j]=0


         if j==2:   # dla wiersza z 5 elementami
             if plansza[i][j-2]==plansza[i+1][j-1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j-2]=plansza[i][j-2]+plansza[i+1][j-1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j-2]**2     #dodanie punktow
                plansza[i+1][j-1]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]=plansza[i+3][j]
                plansza[i+3][j]=plansza[i+4][j]
                plansza[i+4][j]= 0     #przypisanie piatemu elementowi wartosci zerowej



             if plansza[i+1][j-1]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j-1]=plansza[i+1][j-1]+plansza[i+2][j]
                punkty+=plansza[i+1][j-1]**2
                plansza[i+2][j]=plansza[i+3][j]
                plansza[i+3][j]=plansza[i+4][j]
                plansza[i+4][j]=0



             if plansza[i+2][j]==plansza[i+3][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+3][j]
                punkty+=plansza[i+2][j]**2
                plansza[i+3][j]=plansza[i+4][j]
                plansza[i+4][j]=0



             if plansza[i+3][j]==plansza[i+4][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j]=plansza[i+3][j]+plansza[i+4][j]
                punkty+=plansza[i+3][j]**2
                plansza[i+4][j]=0



         if j==3:   # dla wiersza z 4 elementami
             if plansza[i][j-2]==plansza[i+1][j-1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j-2]=plansza[i][j-2]+plansza[i+1][j-1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j-2]**2     #dodanie punktow
                plansza[i+1][j-1]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]=plansza[i+3][j]
                plansza[i+3][j]= 0     #przypisanie czwartemu elementowi wartosci zerowej


             if plansza[i+1][j-1]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j-1]=plansza[i+1][j-1]+plansza[i+2][j]
                punkty+=plansza[i+1][j-1]**2
                plansza[i+2][j]=plansza[i+3][j]
                plansza[i+3][j]=0



             if plansza[i+2][j]==plansza[i+3][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+3][j]
                punkty+=plansza[i+2][j]**2
                plansza[i+3][j]=0

         if j==4:   # dla wiersza z 3 elementami
             if plansza[i][j-2]==plansza[i+1][j-1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j-2]=plansza[i][j-2]+plansza[i+1][j-1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j-2]**2     #dodanie punktow
                plansza[i+1][j-1]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]= 0     #przypisanie trzeciemu elementowi wartosci zerowej



             if plansza[i+1][j-1]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j-1]=plansza[i+1][j-1]+plansza[i+2][j]
                punkty+=plansza[i+1][j-1]**2
                plansza[i+2][j]=0

#------------------------------------Koniec funkcji dodawania po gora-lewym ruchu----------------------------

#-----------------------------------Ruch w gora-prawo(9)--------------------------------------
def gora_prawo(plansza):   #funkcja ruchu w lewo
    i=0
    for j in range(0,5): #przechodzenie przez wszystkie wiersze


       if j==0:   # dla wiersza z 3 elementami
           if plansza[i][j]!=0 or plansza[i+1][j]!=0 or plansza[i+2][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i][j]= plansza[i+1][j]
                       plansza[i+1][j]= plansza[i+2][j]
                       plansza[i+2][j]= 0


               if plansza[i+1][j]==0 and plansza[i+2][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j]= plansza[i+2][j]
                       plansza[i+2][j]= 0



       if j==1 :  #dla wiersz z 4 elementami
           if plansza[i][j]!=0 or plansza[i+1][j]!=0 or plansza[i+2][j]!=0 or plansza[i+3][j-1]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i][j]= plansza[i+1][j]
                       plansza[i+1][j]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= 0


               if plansza[i+1][j]==0 and (plansza[i+2][j]!=0 or plansza[i+3][j-1]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= 0


               if plansza[i+2][j]==0 and plansza[i+3][j-1]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= 0



       if j==2:    #dla wiersza z 5 elementami
           if plansza[i][j]!=0 or plansza[i+1][j]!=0 or plansza[i+2][j]!=0 or plansza[i+3][j-1]!=0 or plansza[i+4][j-2]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i][j]= plansza[i+1][j]
                       plansza[i+1][j]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= plansza[i+4][j-2]
                       plansza[i+4][j-2]= 0


           if plansza[i+1][j]==0 and (plansza[i+2][j]!=0 or plansza[i+3][j-1]!=0 or plansza[i+4][j-2]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= plansza[i+4][j-2]
                       plansza[i+4][j-2]= 0


           if plansza[i+2][j]==0 and (plansza[i+3][j-1]!=0 or plansza[i+4][j-2]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= plansza[i+4][j-2]
                       plansza[i+4][j-2]= 0


           if plansza[i+3][j-1]==0 and plansza[i+4][j-2]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j-1]= plansza[i+4][j-2]
                       plansza[i+4][j-2]= 0


       if j==3 :  #dla wiersz z 4 elementami
           if plansza[i+1][j]!=0 or plansza[i+2][j]!=0 or plansza[i+3][j-1]!=0 or plansza[i+4][j-2]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+1][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+1][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+1][j]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= plansza[i+4][j-2]
                       plansza[i+4][j-2]= 0


               if plansza[i+2][j]==0 and (plansza[i+3][j-1]!=0 or plansza[i+4][j-2]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= plansza[i+4][j-2]
                       plansza[i+4][j-2]= 0


               if plansza[i+3][j-1]==0 and plansza[i+4][j-2]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j-1]= plansza[i+4][j-2]
                       plansza[i+4][j-2]= 0

       if j==4:   # dla wiersza z 3 elementami
           if plansza[i+2][j]!=0 or plansza[i+3][j-1]!=0 or plansza[i+4][j-2]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+2][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+2][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+2][j]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= plansza[i+4][j-2]
                       plansza[i+4][j-2]= 0


               if plansza[i+3][j-1]==0 and plansza[i+4][j-2]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j-1]= plansza[i+4][j-2]
                       plansza[i+4][j-2]= 0

#-------------------------------------Koniec ruchu w gore-prawo------------------------------------------------

#------------------------------------Funkcja dodawania po gora-prawym ruchu------------------------------------
def gora_prawy_dodanie(plansza):
    i=0
    global punkty


    for j in range(0,5):
         if j==0:   # dla wiersza z 3 elementami
             if plansza[i][j]==plansza[i+1][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j]=plansza[i][j]+plansza[i+1][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j]**2     #dodanie punktow
                plansza[i+1][j]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]= 0     #przypisanie trzeciemu elementowi wartosci zerowej



             if plansza[i+1][j]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j]=plansza[i+1][j]+plansza[i+2][j]
                punkty+=plansza[i+1][j]**2
                plansza[i+2][j]=0


         if j==1:   # dla wiersza z 4 elementami
             if plansza[i][j]==plansza[i+1][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j]=plansza[i][j]+plansza[i+1][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j]**2     #dodanie punktow
                plansza[i+1][j]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]=plansza[i+3][j-1]
                plansza[i+3][j-1]= 0     #przypisanie czwartemu elementowi wartosci zerowej


             if plansza[i+1][j]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j]=plansza[i+1][j]+plansza[i+2][j]
                punkty+=plansza[i+1][j]**2
                plansza[i+2][j]=plansza[i+3][j-1]
                plansza[i+3][j-1]=0



             if plansza[i+2][j]==plansza[i+3][j-1]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+3][j-1]
                punkty+=plansza[i+2][j]**2
                plansza[i+3][j-1]=0


         if j==2:   # dla wiersza z 5 elementami
             if plansza[i][j]==plansza[i+1][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i][j]=plansza[i][j]+plansza[i+1][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i][j]**2     #dodanie punktow
                plansza[i+1][j]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]=plansza[i+3][j-1]
                plansza[i+3][j-1]=plansza[i+4][j-2]
                plansza[i+4][j-2]= 0     #przypisanie piatemu elementowi wartosci zerowej



             if plansza[i+1][j]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j]=plansza[i+1][j]+plansza[i+2][j]
                punkty+=plansza[i+1][j]**2
                plansza[i+2][j]=plansza[i+3][j-1]
                plansza[i+3][j-1]=plansza[i+4][j-2]
                plansza[i+4][j-2]=0



             if plansza[i+2][j]==plansza[i+3][j-1]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+3][j-1]
                punkty+=plansza[i+2][j]**2
                plansza[i+3][j-1]=plansza[i+4][j-2]
                plansza[i+4][j-2]=0



             if plansza[i+3][j-1]==plansza[i+4][j-2]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j-1]=plansza[i+3][j-1]+plansza[i+4][j-2]
                punkty+=plansza[i+3][j-1]**2
                plansza[i+4][j-2]=0



         if j==3:   # dla wiersza z 4 elementami
             if plansza[i+1][j]==plansza[i+2][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+1][j]=plansza[i+1][j]+plansza[i+2][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+1][j]**2     #dodanie punktow
                plansza[i+2][j]=plansza[i+3][j-1]   # przypisanie trzeciego elementu jako drugi
                plansza[i+3][j-1]=plansza[i+3][j-2]
                plansza[i+4][j-2]= 0     #przypisanie czwartemu elementowi wartosci zerowej


             if plansza[i+2][j]==plansza[i+3][j-1]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+3][j-1]
                punkty+=plansza[i+2][j]**2
                plansza[i+3][j-1]=plansza[i+4][j-2]
                plansza[i+4][j-2]=0



             if plansza[i+3][j-1]==plansza[i+4][j-2]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j-1]=plansza[i+3][j-1]+plansza[i+4][j-2]
                punkty+=plansza[i+3][j-1]**2
                plansza[i+4][j-2]=0

         if j==4:   # dla wiersza z 3 elementami
             if plansza[i+2][j]==plansza[i+3][j-1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+3][j-1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+2][j]**2     #dodanie punktow
                plansza[i+3][j-1]=plansza[i+4][j-2]   # przypisanie trzeciego elementu jako drugi
                plansza[i+4][j-2]= 0     #przypisanie trzeciemu elementowi wartosci zerowej



             if plansza[i+3][j-1]==plansza[i+4][j-2]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j-1]=plansza[i+3][j-1]+plansza[i+4][j-2]
                punkty+=plansza[i+3][j-1]**2
                plansza[i+4][j-2]=0

#------------------------------------Koniec funkcji dodawania po gora-prawym ruchu----------------------------

#-----------------------------------Ruch w dol-prawo(3)--------------------------------------
def dol_prawo(plansza):   #funkcja ruchu w lewo
    i=0
    for j in range(0,5): #przechodzenie przez wszystkie wiersze


       if j==0:   # dla wiersza z 3 elementami
           if plansza[i+4][j]!=0 or plansza[i+3][j]!=0 or plansza[i+2][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+4][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+4][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+4][j]= plansza[i+3][j]
                       plansza[i+3][j]= plansza[i+2][j]
                       plansza[i+2][j]= 0


               if plansza[i+3][j]==0 and plansza[i+2][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j]= plansza[i+2][j]
                       plansza[i+2][j]= 0



       if j==1 :  #dla wiersz z 4 elementami
           if plansza[i+4][j]!=0 or plansza[i+3][j]!=0 or plansza[i+2][j]!=0 or plansza[i+1][j-1]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+4][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+4][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+4][j]= plansza[i+3][j]
                       plansza[i+3][j]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= 0


               if plansza[i+3][j]==0 and (plansza[i+2][j]!=0 or plansza[i+1][j-1]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= 0


               if plansza[i+2][j]==0 and plansza[i+1][j-1]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= 0



       if j==2:    #dla wiersza z 5 elementami
           if plansza[i+4][j]!=0 or plansza[i+3][j]!=0 or plansza[i+2][j]!=0 or plansza[i+1][j-1]!=0 or plansza[i][j-2]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+4][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+4][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+4][j]= plansza[i+3][j]
                       plansza[i+3][j]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= plansza[i][j-2]
                       plansza[i][j-2]= 0


           if plansza[i+3][j]==0 and (plansza[i+2][j]!=0 or plansza[i+1][j-1]!=0 or plansza[i][j-2]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= plansza[i][j-2]
                       plansza[i][j-2]= 0


           if plansza[i+2][j]==0 and (plansza[i+1][j-1]!=0 or plansza[i][j-2]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= plansza[i][j-2]
                       plansza[i][j-2]= 0


           if plansza[i+1][j-1]==0 and plansza[i][j-2]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j-1]= plansza[i][j-2]
                       plansza[i][j-2]= 0


       if j==3 :  #dla wiersz z 4 elementami
           if plansza[i+3][j]!=0 or plansza[i+2][j]!=0 or plansza[i+1][j-1]!=0 or plansza[i][j-2]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+3][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+3][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+3][j]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= plansza[i][j-2]
                       plansza[i][j-2]= 0


               if plansza[i+2][j]==0 and (plansza[i+1][j-1]!=0 or plansza[i][j-2]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= plansza[i][j-2]
                       plansza[i][j-2]= 0


               if plansza[i+1][j-1]==0 and plansza[i][j-2]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j-1]= plansza[i][j-2]
                       plansza[i][j-2]= 0

       if j==4:   # dla wiersza z 3 elementami
           if plansza[i+2][j]!=0 or plansza[i+1][j-1]!=0 or plansza[i][j-2]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+2][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+2][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+2][j]= plansza[i+1][j-1]
                       plansza[i+1][j-1]= plansza[i][j-2]
                       plansza[i][j-2]= 0


               if plansza[i+1][j-1]==0 and plansza[i][j-2]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j-1]= plansza[i][j-2]
                       plansza[i][j-2]= 0

#-------------------------------------Koniec ruchu w dol-prawo------------------------------------------------

#------------------------------------Funkcja dodawania po dol-prawym ruchu------------------------------------
def dol_prawe_dodanie(plansza):
    i=0
    global punkty


    for j in range(0,5):
         if j==0:   # dla wiersza z 3 elementami
             if plansza[i+4][j]==plansza[i+3][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+4][j]=plansza[i+4][j]+plansza[i+3][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+4][j]**2     #dodanie punktow
                plansza[i+3][j]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]= 0     #przypisanie trzeciemu elementowi wartosci zerowej



             if plansza[i+3][j]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j]=plansza[i+3][j]+plansza[i+2][j]
                punkty+=plansza[i+3][j]**2
                plansza[i+2][j]=0


         if j==1:   # dla wiersza z 4 elementami
             if plansza[i+4][j]==plansza[i+3][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+4][j]=plansza[i+4][j]+plansza[i+3][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+4][j]**2     #dodanie punktow
                plansza[i+3][j]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]=plansza[i+1][j-1]
                plansza[i+1][j-1]= 0     #przypisanie czwartemu elementowi wartosci zerowej


             if plansza[i+3][j]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j]=plansza[i+3][j]+plansza[i+2][j]
                punkty+=plansza[i+3][j]**2
                plansza[i+2][j]=plansza[i+1][j-1]
                plansza[i+1][j-1]=0



             if plansza[i+2][j]==plansza[i+1][j-1]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+1][j-1]
                punkty+=plansza[i+2][j]**2
                plansza[i+1][j-1]=0


         if j==2:   # dla wiersza z 5 elementami
             if plansza[i+4][j]==plansza[i+3][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+4][j]=plansza[i+4][j]+plansza[i+3][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+4][j]**2     #dodanie punktow
                plansza[i+3][j]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]=plansza[i+1][j-1]
                plansza[i+1][j-1]=plansza[i][j-2]
                plansza[i][j-2]= 0     #przypisanie piatemu elementowi wartosci zerowej



             if plansza[i+3][j]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j]=plansza[i+3][j]+plansza[i+2][j]
                punkty+=plansza[i+3][j]**2
                plansza[i+2][j]=plansza[i+1][j-1]
                plansza[i+1][j-1]=plansza[i][j-2]
                plansza[i][j-2]=0



             if plansza[i+2][j]==plansza[i+1][j-1]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+1][j-1]
                punkty+=plansza[i+2][j]**2
                plansza[i+1][j-1]=plansza[i][j-2]
                plansza[i][j-2]=0



             if plansza[i+1][j-1]==plansza[i][j-2]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j-1]=plansza[i+1][j-1]+plansza[i][j-2]
                punkty+=plansza[i+1][j-1]**2
                plansza[i][j-2]=0



         if j==3:   # dla wiersza z 4 elementami
             if plansza[i+3][j]==plansza[i+2][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+3][j]=plansza[i+3][j]+plansza[i+2][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+3][j]**2     #dodanie punktow
                plansza[i+2][j]=plansza[i+1][j-1]   # przypisanie trzeciego elementu jako drugi
                plansza[i+1][j-1]=plansza[i][j-2]
                plansza[i][j-2]= 0     #przypisanie czwartemu elementowi wartosci zerowej


             if plansza[i+2][j]==plansza[i+1][j-1]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+1][j-1]
                punkty+=plansza[i+2][j]**2
                plansza[i+1][j-1]=plansza[i][j-2]
                plansza[i][j-2]=0



             if plansza[i+1][j-1]==plansza[i][j-2]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j-1]=plansza[i+1][j-1]+plansza[i][j-2]
                punkty+=plansza[i+1][j-1]**2
                plansza[i][j-2]=0

         if j==4:   # dla wiersza z 3 elementami
             if plansza[i+2][j]==plansza[i+1][j-1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+1][j-1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+2][j]**2     #dodanie punktow
                plansza[i+1][j-1]=plansza[i][j-2]   # przypisanie trzeciego elementu jako drugi
                plansza[i][j-2]= 0     #przypisanie trzeciemu elementowi wartosci zerowej



             if plansza[i+1][j-1]==plansza[i][j-2]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j-1]=plansza[i+1][j-1]+plansza[i][j-2]
                punkty+=plansza[i+1][j-1]**2
                plansza[i][j-2]=0

#------------------------------------Koniec funkcji dodawania po dol-prawym ruchu----------------------------

#-----------------------------------Ruch w dol-lewo(1)--------------------------------------
def dol_lewo(plansza):   #funkcja ruchu w lewo
    i=0
    for j in range(0,5): #przechodzenie przez wszystkie wiersze


       if j==0:   # dla wiersza z 3 elementami
           if plansza[i+2][j]!=0 or plansza[i+1][j]!=0 or plansza[i][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+2][j]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+2][j]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+2][j]= plansza[i+1][j]
                       plansza[i+1][j]= plansza[i][j]
                       plansza[i][j]= 0


               if plansza[i+1][j]==0 and plansza[i][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j]= plansza[i][j]
                       plansza[i][j]= 0



       if j==1 :  #dla wiersz z 4 elementami
           if plansza[i+3][j-1]!=0 or plansza[i+2][j]!=0 or plansza[i+1][j]!=0 or plansza[i][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+3][j-1]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+3][j-1]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+3][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+1][j]
                       plansza[i+1][j]= plansza[i][j]
                       plansza[i][j]= 0


               if plansza[i+2][j]==0 and (plansza[i+1][j]!=0 or plansza[i][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+1][j]
                       plansza[i+1][j]= plansza[i][j]
                       plansza[i][j]= 0


               if plansza[i+1][j]==0 and plansza[i][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j]= plansza[i][j]
                       plansza[i][j]= 0



       if j==2:    #dla wiersza z 5 elementami
           if plansza[i+4][j-2]!=0 or plansza[i+3][j-1]!=0 or plansza[i+2][j]!=0 or plansza[i+1][j]!=0 or plansza[i][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+4][j-2]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+4][j-2]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+4][j-2]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+1][j]
                       plansza[i+1][j]= plansza[i][j]
                       plansza[i][j]= 0


           if plansza[i+3][j-1]==0 and (plansza[i+2][j]!=0 or plansza[i+1][j]!=0 or plansza[i][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+1][j]
                       plansza[i+1][j]= plansza[i][j]
                       plansza[i][j]= 0


           if plansza[i+2][j]==0 and (plansza[i+1][j]!=0 or plansza[i][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+1][j]
                       plansza[i+1][j]= plansza[i][j]
                       plansza[i][j]= 0


           if plansza[i+1][j]==0 and plansza[i][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+1][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+1][j]= plansza[i][j]
                       plansza[i][j]= 0


       if j==3 :  #dla wiersz z 4 elementami
           if plansza[i+4][j-2]!=0 or plansza[i+3][j-1]!=0 or plansza[i+2][j]!=0 or plansza[i+1][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+4][j-2]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+4][j-2]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+4][j-2]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+1][j]
                       plansza[i+1][j]= 0


               if plansza[i+3][j-1]==0 and (plansza[i+2][j]!=0 or plansza[i+1][j]!=0):   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= plansza[i+1][j]
                       plansza[i+1][j]= 0


               if plansza[i+2][j]==0 and plansza[i+1][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+2][j]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+2][j]= plansza[i+1][j]
                       plansza[i+1][j]= 0

       if j==4:   # dla wiersza z 3 elementami
           if plansza[i+4][j-2]!=0 or plansza[i+3][j-1]!=0 or plansza[i+2][j]!=0:  #sprawdza czy ktoras z kolumn jest niezerowa
               if plansza[i+4][j-2]==0:  #sprawdza czy pierwsza wartosc kolumny jest zerowa
                   while plansza[i+4][j-2]==0:  #przesuwanie aby pierwszy element nie byl zerowy
                       plansza[i+4][j-2]= plansza[i+3][j-1]
                       plansza[i+3][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= 0


               if plansza[i+3][j-1]==0 and plansza[i+2][j]!=0:   #sprawdzamy czy druga wartosc kolumny jest zerowa a pozostale niezerowe
                   while plansza[i+3][j-1]==0:  #przesuwanie aby drugi element nie byl zerowy
                       plansza[i+3][j-1]= plansza[i+2][j]
                       plansza[i+2][j]= 0

#-------------------------------------Koniec ruchu w dol-prawo------------------------------------------------


#------------------------------------Funkcja dodawania po dol-lewym ruchu------------------------------------
def dol_lewe_dodanie(plansza):
    i=0
    global punkty


    for j in range(0,5):
         if j==0:   # dla wiersza z 3 elementami
             if plansza[i+2][j]==plansza[i+1][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+1][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+2][j]**2     #dodanie punktow
                plansza[i+1][j]=plansza[i][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i][j]= 0     #przypisanie trzeciemu elementowi wartosci zerowej



             if plansza[i+1][j]==plansza[i][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j]=plansza[i+1][j]+plansza[i][j]
                punkty+=plansza[i+1][j]**2
                plansza[i][j]=0


         if j==1:   # dla wiersza z 4 elementami
             if plansza[i+3][j-1]==plansza[i+2][j]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+3][j-1]=plansza[i+3][j-1]+plansza[i+2][j]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+3][j-1]**2     #dodanie punktow
                plansza[i+2][j]=plansza[i+1][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+1][j]=plansza[i][j]
                plansza[i][j]= 0     #przypisanie czwartemu elementowi wartosci zerowej


             if plansza[i+2][j]==plansza[i+1][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+1][j]
                punkty+=plansza[i+2][j]**2
                plansza[i+1][j]=plansza[i][j]
                plansza[i][j]=0



             if plansza[i+1][j]==plansza[i][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j]=plansza[i+1][j]+plansza[i][j]
                punkty+=plansza[i+1][j]**2
                plansza[i][j]=0


         if j==2:   # dla wiersza z 5 elementami
             if plansza[i+4][j-2]==plansza[i+3][j-1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+4][j-2]=plansza[i+4][j-2]+plansza[i+3][j-1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+4][j-2]**2     #dodanie punktow
                plansza[i+3][j-1]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]=plansza[i+1][j]
                plansza[i+1][j]=plansza[i][j]
                plansza[i][j]= 0     #przypisanie piatemu elementowi wartosci zerowej



             if plansza[i+3][j-1]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j-1]=plansza[i+3][j-1]+plansza[i+2][j]
                punkty+=plansza[i+3][j-1]**2
                plansza[i+2][j]=plansza[i+1][j]
                plansza[i+1][j]=plansza[i][j]
                plansza[i][j]=0



             if plansza[i+2][j]==plansza[i+1][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+1][j]
                punkty+=plansza[i+2][j]**2
                plansza[i+1][j]=plansza[i][j]
                plansza[i][j]=0



             if plansza[i+1][j]==plansza[i][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+1][j]=plansza[i+1][j]+plansza[i][j]
                punkty+=plansza[i+1][j]**2
                plansza[i][j]=0



         if j==3:   # dla wiersza z 4 elementami
             if plansza[i+4][j-2]==plansza[i+3][j-1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+4][j-2]=plansza[i+4][j-2]+plansza[i+3][j-1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+4][j-2]**2     #dodanie punktow
                plansza[i+3][j-1]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]=plansza[i+1][j]
                plansza[i+1][j]= 0     #przypisanie czwartemu elementowi wartosci zerowej


             if plansza[i+3][j-1]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j-1]=plansza[i+3][j-1]+plansza[i+2][j]
                punkty+=plansza[i+3][j-1]**2
                plansza[i+2][j]=plansza[i+1][j]
                plansza[i+1][j]=0



             if plansza[i+2][j]==plansza[i+1][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+2][j]=plansza[i+2][j]+plansza[i+1][j]
                punkty+=plansza[i+2][j]**2
                plansza[i+1][j]=0

         if j==4:   # dla wiersza z 3 elementami
             if plansza[i+4][j-2]==plansza[i+3][j-1]: #sprawdzanie czy pierwszy element jest rowny drugiemu
                plansza[i+4][j-2]=plansza[i+4][j-2]+plansza[i+3][j-1]  #dodanie 2 elementow i zapisanie ich jako ten pierwszy
                punkty+=plansza[i+4][j-2]**2     #dodanie punktow
                plansza[i+3][j-1]=plansza[i+2][j]   # przypisanie trzeciego elementu jako drugi
                plansza[i+2][j]= 0     #przypisanie trzeciemu elementowi wartosci zerowej



             if plansza[i+3][j-1]==plansza[i+2][j]:  #sprawdzanie czy drugi element jest rowny trzeciemu
                plansza[i+3][j-1]=plansza[i+3][j-1]+plansza[i+2][j]
                punkty+=plansza[i+3][j-1]**2
                plansza[i+2][j]=0

#------------------------------------Koniec funkcji dodawania po dol-lewym ruchu----------------------------

def lista_do_listy(check,plansza):
   for i in range (0,5):
       if i==0 or i==4:
           for j in range(0,3):
               check[i][j]=plansza[i][j]
       if i==1 or i==3:
           for j in range(0,4):
               check[i][j]=plansza[i][j]
       if i==2:
           for j in range(0,5):
               check[i][j]=plansza[i][j]

def cofniecie(check,plansza):
    for i in range (0,5):
        if i==0 or i==4:
           for j in range(0,3):
               plansza[i][j]=check[i][j]
        if i==1 or i==3:
           for j in range(0,4):
               plansza[i][j]=check[i][j]
        if i==2:
           for j in range(0,5):
               plansza[i][j]=check[i][j]


def spr_ruch(plansza):
    global zmiana
    j=0
    for i in range(0,5):
        if i==0:
            if plansza[i][j]==plansza[i][j+1] or plansza[i][j+1]==plansza[i][j+2]:
                zmiana=1
            if plansza[i+2][j]==plansza[i+3][j] or plansza[i+3][j]==plansza[i+4][j]:
                zmiana=1
            if plansza[i+2][j]==plansza[i+1][j] or plansza[i+1][j]==plansza[i][j]:
                zmiana=1
        if i==1:
            if plansza[i][j]==plansza[i][j+1] or plansza[i][j+1]==plansza[i][j+2] or plansza[i][j+2]==plansza[i][j+3]:
                zmiana=1
            if plansza[i][j]==plansza[i+1][j+1] or plansza[i+1][j+1]==plansza[i+2][j+1] or plansza[i+2][j+1]==plansza[i+3][j+1]:
                zmiana=1
            if plansza[i-1][j+1]==plansza[i][j+1] or plansza[i][j+1]==plansza[i+1][j+1] or plansza[i+1][j+1]==plansza[i+2][j]:
                zmiana=1

        if i==2:
            if plansza[i][j]==plansza[i][j+1] or plansza[i][j+1]==plansza[i][j+2] or plansza[i][j+2]==plansza[i][j+3] or plansza[i][j+3]==plansza[i][j+4]:
                zmiana=1
            if plansza[i-2][j]==plansza[i-1][j+1] or plansza[i-1][j+1]==plansza[i][j+2] or plansza[i][j+2]==plansza[i+1][j+2] or plansza[i+1][j+2]==plansza[i+2][j+2]:
                zmiana=1
            if plansza[i-2][j+2]==plansza[i-1][j+2] or plansza[i-1][j+2]==plansza[i][j+2] or plansza[i][j+2]==plansza[i+1][j+1] or plansza[i+1][j+1]==plansza[i+2][j]:
                zmiana=1

        if i==3:
            if plansza[i][j]==plansza[i][j+1] or plansza[i][j+1]==plansza[i][j+2] or plansza[i][j+2]==plansza[i][j+3]:
                zmiana=1
            if plansza[i-3][j+1]==plansza[i-2][j+2] or plansza[i-2][j+2]==plansza[i-1][j+3] or plansza[i-1][j+3]==plansza[i][j+3]:
                zmiana=1
            if plansza[i-2][j+3]==plansza[i-1][j+3] or plansza[i-1][j+3]==plansza[i][j+2] or plansza[i][j+2]==plansza[i+1][j+1]:
                zmiana=1
        if i==4:
            if plansza[i][j]==plansza[i][j+1] or plansza[i][j+1]==plansza[i][j+2]:
                zmiana=1
            if plansza[i-4][j+2]==plansza[i-3][j+3] or plansza[i-3][j+3]==plansza[i-2][j+4]:
                zmiana=1
            if plansza[i-2][j+4]==plansza[i-1][j+3] or plansza[i-1][j+3]==plansza[i][j+2]:
                zmiana=1

def ist_zero(plansza):
    global zero

    zero=1
    for i in range (0,5):
       if i==0:
           for j in range(0,3):
               if plansza[i][j]==0:
                   zero=0
       if i==1 or i==3:
           for j in range(0,4):
                if plansza[i][j]==0:
                   zero=0
       if i==2:
           for j in range(0,5):
                 if plansza[i][j]==0:
                   zero=0


def sztuczna_int(plansza):
    global kierunek
    if(check==plansza):
        kierunek += 1
    else:
        kierunek=0

    lista_do_listy(check,plansza)

    ist_zero(plansza)
    if zero==0:
        if(kierunek==0):
            gora_lewo(plansza)
            gora_lewe_dodanie(plansza)
        if(kierunek==2):
            lewo(plansza)
            lewe_dodanie(plansza)
        if(kierunek==1):
            gora_prawo(plansza)
            gora_prawy_dodanie(plansza)
        if(kierunek==3):
            prawo(plansza)
            prawe_dodanie(plansza)
        if(kierunek==4):
            dol_lewo(plansza)
            dol_lewe_dodanie(plansza)
        if(kierunek==5):
            dol_prawo(plansza)
            dol_prawe_dodanie(plansza)

    if zero==1:
        if(kierunek==2):
            gora_lewo(plansza)
            gora_lewe_dodanie(plansza)
        if(kierunek==3):
            lewo(plansza)
            lewe_dodanie(plansza)
        if(kierunek==0):
            gora_prawo(plansza)
            gora_prawy_dodanie(plansza)
        if(kierunek==1):
            prawo(plansza)
            prawe_dodanie(plansza)
        if(kierunek==4):
            dol_lewo(plansza)
            dol_lewe_dodanie(plansza)
        if(kierunek==5):
            dol_prawo(plansza)
            dol_prawe_dodanie(plansza)

    time.sleep(0.00)

def wygrana(plansza):
   global wygrales
   for i in range (0,5):
       if i==0 or i==4:
           for j in range(0,3):
               if plansza[i][j]==2048:
                   wygrales=1
       if i==1 or i==3:
           for j in range(0,4):
                if plansza[i][j]==2048:
                   wygrales=1
       if i==2:
           for j in range(0,5):
                 if plansza[i][j]==2048:
                   wygrales=1

def wyswietl(plansza):
    print "\n\n"
    print "   ",plansza[0][0],"  ",plansza[0][1],"  ",plansza[0][2],"\n"
    print " ", plansza[1][0],"  ",plansza[1][1],"  ",plansza[1][2],"  ",plansza[1][3],"\n"
    print plansza[2][0],"  ",plansza[2][1],"  ",plansza[2][2],"  ",plansza[2][3],"  ",plansza[2][4],"\n"
    print " ",plansza[3][0],"  ",plansza[3][1],"  ",plansza[3][2],"  ",plansza[3][3],"\n"
    print "   ",plansza[4][0],"  ",plansza[4][1],"  ",plansza[4][2],"\n"

def wys_check(check):
    print "\n\n"
    print "   ",check[0][0],"  ",check[0][1],"  ",check[0][2],"\n"
    print " ", check[1][0],"  ",check[1][1],"  ",check[1][2],"  ",check[1][3],"\n"
    print check[2][0],"  ", check[2][1],"  ",check[2][2],"  ",check[2][3],"  ",check[2][4],"\n"
    print " ",check[3][0],"  ",check[3][1],"  ",check[3][2],"  ",check[3][3],"\n"
    print "   ",check[4][0],"  ",check[4][1],"  ",check[4][2],"\n"

def dodanie_el(check,plansza):
    global zmiana
    global kierunek
    global koniec
    global cofka
    wiersz_zerowy_indeks=[]
    kolumna_zerowy_indeks=[]
    zmiana=0

    for i in range (0,5):
        if i==0 or i==4:
            for j in range(0,3):
                if plansza[i][j]==0:
                    wiersz_zerowy_indeks.append(i)
                    kolumna_zerowy_indeks.append(j)

        if i==1 or i==3:
            for j in range(0,4):
                if plansza[i][j]==0:
                    wiersz_zerowy_indeks.append(i)
                    kolumna_zerowy_indeks.append(j)

        if i==2:
            for j in range(0,5):
                if plansza[i][j]==0:
                    wiersz_zerowy_indeks.append(i)
                    kolumna_zerowy_indeks.append(j)



    if check!=plansza:
        if len(wiersz_zerowy_indeks)>1:
            losowy_index=wiersz_zerowy_indeks.index(random.choice(wiersz_zerowy_indeks))
            wiersz_nowy=wiersz_zerowy_indeks[losowy_index]
            kolumna_nowa=kolumna_zerowy_indeks[losowy_index]
            plansza[wiersz_nowy][kolumna_nowa]= 2


        elif  len(wiersz_zerowy_indeks)==1:
            wiersz_nowy=wiersz_zerowy_indeks[0]
            kolumna_nowa=kolumna_zerowy_indeks[0]
            plansza[wiersz_nowy][kolumna_nowa]= 2

            spr_ruch(plansza)
            if zmiana==0:
                cofniecie(check,plansza)
                cofka+=1
                kierunek+=1

                if cofka>6:
                    koniec=10









class Okno(QtGui.QMainWindow,object):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('graf.ui',self)
        self.metoda()


    def metoda(self):
        self.label_22.setText(str(punkty))
        #if koniec>5:
         #   self.label_20.setText('Koniec gry')
        zeroo=QtGui.QPixmap('0.png')
        dwa=QtGui.QPixmap('2.png')
        cztery = QtGui.QPixmap('4.png')
        osiem=QtGui.QPixmap('8.png')
        szesnascie=QtGui.QPixmap('16.png')
        trzydziescidwa=QtGui.QPixmap('32.png')
        szescdziesiatcztery=QtGui.QPixmap('64.png')
        stwodwadziesciaosiem=QtGui.QPixmap('128.png')
        dwiesciepiedziesiatszesc=QtGui.QPixmap('256.png')
        piecsetdwanascie=QtGui.QPixmap('512.png')
        tysiac=QtGui.QPixmap('1024.png')
        dwatysie=QtGui.QPixmap('2048.png')
        czterytysie=QtGui.QPixmap('4096.png')
        osiemtysi=QtGui.QPixmap('8192.png')
       # myScaledPixmap = myPixmap.scaled(self.label.size(), Qt.KeepAspectRatio)
        #if koniec==10:
         #   self.label_20.setText("Koniec")
        #if koniec==0:
         #   self.label_20.setText("")

        for i in range (0,5):
            if i==0 or i==4:
                for j in range(0,3):
                    if plansza[i][j]==0:
                        numer[i][j]=zeroo
                    if plansza[i][j]==2:
                        numer[i][j]=dwa
                    if plansza[i][j]==4:
                        numer[i][j]=cztery
                    if plansza[i][j]==8:
                        numer[i][j]=osiem
                    if plansza[i][j]==16:
                        numer[i][j]=szesnascie
                    if plansza[i][j]==32:
                        numer[i][j]=trzydziescidwa
                    if plansza[i][j]==64:
                        numer[i][j]=szescdziesiatcztery
                    if plansza[i][j]==128:
                        numer[i][j]=stwodwadziesciaosiem
                    if plansza[i][j]==256:
                        numer[i][j]=dwiesciepiedziesiatszesc
                    if plansza[i][j]==512:
                        numer[i][j]=piecsetdwanascie
                    if plansza[i][j]==1024:
                        numer[i][j]=tysiac
                    if plansza[i][j]==2048:
                        numer[i][j]=dwatysie
                    if plansza[i][j]==4096:
                        numer[i][j]=czterytysie
                    if plansza[i][j]==8192:
                        numer[i][j]=osiemtysi

            if i==1 or i==3:
                for j in range(0,4):
                    if plansza[i][j]==0:
                        numer[i][j]=zeroo
                    if plansza[i][j]==2:
                        numer[i][j]=dwa
                    if plansza[i][j]==4:
                        numer[i][j]=cztery
                    if plansza[i][j]==8:
                        numer[i][j]=osiem
                    if plansza[i][j]==16:
                        numer[i][j]=szesnascie
                    if plansza[i][j]==32:
                        numer[i][j]=trzydziescidwa
                    if plansza[i][j]==64:
                        numer[i][j]=szescdziesiatcztery
                    if plansza[i][j]==128:
                        numer[i][j]=stwodwadziesciaosiem
                    if plansza[i][j]==256:
                        numer[i][j]=dwiesciepiedziesiatszesc
                    if plansza[i][j]==512:
                        numer[i][j]=piecsetdwanascie
                    if plansza[i][j]==1024:
                        numer[i][j]=tysiac
                    if plansza[i][j]==2048:
                        numer[i][j]=dwatysie
                    if plansza[i][j]==4096:
                        numer[i][j]=czterytysie
                    if plansza[i][j]==8192:
                        numer[i][j]=osiemtysi

            if i==2:
                for j in range(0,5):
                    if plansza[i][j]==0:
                        numer[i][j]=zeroo
                    if plansza[i][j]==2:
                        numer[i][j]=dwa
                    if plansza[i][j]==4:
                        numer[i][j]=cztery
                    if plansza[i][j]==8:
                        numer[i][j]=osiem
                    if plansza[i][j]==16:
                        numer[i][j]=szesnascie
                    if plansza[i][j]==32:
                        numer[i][j]=trzydziescidwa
                    if plansza[i][j]==64:
                        numer[i][j]=szescdziesiatcztery
                    if plansza[i][j]==128:
                        numer[i][j]=stwodwadziesciaosiem
                    if plansza[i][j]==256:
                        numer[i][j]=dwiesciepiedziesiatszesc
                    if plansza[i][j]==512:
                        numer[i][j]=piecsetdwanascie
                    if plansza[i][j]==1024:
                        numer[i][j]=tysiac
                    if plansza[i][j]==2048:
                        numer[i][j]=dwatysie
                    if plansza[i][j]==4096:
                        numer[i][j]=czterytysie
                    if plansza[i][j]==8192:
                        numer[i][j]=osiemtysi

        self.label.setPixmap(numer[0][0])
        self.label_2.setPixmap(numer[0][1])
        self.label_3.setPixmap(numer[0][2])
        self.label_4.setPixmap(numer[1][0])
        self.label_5.setPixmap(numer[1][1])
        self.label_6.setPixmap(numer[1][2])
        self.label_7.setPixmap(numer[1][3])
        self.label_8.setPixmap(numer[2][0])
        self.label_9.setPixmap(numer[2][1])
        self.label_10.setPixmap(numer[2][2])
        self.label_11.setPixmap(numer[2][3])
        self.label_12.setPixmap(numer[2][4])
        self.label_13.setPixmap(numer[3][0])
        self.label_14.setPixmap(numer[3][1])
        self.label_15.setPixmap(numer[3][2])
        self.label_16.setPixmap(numer[3][3])
        self.label_17.setPixmap(numer[4][0])
        self.label_18.setPixmap(numer[4][1])
        self.label_19.setPixmap(numer[4][2])




    def keyPressEvent(self,e):
                if e.key()==QtCore.Qt.Key_7:
                    lista_do_listy(check,plansza)
                    gora_lewo(plansza)
                    gora_lewe_dodanie(plansza)
                    dodanie_el(check,plansza)
                    self.metoda()

                if e.key()==QtCore.Qt.Key_9:
                    lista_do_listy(check,plansza)
                    gora_prawo(plansza)
                    gora_prawy_dodanie(plansza)
                    dodanie_el(check,plansza)
                    self.metoda()

                if e.key()==QtCore.Qt.Key_4:
                    lista_do_listy(check,plansza)
                    lewo(plansza)
                    lewe_dodanie(plansza)
                    dodanie_el(check,plansza)
                    self.metoda()

                if e.key()==QtCore.Qt.Key_6:
                    lista_do_listy(check,plansza)
                    prawo(plansza)
                    prawe_dodanie(plansza)
                    dodanie_el(check,plansza)
                    self.metoda()

                if e.key()==QtCore.Qt.Key_1:
                    lista_do_listy(check,plansza)
                    dol_lewo(plansza)
                    dol_lewe_dodanie(plansza)
                    dodanie_el(check,plansza)
                    self.metoda()

                if e.key()==QtCore.Qt.Key_3:
                    lista_do_listy(check,plansza)
                    dol_prawo(plansza)
                    dol_prawe_dodanie(plansza)
                    dodanie_el(check,plansza)
                    self.metoda()

                if e.key()==QtCore.Qt.Key_S:
                    while koniec==0:
                        sztuczna_int(plansza)
                        dodanie_el(check,plansza)
                    for j in range (0,10):
                        sztuczna_int(plansza)
                        dodanie_el(check,plansza)
                    self.metoda()

                if e.key()==QtCore.Qt.Key_A:
                    for j in range (0,2):
                        sztuczna_int(plansza)
                        dodanie_el(check,plansza)
                    self.metoda()
                    cofka=0


                if e.key()==QtCore.Qt.Key_N:
                    nowa()
                    print punkty
                    self.metoda()

if  __name__=='__main__':
    app=QApplication(sys.argv)
    okienko= Okno()
    okienko.show()
    sys.exit(app.exec_())


#while True:
    #wyswietl(plansza)


   # if ruch!="Si":
     #   ruch=raw_input("Wybiersz ruch  ")  #wybieranie ruchu przez uzytkownika
      #  if ruch=="4":
         #   lista_do_listy(check,plansza)
          #  lewo(plansza)
          #  lewe_dodanie(plansza)
       # if ruch=="6":
        #    lista_do_listy(check,plansza)
         #   prawo(plansza)
          #  prawe_dodanie(plansza)
        #if ruch=="7":
         #   lista_do_listy(check,plansza)
          #  gora_lewo(plansza)
           # gora_lewe_dodanie(plansza)
        #if ruch=="9":
         #   lista_do_listy(check,plansza)
          #  gora_prawo(plansza)
           # gora_prawy_dodanie(plansza)
        #if ruch=="3":
         #   lista_do_listy(check,plansza)
          #  dol_prawo(plansza)
           # dol_prawe_dodanie(plansza)
        #if ruch=="1":
         #   lista_do_listy(check,plansza)
          #  dol_lewo(plansza)
           # dol_lewe_dodanie(plansza)
    #if ruch=="Si":
     #   sztuczna_int(plansza)



          #  spr_ruch(plansza)
           # print kierunek
            #if zmiana==0:
             #   cofniecie(check,plansza)
              #  kierunek+=1
               # if kierunek<6:
                #   zmiana=1


           # if zmiana==0:
            #    wyswietl(plansza)
             #   break
   # else:
    #    koniec+=1

    #if koniec>5:
     #   wyswietl(plansza)
      #  break

#print "Gratulacje!! Zdobyles ", str(punkty), "punktow"
#print "\n\n"

