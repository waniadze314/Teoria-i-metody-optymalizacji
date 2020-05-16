# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:52:10 2020

@author: DAMIAN
"""


import PySimpleGUI as sg
import tps

# Design pattern 2 - First window does remain active
st = tps.two_phase_simplex()
sg.ChangeLookAndFeel('LightBlue2')
ograniczenia = 1
layout = [
    [sg.Text('PL – metoda dwufazowa simpleks', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text(' '*25), sg.Text('Wprowadź funkcję do maksymalizacji', font=("Helvetica",15))],
    [sg.Text('')],
    [sg.Input((''),size=(5,1)), sg.Text('x1'), sg.Text('+'), sg.Input((''),size=(5,1)), sg.Text('x2'), sg.Text('+'),
     sg.Input((''),size=(5,1)), sg.Text('x3'), sg.Text('+'), sg.Input((''),size=(5,1)), sg.Text('x4'), sg.Text('+'),
     sg.Input((''),size=(5,1)), sg.Text('x5')],
    [sg.Text('')],
    [sg.Text(' '*35), sg.Text('Wprowadź ograniczenia', font=("Helvetica",15))],
    [sg.Text('')],
    [sg.Text('x1'),sg.Text(' '*11), sg.Text('x2'),sg.Text(' '*11), sg.Text('x3'),sg.Text(' '*10), sg.Text('x4'), sg.Text(' '*10),sg.Text('x5'), sg.Text(' '*12), sg.Text('Znak') ],
    *[[sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.InputCombo(['≤', '≥'], size=(5,1)),
     sg.Input('',size=(10,1))] for i in range(ograniczenia)],
    [sg.Text('_' * 75)],
    [sg.Text(' '*40), sg.Button(('Dodaj nowe ograniczenie'), size = (25,1))],
    [sg.Text(' '*40), sg.Button(('Usun ograniczenie'), size = (25,1))],
    [sg.Text(' ' * 40), sg.Button(('Rozpocznij proces optymalizacji'), size=(25,1))], 
    [sg.Text(' ' * 40), sg.Button(('Zamknij program'), size=(25,1))]]



win1 = sg.Window('Window 1').Layout(layout)
win2_active=False
while True:
    ev1, vals1 = win1.Read(timeout=100)
    
    if ev1 is None or ev1 == 'Zamknij program':
        break
    
    if ev1 == 'Dodaj nowe ograniczenie' and not win2_active:
        ograniczenia += 1
        
        layout = [
    [sg.Text('PL – metoda dwufazowa simpleks', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text(' '*25), sg.Text('Wprowadź funkcję do maksymalizacji', font=("Helvetica",15))],
    [sg.Text('')],
    [sg.Input((''),size=(5,1)), sg.Text('x1'), sg.Text('+'), sg.Input((''),size=(5,1)), sg.Text('x2'), sg.Text('+'),
     sg.Input((''),size=(5,1)), sg.Text('x3'), sg.Text('+'), sg.Input((''),size=(5,1)), sg.Text('x4'), sg.Text('+'),
     sg.Input((''),size=(5,1)), sg.Text('x5')],
    [sg.Text('')],
    [sg.Text(' '*35), sg.Text('Wprowadź ograniczenia', font=("Helvetica",15))],
    [sg.Text('')],
    [sg.Text('x1'),sg.Text(' '*11), sg.Text('x2'),sg.Text(' '*11), sg.Text('x3'),sg.Text(' '*10), sg.Text('x4'), sg.Text(' '*10),sg.Text('x5'), sg.Text(' '*12), sg.Text('Znak') ],
    *[[sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.InputCombo(['≤', '≥'], size=(5,1)),
     sg.Input('',size=(10,1))] for i in range(ograniczenia)],
    [sg.Text('_' * 75)],
    [sg.Text(' '*40), sg.Button(('Dodaj nowe ograniczenie'), size = (25,1))],
    [sg.Text(' '*40), sg.Button(('Usun ograniczenie'), size = (25,1))],
    [sg.Text(' ' * 40), sg.Button(('Rozpocznij proces optymalizacji'), size=(25,1))], 
    [sg.Text(' ' * 40), sg.Button(('Zamknij program'), size=(25,1))]]
        
        win12 = sg.Window('Metoda simpleks').Layout(layout)
        win1.Close()
        win1 = win12

    if ev1 == 'Usun ograniczenie' and not win2_active:
        ograniczenia -= 1
        
        layout = [
    [sg.Text('PL – metoda dwufazowa simpleks', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text(' '*25), sg.Text('Wprowadź funkcję do maksymalizacji', font=("Helvetica",15))],
    [sg.Text('')],
    [sg.Input((''),size=(5,1)), sg.Text('x1'), sg.Text('+'), sg.Input((''),size=(5,1)), sg.Text('x2'), sg.Text('+'),
     sg.Input((''),size=(5,1)), sg.Text('x3'), sg.Text('+'), sg.Input((''),size=(5,1)), sg.Text('x4'), sg.Text('+'),
     sg.Input((''),size=(5,1)), sg.Text('x5')],
    [sg.Text('')],
    [sg.Text(' '*35), sg.Text('Wprowadź ograniczenia', font=("Helvetica",15))],
    [sg.Text('')],
    [sg.Text('x1'),sg.Text(' '*11), sg.Text('x2'),sg.Text(' '*11), sg.Text('x3'),sg.Text(' '*10), sg.Text('x4'), sg.Text(' '*10),sg.Text('x5'), sg.Text(' '*12), sg.Text('Znak') ],
    *[[sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.Input((''),size=(10,1)), sg.InputCombo(['≤', '≥'], size=(5,1)),
     sg.Input('',size=(10,1))] for i in range(ograniczenia)],
    [sg.Text('_' * 75)],
    [sg.Text(' '*40), sg.Button(('Dodaj nowe ograniczenie'), size = (25,1))],
    [sg.Text(' '*40), sg.Button(('Usun ograniczenie'), size = (25,1))],
    [sg.Text(' ' * 40), sg.Button(('Rozpocznij proces optymalizacji'), size=(25,1))], 
    [sg.Text(' ' * 40), sg.Button(('Zamknij program'), size=(25,1))]]
        
        win123 = sg.Window('Metoda simpleks - wprowadzanie danych').Layout(layout)
        win1.Close()
        win1 = win123

    if ev1 == 'Rozpocznij proces optymalizacji' and not win2_active:
        # get coefs
        st.get_problem_coefficients(vals1, ograniczenia)
        tables_to_print, function_points, optimal_value = st.calculate_table()
        print(function_points)
        print(optimal_value)
        print(tables_to_print)

        win2_active = True
        layout2 = [ 
        [sg.Text('PL – metoda dwufazowa simpleks', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [ sg.Text('Tablice simplexowe')],
        [sg.Multiline('Tutaj zostana wyswietlone kolejne kroki algorytmu',size=(70,8))],
        [sg.Text('Rozwiazanie optymalne'), sg.Text(' '*42), sg.Text('Optymalizowana funckja')],
        [sg.Multiline('Tutaj pojawi się wynik optymalizacji', size=(37,1)), sg.Multiline('Tutaj wyswietli się optymalizowana funckja', size=(37,1))],
        [sg.Button('Cofnij'), sg.Button('Narysuj wykres')],
        ]
        win2 = sg.Window('Metoda simpleks - Wyniki obliczeń').Layout(layout2)

    if win2_active:
        ev2, vals2 = win2.Read(timeout=100)
        if ev2 is None or ev2 == 'Cofnij':
            win2.Close()
            win2_active = False
win1.close()
