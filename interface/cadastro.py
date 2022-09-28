from PySimpleGUI import PySimpleGUI as sg 

# Layout 
sg.theme('LightBrown4')
layout = [
    [sg.Text('Login'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Button('Cadastrar')]
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