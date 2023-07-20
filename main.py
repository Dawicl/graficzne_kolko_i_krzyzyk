from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

macierz_przyciskow = [["pierwszy", "drugi", "trzeci"],
                      ["czwarty", "piaty", "szosty"],
                      ["siodmy", "osmy", "dziewiaty"]]

score_O = 0
score_X = 0

Builder.load_file('grafika.kv')
class main_window(Widget):
    def ruch_gracza(self, widget):
        if widget.text != " ":
            self.ids.temp_ekran.text = "To pole jest zajęte!"
            return
        else:
            self.ids.temp_ekran.text = " "

        if self.ids.wyswietlacz.text == "Gracz: O":
            widget.text = "O"
        else:
            widget.text = "X"
        self.sprawdzanie()
        if self.ids.wyswietlacz.text == "Gracz: X":
            self.ids.wyswietlacz.text = "Gracz: O"
        elif self.ids.wyswietlacz.text == "Gracz: O":
            self.ids.wyswietlacz.text = "Gracz: X"

    def sprawdzanie(self):
        global score_O
        global score_X
        for i in range(3):
            if self.ids[macierz_przyciskow[i][0]].text == self.ids[macierz_przyciskow[i][1]].text and self.ids[macierz_przyciskow[i][1]].text == self.ids[macierz_przyciskow[i][2]].text \
                and self.ids[macierz_przyciskow[i][0]].text != " ":
                self.ids.temp_ekran.text = "Koniec gry!"
                self.blokada_przyciskow()
                if self.ids[macierz_przyciskow[i][0]].text == "X":
                    score_X += 1
                    final_X = "Gracz: X - " + str(score_X)
                    self.ids.wynik_X.text = final_X
                else:
                    score_O += 1
                    final_O = "Gracz: O - " + str(score_O)
                    self.ids.wynik_O.text = final_O

        for i in range(3):
            if self.ids[macierz_przyciskow[0][i]].text == self.ids[macierz_przyciskow[1][i]].text and self.ids[macierz_przyciskow[1][i]].text == self.ids[macierz_przyciskow[2][i]].text \
                and self.ids[macierz_przyciskow[0][i]].text != " ":
                self.ids.temp_ekran.text = "Koniec gry!"
                self.blokada_przyciskow()
                if self.ids[macierz_przyciskow[0][i]].text == "X":
                    score_X += 1
                    final_X = "Gracz: X - " + str(score_X)
                    self.ids.wynik_X.text = final_X
                else:
                    score_O += 1
                    final_O = "Gracz: O - " + str(score_O)
                    self.ids.wynik_O.text = final_O

        diagonal_1 = [self.ids.pierwszy.text, self.ids.piaty.text, self.ids.dziewiaty.text]
        if diagonal_1[0] == diagonal_1[1] and diagonal_1[1] == diagonal_1[2] and diagonal_1[0] != " ":
            self.ids.temp_ekran.text = "Koniec gry!"
            self.blokada_przyciskow()
            if diagonal_1[0] == "X":
                score_X += 1
                final_X = "Gracz: X - " + str(score_X)
                self.ids.wynik_X.text = final_X
            else:
                score_O += 1
                final_O = "Gracz: O - " + str(score_O)
                self.ids.wynik_O.text = final_O

        diagonal_2 = [self.ids.siodmy.text, self.ids.piaty.text, self.ids.trzeci.text]
        if diagonal_2[0] == diagonal_2[1] and diagonal_2[1] == diagonal_2[2] and diagonal_2[0] != " ":
            self.ids.temp_ekran.text = "Koniec gry!"
            self.blokada_przyciskow()
            if diagonal_2[0] == "X":
                score_X += 1
                final_X = "Gracz: X - " + str(score_X)
                self.ids.wynik_X.text = final_X
            else:
                score_O += 1
                final_O = "Gracz: O - " + str(score_O)
                self.ids.wynik_O.text = final_O

    def blokada_przyciskow(self):
        for wiersz in macierz_przyciskow:
            for elem in wiersz:
                self.ids[elem].disabled = True

    def reset(self):
        for wiersz in macierz_przyciskow:
            for elem in wiersz:
                self.ids[elem].disabled = False
                self.ids[elem].text = " "
                self.ids.temp_ekran.text = " "
                self.ids.wyswietlacz.text = "Gracz: O"


class MyApp(App):
    def build(self):
        return main_window()

aplikacja = MyApp()
aplikacja.run()