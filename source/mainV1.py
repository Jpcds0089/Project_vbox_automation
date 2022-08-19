import os
import time
import inspect
from scripts import os as OS
from colorama import Fore, Style
from scripts import get_week_day
from scripts import pyautogui as PyAutogui


# ------------------------------------------------------------------------------------------------------------#
# Source
# ------------------------------------------------------------------------------------------------------------#


class OpenKali:
    def __init__(self):
        print('\n' + 'Iniciando o BOT.')

        # Variables
        self.current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))).replace(r'\source', '')
        self.vm_dir = r'C:\Program Files\Oracle\VirtualBox\VirtualBox.exe'
        self.pictures_dir = r'{}\assets\pictures'.format(self.current_dir)

        # Picutes
        self.pictures = {'show': r'{}\show.png'.format(self.pictures_dir),
                         'vm_logo': r'{}\vm_logo.png'.format(self.pictures_dir),
                         'start_vm': r'{}\start_vm.png'.format(self.pictures_dir),
                         'minimize': r'{}\minimize_vm.png'.format(self.pictures_dir),
                         'vm_focused': r'{}\vm_focused.png'.format(self.pictures_dir),
                         'host_login': r'{}\host_login.png'.format(self.pictures_dir),
                         'kali_pressed': r'{}\kali_pressed.png'.format(self.pictures_dir),
                         'vm_not_focused': r'{}\vm_not_focused.png'.format(self.pictures_dir),
                         'hoonix_focused': r'{}\gateway_logo_focused.png'.format(self.pictures_dir),
                         'gateway_pressed': r'{}\gateway_pressed.png'.format(self.pictures_dir),
                         'kali_not_pressed': r'{}\kali_not_pressed.png'.format(self.pictures_dir),
                         'hoonix_not_focused': r'{}\gateway_logo_not_focused.png'.format(self.pictures_dir),
                         'gateway_not_pressed': r'{}\gateway_not_pressed.png'.format(self.pictures_dir)}

    def start(self):
        self.open_vm()
        self.open_whonix_gateway()
        self.window_login()
        self.minimize_whonix_gateway_and_open_vm()
        self.open_kali()
        self.window_login()
        self.finalizar()

    def open_vm(self):
        print('\n' + '- TENTANDO ABRIR O VIRTUAL BOX MANAGER.')

        if PyAutogui.esta_presente(self.pictures['vm_focused'], 2) is True or PyAutogui.esta_presente(self.pictures['vm_not_focused'], 2) is True:
            print(Fore.GREEN + '\n' + '- VIRTUAL BOX MANAGER JÁ ESTÁ ABERTO.' + Style.RESET_ALL)
        else:
            PyAutogui.pressionar('altright', 'tab')
            if PyAutogui.esta_presente(self.pictures['vm_logo'], 2) is True:
                PyAutogui.clickar(self.pictures['vm_logo'], move=True, y=50)
                print(Fore.GREEN + '\n' + '- VIRTUAL BOX MANAGER FOI ABERTO.' + Style.RESET_ALL)
            else:
                PyAutogui.pressionar('esc')
                OS.abrir(self.vm_dir)
                print(Fore.GREEN + '\n' + '- VIRTUAL BOX MANAGER FOI ABERTO.' + Style.RESET_ALL)

    def open_whonix_gateway(self):
        print('\n' + '- TENTANDO ABRIR O WHOONIX GATEWAY.')

        for i in range(5):
            # Apertando na vm
            if PyAutogui.esta_presente(self.pictures['gateway_not_pressed'], loop=5) is True:
                PyAutogui.clickar(self.pictures['gateway_not_pressed'])
            else:
                assert PyAutogui.esta_presente(self.pictures['gateway_pressed'], 5) is True, Fore.RED + '- NÃO FOI POSSÍVEL ENCONTRAR A VIRTUAL BOX.' + Style.RESET_ALL
                PyAutogui.clickar(self.pictures['gateway_pressed'])

            # Apertando em start ou show
            if PyAutogui.esta_presente(self.pictures['start_vm'], loop=1) is True:
                PyAutogui.clickar(self.pictures['start_vm'])
                print(Fore.GREEN + '\n' + '- WOONIX GATEWAY FOI ABERTO.' + Style.RESET_ALL)
                break
            elif PyAutogui.esta_presente(self.pictures['show']) is True:
                PyAutogui.clickar(self.pictures['show'])
                print(Fore.GREEN + '\n' + '- WOONIX GATEWAY FOI ABERTO.' + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + '   A primeira tentativa de abrir o Woonix Gateway falhou. Tentando novamente.' + Style.RESET_ALL)
                time.sleep(2)

    def window_login(self):
        print('\n' + '- ESPERANDO CONFIRMAÇÃO DO LOGIN.')

        confirm = PyAutogui.confirm('Já está logado?',
                                    ['Sim.'],
                                    'Já está logado?')
        assert confirm == 'Sim.', Fore.RED + 'Você precisa fazer o login.' + Style.RESET_ALL

        print(Fore.GREEN + '\n' + '- LOGIN CONCLUIDO.' + Style.RESET_ALL)

    def minimize_whonix_gateway_and_open_vm(self):
        # Minimize Whoonix Gateway
        print('\n' + '- TENTANDO MINIMIZAR O WHOONIX.')
        if PyAutogui.esta_presente(self.pictures['hoonix_focused'], 2) is True:
            PyAutogui.clickar(self.pictures['hoonix_focused'])
        else:
            if PyAutogui.esta_presente(self.pictures['hoonix_not_focused'], 2) is True:
                PyAutogui.clickar(self.pictures['hoonix_not_focused'])
        PyAutogui.clickar(self.pictures['minimize'], confidense=False, move=True, x=-40)
        print(Fore.GREEN + '\n' + '- O WHOONIX FOI MINIMIZADO.' + Style.RESET_ALL)

        # Abrir o Virtual Box
        self.open_vm()

    def open_kali(self):
        print('\n' + '- TENTANDO ABRIR O KALI.')

        for i in range(5):
            # Apertando na vm
            if PyAutogui.esta_presente(self.pictures['kali_not_pressed'], loop=5) is True:
                PyAutogui.clickar(self.pictures['kali_not_pressed'])
            else:
                assert PyAutogui.esta_presente(self.pictures['kali_pressed'], 5) is True, Fore.RED + '- NÃO FOI POSSÍVEL ENCONTRAR A VIRTUAL BOX.' + Style.RESET_ALL
                PyAutogui.clickar(self.pictures['kali_pressed'])

            # Apertando em start ou show
            if PyAutogui.esta_presente(self.pictures['start_vm'], loop=1) is True:
                PyAutogui.clickar(self.pictures['start_vm'])
                print(Fore.GREEN + '\n' + '- KALI FOI ABERTO.' + Style.RESET_ALL)
                break
            elif PyAutogui.esta_presente(self.pictures['show']) is True:
                PyAutogui.clickar(self.pictures['show'])
                print(Fore.GREEN + '\n' + '- KALI JÁ ESTAVA ABERTO.' + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + '   A primeira tentativa de abrir Kali falhou. Tentando novamente.' + Style.RESET_ALL)
                time.sleep(2)

    def finalizar(self):
        clock = get_week_day.obter_horario().split(':')
        if 5 < int(clock[0]) <= 11:
            PyAutogui.alerta(title='Altomação finalizada.', text='A Altomação acaba de ser finalizada. '
                                                                 'Tenha um bom dia!')
        if 11 < int(clock[0]) <= 17:
            PyAutogui.alerta(title='Altomação finalizada.', text='A Altomação acaba de ser finalizada. '
                                                                 'Tenha uma boa tarde!')
        if 17 < int(clock[0]) <= 23 or -1 < int(clock[0]) <= 5:
            PyAutogui.alerta(title='Altomação finalizada.', text='A Altomação acaba de ser finalizada. '
                                                                 'Tenha uma boa noite!')


# ------------------------------------------------------------------------------------------------------------#
# Init
# ------------------------------------------------------------------------------------------------------------#


open_kali = OpenKali()
open_kali.start()
