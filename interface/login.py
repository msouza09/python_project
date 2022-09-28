from PySimpleGUI import PySimpleGUI as sg 
from cadastro import*

# Layout 
sg.theme('Reddit')
layout = [
    [sg.Text('Login'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Button('Logar')]
]
# Janela 
janela = sg.Window('Tela de Login', layout)
# Ler os eventos 
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['login'] and valores['senha']:
            print('Bem vindo')
        elif valores['senha'] and valores['senha']:
            print('Senha ou login incorreto')