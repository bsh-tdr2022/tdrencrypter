import PySimpleGUI as gui
from encrypter import encriptar
from decrypter import desencriptar
from sender import send

gui.theme ('SystemDefault')

layout = [ [gui.Text('Encriptador i desencriptador de missatges')],
           [gui.Text('Escrigui el missatge'), gui.InputText(key='-INPUT-', size=(85, 10))], 
           [gui.Text('En cas de voler encriptar, escrigui la clau'), gui.InputText(key = '-INPUT2-', size = (85, 10))],
           [gui.Text(size=(40,1), key='-OUTPUT-')],
           [gui.Button('Encriptar'), gui.Button('Desencriptar'), gui.Button('Encriptar i enviar')],
           [gui.Multiline(font='Courier 10', key='-EXTRA-', size=(85,10))],
           [gui.Button('Tancar')] ]

screen = gui.Window ('TDR', layout)

#Codi de la pantalla d'enviament
def enviament(correu):
    send_layout = [ [gui.Text('Encriptador i desencriptador de missatges')],
           [gui.Text('Escrigui la direcció des de la qual envia el missatge'), gui.InputText(key='-INPUT3-', size=(85, 10))], 
           [gui.Text('Escrigui a on vol enviar el missatge'), gui.InputText(key = '-INPUT4-', size = (85, 10))],
           [gui.Text(size=(40,1), key='-OUTPUT2-')],
           [gui.Button('Enviar')],
           [gui.Multiline(font='Courier 10', key='-EXTRA2-', size=(85,10))],
           [gui.Button('Tancar')] ]
    
    window = gui.Window ('Enviament', send_layout)

    while True:
        event, values = window.Read()
        if event == gui.WIN_CLOSED or event == 'Tancar':
            break

        if event == 'Enviar':
            persona1 = values ['-INPUT3-']
            persona2 = values ['-INPUT4-']
            send (persona1, persona2, correu)

            try:
                window['-EXTRA2-'].update("Missatge enviat amb èxit!")
            except:
                window['-EXTRA2-'].update("Ha hagut un error")

    window.close()


while True:
    event, values = screen.Read()
    if event == gui.WIN_CLOSED or event == 'Tancar':
        break

    if event == 'Encriptar':
        missatge = values ['-INPUT-']
        shift = int(values ['-INPUT2-'])
        missatgencriptat = encriptar(missatge, shift)
        screen['-EXTRA-'].update(missatgencriptat)
    
    if event == 'Desencriptar':
        text = values ['-INPUT-']
        missatgedesencriptat = desencriptar (text)        
        screen['-EXTRA-'].update(missatgedesencriptat)
    
    if event == 'Encriptar i enviar':
        text = values ['-INPUT-']
        shift = int(values['-INPUT2-'])
        textencriptat = encriptar (text, shift)
        enviament (textencriptat)

screen.close()
