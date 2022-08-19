import os
import time
from datetime import datetime
from inspect import getfile, currentframe
from pyautogui import (alert, hotkey, press, locateCenterOnScreen, rightClick, click, moveTo, confirm)


# ------------------------------------------------------------------------------------------------------------#
# Functions
# ------------------------------------------------------------------------------------------------------------#


def obter_dia_da_semana():
    hoje = datetime.today()
    return hoje.strftime("%A")

def obter_horario():
    hora = str(datetime.now().time())
    return hora[:8]


def abrir(directory: str):
    archive = directory.split('\\')[-1]
    print('   Abrindo "{}".'.format(archive))
    os.startfile(directory)
    print('   "{}" acabou de ser aberto.'.format(archive))


def alerta(text: str, title: str):
    alerta = alert(text=text, title=title)
    if alerta == 'OK':
        return True
    else:
        return False


def confirme(text: str, buttons: list, title=None):
    dialog = confirm(text=text, title=title, buttons=buttons)
    if dialog is not None:
        for button in buttons:
            if dialog.lower() == button.lower():
                return button
    else:
        return None


def pressionar(key1, key2=None, presses: int = 1):
    for i in range(presses):
        if key2:
            hotkey(key1, key2)
        else:
            press(key1)


def esta_presente(image, loop: int = 10):
    img_name = image.split('\\')[-1]
    print('   Tentando encontrar "{}".'.format(img_name))
    for i in range(loop):
        try:
            button = locateCenterOnScreen(image, confidence=0.9)
            assert button is not None
            print('   "{}" foi encontrada. Tentativas: {}.'.format(img_name, i + 1))
            return True
        except:
            loop -= 1
        if loop == 0:
            print('   "{}" não pôde ser encontrada.'.format(img_name))
            return False


def clickar(image: str, need_click=True, right=False, time: int = 20, confidense=True, move=False, x: int = 0, y: int = 0):
    img_name = image.split('\\')[-1]
    print('   Tentando clickar em "{}"'.format(img_name))
    for i in range(time):
        try:
            if confidense:
                button = locateCenterOnScreen(image, confidence=0.9)
            else:
                button = locateCenterOnScreen(image)

            assert button is not None

            if move:
                if need_click:
                    if right:
                        rightClick(button[0] + x, button[1] + y)
                        print('   Clickou com o botão direito em "{}". Tentativas: {}.'.format(img_name, i + 1))
                    else:
                        click(button[0] + x, button[1] + y)
                        print('   Clickou em "{}". Tentativas: {}.'.format(img_name, i + 1))
                else:
                    moveTo(button[0] + x, button[1] + y)
            else:
                if need_click:
                    if right:
                        rightClick(button)
                        print('   Clickou com o botão direito em "{}". Tentativas: {}.'.format(img_name, i + 1))
                    else:
                        click(button)
                        print('   Clickou em "{}". Tentativas: {}.'.format(img_name, i + 1))

            break
        except:
            time -= 1
        if time == 0:
            print('   Infelizmente não foi possivel clickar em "{}". Tentativas: {}.'.format(img_name, time))


# ------------------------------------------------------------------------------------------------------------#
# Source
# ------------------------------------------------------------------------------------------------------------#


class OpenKali:
    def __init__(self):
        print('\n' + 'Iniciando o BOT.')

        # Variables
        self.current_dir = os.path.dirname(os.path.abspath(getfile(currentframe()))).replace(r'\source', '')
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

        if esta_presente(self.pictures['vm_focused'], 2) is True or esta_presente(self.pictures['vm_not_focused'], 2) is True:
            print('\n' + '- VIRTUAL BOX MANAGER JÁ ESTÁ ABERTO.')
        else:
            pressionar('altright', 'tab')
            if esta_presente(self.pictures['vm_logo'], 2) is True:
                clickar(self.pictures['vm_logo'], move=True, y=50)
                print('\n' + '- VIRTUAL BOX MANAGER FOI ABERTO.')
            else:
                pressionar('esc')
                abrir(self.vm_dir)
                print('\n' + '- VIRTUAL BOX MANAGER FOI ABERTO.')

    def open_whonix_gateway(self):
        print('\n' + '- TENTANDO ABRIR O WHOONIX GATEWAY.')

        for i in range(5):
            # Apertando na vm
            if esta_presente(self.pictures['gateway_not_pressed'], loop=5) is True:
                clickar(self.pictures['gateway_not_pressed'])
            else:
                assert esta_presente(self.pictures['gateway_pressed'], 5) is True, '- NÃO FOI POSSÍVEL ENCONTRAR A VIRTUAL BOX.'
                clickar(self.pictures['gateway_pressed'])

            # Apertando em start ou show
            if esta_presente(self.pictures['start_vm'], loop=1) is True:
                clickar(self.pictures['start_vm'])
                print('\n' + '- WOONIX GATEWAY FOI ABERTO.')
                break
            elif esta_presente(self.pictures['show']) is True:
                clickar(self.pictures['show'])
                print('\n' + '- WOONIX GATEWAY FOI ABERTO.')
                break
            else:
                print('   A primeira tentativa de abrir o Woonix Gateway falhou. Tentando novamente.')
                time.sleep(2)

    def window_login(self):
        print('\n' + '- ESPERANDO CONFIRMAÇÃO DO LOGIN.')

        confirmar = confirme('Já está logado?', ['Sim.'], 'Já está logado?')
        assert confirmar == 'Sim.', 'Você precisa fazer o login.'

        print('\n' + '- LOGIN CONCLUIDO.')

    def minimize_whonix_gateway_and_open_vm(self):
        # Minimize Whoonix Gateway
        print('\n' + '- TENTANDO MINIMIZAR O WHOONIX.')
        if esta_presente(self.pictures['hoonix_focused'], 2) is True:
            clickar(self.pictures['hoonix_focused'])
        else:
            if esta_presente(self.pictures['hoonix_not_focused'], 2) is True:
                clickar(self.pictures['hoonix_not_focused'])
        clickar(self.pictures['minimize'], confidense=False, move=True, x=-40)
        print('\n' + '- O WHOONIX FOI MINIMIZADO.')

        # Abrir o Virtual Box
        self.open_vm()

    def open_kali(self):
        print('\n' + '- TENTANDO ABRIR O KALI.')

        for i in range(5):
            # Apertando na vm
            if esta_presente(self.pictures['kali_not_pressed'], loop=5) is True:
                clickar(self.pictures['kali_not_pressed'])
            else:
                assert esta_presente(self.pictures['kali_pressed'], 5) is True, '- NÃO FOI POSSÍVEL ENCONTRAR A VIRTUAL BOX.'
                clickar(self.pictures['kali_pressed'])

            # Apertando em start ou show
            if esta_presente(self.pictures['start_vm'], loop=1) is True:
                clickar(self.pictures['start_vm'])
                print('\n' + '- KALI FOI ABERTO.')
                break
            elif esta_presente(self.pictures['show']) is True:
                clickar(self.pictures['show'])
                print('\n' + '- KALI JÁ ESTAVA ABERTO.')
                break
            else:
                print('   A primeira tentativa de abrir Kali falhou. Tentando novamente.')
                time.sleep(2)

    def finalizar(self):
        clock = obter_horario().split(':')
        if 5 < int(clock[0]) <= 11:
            alerta(title='Altomação finalizada.', text='A Altomação acaba de ser finalizada. '
                                                                 'Tenha um bom dia!')
        if 11 < int(clock[0]) <= 17:
            alerta(title='Altomação finalizada.', text='A Altomação acaba de ser finalizada. '
                                                                 'Tenha uma boa tarde!')
        if 17 < int(clock[0]) <= 23 or -1 < int(clock[0]) <= 5:
            alerta(title='Altomação finalizada.', text='A Altomação acaba de ser finalizada. '
                                                                 'Tenha uma boa noite!')


# ------------------------------------------------------------------------------------------------------------#
# Init
# ------------------------------------------------------------------------------------------------------------#


open_kali = OpenKali()
open_kali.start()
