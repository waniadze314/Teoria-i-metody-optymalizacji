# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:52:10 2020

@author: DAMIAN
"""


import PySimpleGUI as sg
import tps
from subprocess import *
from io import StringIO  # Python3
import sys
import matplotlib.pyplot as plt
import numpy as np

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
        # Store the reference, in case you want to show things again in standard output
 
        old_stdout = sys.stdout
 
# This variable will store everything that is sent to the standard output
 
        result = StringIO()
        sys.stdout = result
        
        st.get_problem_coefficients(vals1, ograniczenia)
        tables_to_print, function_points, optimal_value = st.calculate_table()
        
        # Redirect again the std output to screen
 
        sys.stdout = old_stdout
 
# Then, get the stdout like a string and process it!
 
        result_string = result.getvalue()
  
        #print(function_points)
        #print(optimal_value)
        #print(tables_to_print)

        win2_active = True
        layout2 = [ 
        [sg.Text('PL – metoda dwufazowa simpleks', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [ sg.Text('Tablice simplexowe')],
        [sg.Multiline(key = 'tablice_simp',size=(70,8), disabled = True, autoscroll = True )],
        [sg.Text('Rozwiazanie optymalne'), sg.Text(' '*42), sg.Text('Punkty funkcji')],
        [sg.Multiline(key='optymalne', size=(37,1)), sg.Multiline(key = 'pkt_funkcji', size=(37,1))],
        [sg.Button('Cofnij'), sg.Button('Narysuj wykres')],
        ]
        win2 = sg.Window('Metoda simpleks - Wyniki obliczeń').Layout(layout2)

    if win2_active:
        ev2, vals2 = win2.Read(timeout=100)
        win2['tablice_simp'].update(result_string)
        win2['optymalne'].update(optimal_value)
        win2['pkt_funkcji'].update(function_points)
        #print(function_points[2][0], function_points[2][1])
        if ev2 is None or ev2 == 'Cofnij':
            win2.Close()
            win2_active = False
        if ev2 is None or ev2 == 'Narysuj wykres':
            
            if ograniczenia == 1:
                zasieg = int(vals1[11])
                #print(zasieg)
                x1 = np.linspace(0, zasieg)
                plt.plot(x1, (int(vals1[11]) - int(vals1[5]) * x1)/int(vals1[6]))
                plt.plot(0,0, 'co', label = '0')
               #plt.plot(function_points[0][0], function_points[0][1], 'bo', label = '1')
            if ograniczenia == 2:
                zasieg = max(int(vals1[11]), int(vals1[18]))
                #print(zasieg)
                x1 = np.linspace(0, zasieg)
                plt.plot(x1, (int(vals1[11]) - int(vals1[5]) * x1)/int(vals1[6]))
                plt.plot(x1, (int(vals1[18]) - int(vals1[12])*x1)/int(vals1[13]))
                plt.plot(0,0, 'co', label = '0')
                #plt.plot(function_points[0][0], function_points[0][1], 'bo', label = '1')
                #plt.plot(function_points[1][0], function_points[1][1], 'go', label ='2')
            if ograniczenia == 3:
                zasieg = max(int(vals1[11]), int(vals1[18]), int(vals1[25]))
                #print(zasieg)
                x1 = np.linspace(0, zasieg)
                plt.plot(x1, (int(vals1[11]) - int(vals1[5]) * x1)/int(vals1[6]))
                plt.plot(x1, (int(vals1[18]) - int(vals1[12])*x1)/int(vals1[13]))
                plt.plot(x1, (int(vals1[25]) - int(vals1[19])*x1)/int(vals1[20]))
                plt.plot(0,0, 'co', label = '0')
                plt.plot(function_points[0][0], function_points[0][1], 'bo', label = '1')
                plt.plot(function_points[1][0], function_points[1][1], 'go', label = '2')
                plt.plot(function_points[2][0], function_points[2][1], 'ko', label = '3')
            if ograniczenia == 4:
                zasieg = max(int(vals1[11]), int(vals1[18]), int(vals1[25]))
                #print(zasieg)
                x1 = np.linspace(0, zasieg)
                plt.plot(x1, (int(vals1[11]) - int(vals1[5]) * x1)/int(vals1[6]))
                plt.plot(x1, (int(vals1[18]) - int(vals1[12])*x1)/int(vals1[13]))
                plt.plot(x1, (int(vals1[25]) - int(vals1[19])*x1)/int(vals1[20]))
                plt.plot(x1, (int(vals1[32]) - int(vals1[26])*x1)/int(vals1[27]))
                plt.plot(0,0, 'co', label = '0')
                plt.plot(function_points[0][0], function_points[0][1], 'bo', label = '1')
                plt.plot(function_points[1][0], function_points[1][1], 'go', label = '2')
                plt.plot(function_points[2][0], function_points[2][1], 'ko', label = '3')
                #plt.plot(function_points[3][0], function_points[3][1], 'ro', label = '4')
            if ograniczenia == 5:
                zasieg = max(int(vals1[11]), int(vals1[18]), int(vals1[25]))
                #print(zasieg)
                x1 = np.linspace(0, zasieg)
                plt.plot(x1, (int(vals1[11]) - int(vals1[5]) * x1)/int(vals1[6]))
                plt.plot(x1, (int(vals1[18]) - int(vals1[12])*x1)/int(vals1[13]))
                plt.plot(x1, (int(vals1[25]) - int(vals1[19])*x1)/int(vals1[20]))
                plt.plot(x1, (int(vals1[32]) - int(vals1[26])*x1)/int(vals1[27]))
                plt.plot(x1, (int(vals1[39]) - int(vals1[33])*x1)/int(vals1[34]))
                plt.plot(0,0, 'co',  label = '0')
                plt.plot(function_points[0][0], function_points[0][1], 'bo', label = '1')
                plt.plot(function_points[1][0], function_points[1][1], 'go', label = '2')
                plt.plot(function_points[2][0], function_points[2][1], 'ko', label = '3')
                #plt.plot(function_points[3][0], function_points[3][1], 'ro', label = '4')
                #plt.plot(function_points[4][0], function_points[4][1], 'mo', label = '5')

            plt.ylim([0, zasieg])
            plt.xticks(np.arange(0, zasieg))
            plt.yticks(np.arange(0, zasieg))
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')
            plt.xlabel('x1')
            plt.ylabel('x2')
            plt.legend()
            plt.show()
win1.close()


