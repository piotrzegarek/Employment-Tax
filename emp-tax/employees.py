import pandas as pd

class Employee():
    def __init__(self, first_name, surname, pesel, salary, contract, bonuses = {}):
        self.first_name = first_name
        self.surname = surname
        self.pesel = pesel
        self.salary = salary
        self.contract = contract
        self.bonuses = bonuses    # {"rodzaj_premii": wartosc}

    def add_bonus(self, bonus_name, amount):
        self.bonuses[bonus_name] = amount

class BazaDanych():
    def __init__(self, db_name):        # Tworzy pusta baze pracownikow
        self.db_name = db_name
        self.db = []              # Lista obiektów Pracownik
        self.imiona = [pracownik.imie for pracownik in self.baza]
        self.nazwiska = [pracownik.nazwisko for pracownik in self.baza]
        self.pesele = [pracownik.pesel for pracownik in self.baza]
        self.wynagrodzenia = [pracownik.wynagrodzenie for pracownik in self.baza]
        self.umowy = [pracownik.umowa for pracownik in self.baza]
        self.premie = [pracownik.premie for pracownik in self.baza]
        
# TO-DO: Pesel pobiera jako int i usuwa 0 z przodu, ogarnąć pobieranie premii
    def wczytaj_baze(self, file_name):        # Wczytuje baze z pliku
        if ".xlsx" in file_name:
            df = pd.read_excel(file_name, index_col=None, dtype={"pesel":"string"})
        elif ".csv" in file_name:
            df = pd.read_csv(file_name, index_col=None)

        for row in df.iterrows():
            nowy_pracownik = Employee(row[1][0], row[1][1], str(row[1][2]), row[1][3], row[1][4], row[1][5])
            self.baza.append(nowy_pracownik)    

    def zapisz_baze(self, file_name):             # Zapisuje baze do pliku
        data = [[pracownik.imie, pracownik.nazwisko, pracownik.pesel, pracownik.wynagrodzenie, pracownik.umowa, pracownik.premie] for pracownik in self.baza]
        df = pd.DataFrame(data=data, columns= ["imie", "nazwisko", "pesel", "wynagrodzenie", "umowa", "premie"])
        df.to_excel(f"{file_name}", index = False)

    def get_pracownikow(self,):         # Drukuje pracownikow z bazy (domyslnie ma zwracac)
        print("Id   Imie      Nazwisko     Pesel         Wynagrodzenie    Umowa     Premie")
        for pracownik in self.baza:
            print(f"{self.baza.index(pracownik)} {pracownik.imie} {pracownik.nazwisko} {pracownik.pesel} {pracownik.wynagrodzenie} {pracownik.umowa} {pracownik.premie}")

    def dodaj_pracownika(self, pracownik:Employee):        # Dodaje pracownika do bazy
        self.baza.append(pracownik)

    def usun_pracownika(self, imie, nazwisko):         # Usuwa pracownika z bazy
        for pracownik in self.baza:
            if pracownik.imie == imie and pracownik.nazwisko == nazwisko:
                indeks_pracownika = self.baza.index(pracownik)
                self.baza.pop(indeks_pracownika)
                print(f"Usunieto {imie} {nazwisko}")
                return
        print("Nie ma takiego pracownika")
        return

