import pyautogui as pg
import PySimpleGUI as sg
import keyboard
import time

def createButton(buttonColor):
    element = [sg.B("", size=(2,1), button_color=buttonColor, border_width = 1, key = "buttonPressed")]
    return element

def RGB2HEX(color):
    return "#%02x%02x%02x" % color

sg.theme('Default 1')

layout = [[sg.Column([createButton("#000000")], key = "createButton")],
          [sg.T("RGB = ", key = "updateColor")]]
window = sg.Window('ColorPicker', layout, return_keyboard_events=True, size = (300, 200))

while True:
    event, values = window.read(timeout = 50)
    if event == sg.WIN_CLOSED:
        break

    if keyboard.is_pressed("enter"):
        window.extend_layout(window["createButton"], [createButton(RGB2HEX(color))])
        pg.keyUp("enter")

    x, y = pg.position()
    color = pg.pixel(x, y)
    window["updateColor"].update("RGB = " + str(color))

window.close()