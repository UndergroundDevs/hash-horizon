# -*- coding: utf-8 -*-
import PySimpleGUI as Kar


class Screen:
    def __init__(self):
        pass

    def home(self):
        home = [
            [Kar.Push()],
            [Kar.VPush(), Kar.Button('Noticias Recentes', key='001_O', size=(18, 2), font=('Fantasy', 15)),
             Kar.VPush()],
            [Kar.VPush(), Kar.Button('Noticias Passadas', key='002_O', size=(18, 2), font=('Times', 15)), Kar.VPush()],
            [Kar.VPush(), Kar.Button('Ações criptomoedas', key='003_O', size=(18, 2), font=('Times', 15)), Kar.VPush()],
            [Kar.Push()],
        ]
        return Kar.Window('Home', layout=home, auto_size_text=True, finalize=True, resizable=True,
                          icon=Kar.EMOJI_BASE64_HAPPY_LAUGH)

    def tela_nr(self):
        tela_nr = [
            [Kar.VPush(), Kar.Text('Date', key='001_O', size=(12, 1), font=('Fantasy', 15)), Kar.VPush()],
            [Kar.Push()],
            [Kar.Push()],
            [Kar.VPush(), Kar.Listbox(values=['1', '2', '3', '4', '5', '6'], size=(30, 15)), Kar.VPush()],
            [Kar.Push()],
            [Kar.VPush(), Kar.Button('Mostrar Noticia'), Kar.VPush()]
        ]
        return Kar.Window('Tela NR', layout=tela_nr)


class App:
    def __init__(self):
        self.screen = Screen()

    def start_screen(self):
        Kar.theme("DarkGreen4")
        home = self.screen.home()
        while True:
            window, event, values = Kar.read_all_windows()
            if window == home and event == Kar.WINDOW_CLOSED:
                break


if __name__ == '__main__':
    App = App()
    App.start_screen()
