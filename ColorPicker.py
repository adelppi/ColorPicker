import pyautogui as pg
import PySimpleGUI as sg

sg.theme('Default 1')
layout = [[sg.Text('RGB = ', key = "-ACT-")]]

window = sg.Window('sample', layout, size = (300, 200))

while True:
    event, values = window.read(timeout = 50)
    if event == sg.WIN_CLOSED:
        break
    x, y = pg.position()
    color = pg.pixel(x, y)
    window["-ACT-"].update(color)

window.close()