import Chatbot
import PySimpleGUI as psg

psg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [psg.Text("Hi, Im chatBot!")],
            [psg.Text('Ask me anything: '), psg.Input(key="K")],
            [psg.Text(key="OUT")],
            [psg.OK(), psg.Exit()]
              ]

# Create the Window
window = psg.Window('ChatBot', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    out = values["K"]
    out = Chatbot.vastus(out)
    window["OUT"].update(out)
    #psg.popup_ok(Chatbot.vastus(vastus), title="Response")

window.close()


