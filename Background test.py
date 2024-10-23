import PySimpleGUI as sg
font = ("Helvetica", 20)
sg.set_options(font=font)
sg.theme("PythonPlus")
sg.Window._move_all_windows = True
sg.theme_background_color("#001d3c")
background_layout=[[sg.Image(source="Background_image.png")]]
window_background = sg.Window('Background', background_layout, no_titlebar=True, finalize=True, margins=(0, 0), element_padding=(0,0))
menu    =[[sg.Push(),sg.Text("Sree Narayana Public School Poothotta"),sg.Push()],
          [sg.Push(),sg.Text("ComputerScience Department\n"),sg.Push()],
          [sg.Push(),sg.Text("Take A Quiz\n"),sg.Push()],
          [sg.Text("           Select A Category")],
          [sg.Push(),sg.Slider((1,3),orientation="horizontal",size=(12,14))],
          [sg.Button("MATHS",size=(25,1)),sg.Text("                                                                          Difficulty")],
          [sg.Button("COMPUTER SCIENCE",size=(25,1)),sg.Push()],
          [sg.Button("SCIENCE",size=(25,1)),sg.Push(),sg.Text("Follow Me On Github")],
          [sg.Button("ENGLISH",size=(25,1)),sg.Push(),sg.Button("@Solidsilvr",size=(9,1))],
          [sg.Button("GK",size=(25,1)),sg.Push(),sg.Button("QUIT",size=(9,1))]
          ]
menuwin = sg.Window("Main Menu",menu,size=(1200,620),finalize=True, keep_on_top=True, grab_anywhere=False,  transparent_color=sg.theme_background_color(), no_titlebar=True)
while True:
    window, event, values = sg.read_all_windows()
    print(event, values)
    if event == "QUIT":
        print(f'closing window = {window.Title}')
        break
menuwin.close()
window_background.close()
