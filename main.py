import PySimpleGUI as Kar


class Screen:
    def __init__(self):
        pass

    def modalidade(self):
        home = [
            [Kar.Push()],
            [
                Kar.VPush(),
                Kar.Button('Modadalidade Earn', key='001_O', size=(18, 2), font=('Times', 15)),
                Kar.VPush()
            ],
            [Kar.VPush(), Kar.Button('Modalidade Trades Manual', key='002_O', size=(18, 2), font=('Times', 15)),
                Kar.VPush()],
            [Kar.VPush(), Kar.Button('Modalidade Bots Trades', key='003_O', size=(18, 2), font=('Times', 15)),
             Kar.VPush()],
            [Kar.Push()]
        ]
        return Kar.Window('Home', home, auto_size_text=True, finalize=True, resizable=True,
                          icon=Kar.EMOJI_BASE64_HAPPY_LAUGH)

    def inicial(self):
        Iniit = [
            [Kar.Push()],
            [Kar.VPush(),Kar.Text('Escolha a forma de Operação do Bot: ', key='001_O',size=(12,1), font=('Times',15)),Kar.VPush()],
            [Kar.VPush(),Kar.Button('Manual', key='004_0', size=(18, 2), font=('Times', 15)),Kar.VPush()],
            [Kar.VPush(),Kar.Button('Automatico', key='005_O', size=(18, 2), font=('Times', 15)),Kar.VPush(),],
            [Kar.Push()]
        ]
        return Kar.Window('Home', Iniit, auto_size_text=True, finalize=True, resizable=True,
                          icon=Kar.EMOJI_BASE64_HAPPY_LAUGH, location=(0, 0))

    def provide_date_value(self):
        screen = [
            [Kar.Push()],
            [Kar.Push(),
             Kar.Text('Escolha o valor do investimento', key='001_O', auto_size_text=True, font=('Robot', 15)),
             Kar.Push()],
            [Kar.Push()],
        ]
        return Kar.Window('Home', layout=screen, finalize=True, auto_size_text=True, resizable=True, size=(800, 600),
                          location=(0, 0))
#
class start:
    def __init__(self):
        self.screen = Screen()
        self.home = self.screen.inicial()
        # self.provide_date_value = self.screen.provide_date_value()

    def screens(self):
        Kar.theme("DarkGreen4")
        while True:
            window, events, values = Kar.read_all_windows()
            if window == self.home and events == Kar.WIN_CLOSED:
                break
            if window == self.home and events == '004_0':
                self.home.hide()
                self.provide_date_value = self.screen.provide_date_value()
                print('Hello World')


if __name__ == '__main__':
    a = start()
    a.screens()
