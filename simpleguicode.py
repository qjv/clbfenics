import PySimpleGUIQt as sg
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


def kWindow(valores):
    line = "[sg.In('{0}', size=(20,1), key='-temp{id}-', visible={2}, justification='right'), sg.In('{1}', size=(20,1), key='-k{id}-', visible={2}, justification='right'), sg.Button('+', size=(5,1), key='+{id}', visible={3})]"
    layout = [[sg.T('Temperature [°C]', size=(20,1), justification='center'), sg.T('k [W/(m·K)]', size=(20,1), justification='center')]]
    layout.append([sg.Button('Load', size=(20,1)), sg.Button('Cancel', size=(20,1))])
    for i in range(0, 10):
        try:
            if valores is None:
                layout.insert(-1, eval(line.format('','','True','True',id=i)))
                valores = np.array([['','']])
            elif i+1 == valores.shape[0]:
                layout.insert(-1, eval(line.format(valores[i,0],valores[i,1],'True','True',id=i)))
            else:
                layout.insert(-1, eval(line.format(valores[i,0],valores[i,1],'True','False',id=i)))
        except: layout.insert(-1, eval(line.format('','','False','False',id=i)))
    window = sg.Window('Thermal Conductivity', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit', 'Cancel'):
            window.close()
            break
        if "Load" in event:
            try:
                hr, t = [], []
                valores = list(values.values())
                for i in range(0, len(valores)-1, 2):
                    if valores[i]!='' and valores[i+1]!='':
                        hr.append(valores[i])
                        t.append(valores[i+1])
                params = np.array(list(zip(hr, t)), dtype=float)
                window.close()
                return params
            except ValueError:
                sg.PopupOK('Invalid Input!', title='Warning')
        if "+" in event:
            n = int(event[1:])+1
            if n<9:
                window[f'+{n-1}'].update(visible=False)
                window[f'-temp{n}-'].update(visible=True)
                window[f'-k{n}-'].update(visible=True)
                window[f'+{n}'].update(visible=True)
            elif n==9:
                window[f'+{n-1}'].update(visible=False)
                window[f'-temp{n}-'].update(visible=True)
                window[f'-k{n}-'].update(visible=True)
                
def plotk(params):
    import numpy as np
    import matplotlib.pyplot as plt
    if type(params) == float:
        plt.plot([25,800],[params, params])
    else:
        T, k = params.T
        plt.plot(T, k)
        plt.show()
        
def Window():
    col_prop = [[sg.T(' k [W/(m·K)]', size=(10,1)), sg.In('', size=(15,1), justification='right', key='-k-'), sg.Button('Temperature Dependant', size=(18,1), key='-loadk-'), sg.Button('📊', size=(4,1), key='-plotk-')],
            ]

    menu_def = [['File', ['Load','Save','Exit']],
                ['Help', ['About']]]

    layout = [[sg.Menu(menu_def)],
              [sg.Column(col_prop)]]
    window = sg.Window('Name!', layout)

    kparams = np.array([['','']])

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == '-loadk-':
            try:
                tpar = kWindow(kparams)
                if tpar is not None: kparams = tpar
            except: pass
        if event == '-plotk-':
            if kparams[0,0] == '' and values['-k-']=='':
                sg.PopupOK('You need to define the «Thermal Conductivity» first!', title='Warning')
            elif values['-k-']!='': plotk(float(values['-k-']))
            else: plotk(kparams)
    window.close()
    
Window()
