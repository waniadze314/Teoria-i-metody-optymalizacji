# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:05:15 2020

@author: DAMIAN
"""

import PySimpleGUI as sg
from math import *
import parser

sg.ChangeLookAndFeel('LightBlue2')

layout1 = [
    [sg.Text('PL – metoda dwufazowa simpleks', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Wprowadź funkcję do optymalizacji'), sg.Text(' ' * 14), sg.Text('Wprowadź ograniczenia')],
    [sg.Multiline((''),size=(37,1)), sg.Multiline((''),size=(37,1))],
    [sg.Text(' ' * 40), sg.Text('Wprowadź parametry optymalizacji')],
    [sg.Text('Precyzja'), sg.Text(' ' * 53), sg.Text('Ilosć iteracji')],
    [sg.Multiline((''),size=(37,1)),  sg.Multiline((''),size=(37,1))],
    [sg.Text('_' * 80)],
    [sg.Text(' ' * 40), sg.Button('Rozpocznij proces optymalizacji')], 
    [sg.Text(' ' * 50), sg.Button('Zamknij program')]]

layout2 = [
    [sg.Text('PL – metoda dwufazowa simpleks', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [ sg.Text('Komunikaty programu')],
    [sg.Multiline('Tutaj będą pojawiać się komunikaty',size=(70,8))],
    [sg.Text('Uzyskany wynik'), sg.Text(' '*42), sg.Text('Optymalizowana funckja')],
    [sg.Multiline('Tutaj pojawi się wynik optymalizacji', size=(37,1)), sg.Multiline('Tutaj wyswietli się optymalizana funckja', size=(37,1))],
    [sg.Button('Cofnij'), sg.Button('Narysuj wykres')],
    ]

window1 = sg.Window('Metoda simpleks', layout1, default_element_size=(40, 1), grab_anywhere=False)
window2 = sg.Window('Metoda simpleks', layout2, default_element_size=(40, 1), grab_anywhere=False)

while True:
    event1, values1 = window1.Read()
    if event1 == 'Rozpocznij proces optymalizacji':
        window1.Minimize()
        window2.Read()
        event2, values2 = window1.Read()
        if event2 is None or event2 == 'Zamknij program':
            break
    if event1 is None or event1 == 'Zamknij program':
        break
window1.close()
window2.close()

#sg.Popup('Title',
#         'The results of the window.',
#         'The button clicked was "{}"'.format(event),
#        'The values are', values)
# Display the window and get values
#window = sg.Window('Test',layout)
#event, values = window.read()
#window.Close()
#a = int(values[1])
#b = int(values[2])
#c = int(values[3])
#formula = values[0]
#code = parser.expr(formula).compile()
#wynik = eval(code)
#sg.Popup('Wynik',wynik, line_width=200)
