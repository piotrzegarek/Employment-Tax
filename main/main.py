from obliczenia import Wynagrodzenia, Podatki
from pracownicy import BazaDanych, Pracownik
import pandas as pd

gmina = BazaDanych("gmina")
gmina.wczytaj_baze("dane.xlsx")
gmina.get_pracownikow()
gmina.usun_pracownika(imie="Karol", nazwisko="Misiek")
gmina.dodaj_pracownika(Pracownik("kupa","dupa","01253127341",22777,"B2B"))
gmina.get_pracownikow()
gmina.zapisz_baze("nowe_dane.xlsx")

