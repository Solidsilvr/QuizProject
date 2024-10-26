import PySimpleGUI as sg
font = ("Helvetica", 20)
sg.set_options(font=font)
sg.theme("LightPurple")
sg.Window._move_all_windows = True
sg.theme_background_color("#B0AAC2")

fin_bg_menu=True
kot_menu=True

timecount=30
Score=0
loopbreaker1=True
Exit_code= "|          QUIT          |\n"

background_layout=[[sg.Image(source="Background_image.png")]]
window_background = sg.Window('Background', background_layout, no_titlebar=True, finalize=fin_bg_menu, margins=(0, 0), element_padding=(0,0))
menu    =[[sg.Push(),sg.Text("Sree Narayana Public School Poothotta",font="Verdana 24 italic",pad=(0,(11,0))),sg.Push()],
          [sg.Push(),sg.Text("ComputerScience Department\n",font="Verdana 24 italic"),sg.Push()],
          [sg.Push(),sg.Text("Take A Quiz\n",font="Helvetica 21"),sg.Push()],
          [sg.Text("           Select A Category",font="Helvetica 21")],
          [sg.Push(),sg.Slider((1,3),orientation="horizontal",size=(12,14),pad=((0,9),0))],
          [sg.Button("MATHS",size=(25,1)),sg.Text("                                                                         Difficulty",font="Helvetica 22")],
          [sg.Button("COMPUTER SCIENCE",size=(25,1)),sg.Push()],
          [sg.Button("SCIENCE",size=(25,1)),sg.Push(),sg.Text("Follow Me On Github")],
          [sg.Button("ENGLISH",size=(25,1)),sg.Push(),sg.Button("@Solidsilvr",size=(9,1))],
          [sg.Button("GK",size=(25,1)),sg.Push(),sg.Button("QUIT",size=(9,1))]
          ]
menuwin = sg.Window("Main Menu",menu,size=(1200,620),finalize=fin_bg_menu, keep_on_top=kot_menu, grab_anywhere=False,  transparent_color=sg.theme_background_color(), no_titlebar=True)
qz_lo  =[[sg.Text("Question 1",pad=((9,0),(11,0))),sg.Push(),sg.Text(key="Timer",font="Courier 24 bold",text_color="white",size=(6,1),justification='right',pad=((0,9),(11,0)))],
         [sg.VPush()],
         [sg.Push(),sg.Button("A",size=(15,1),pad=((8,5),(0,9))),sg.Button("B",size=(15,1),pad=(5,(0,9))),sg.Button("C",size=(15,1),pad=(5,(0,9))),sg.Button("D",size=(15,1),pad=((5,7),(0,9))),sg.Push()]
          ]
qz_win = sg.Window("Quiz Window",qz_lo,size=(1120,199),no_titlebar=True)
sc_lo  =[[sg.Push(),sg.Text("Your Score = ",font="Helvetica 22",pad=((5,0),(8,0))),sg.Text(key="-score-",font="Helvetica 22",justification='c',pad=((1,2),(8,0))),sg.Text("/ 5",font="Helvetica 22",pad=((1,5),(8,0))),sg.Push()],
         [sg.Push(),sg.Text("Return To Main Menu",font="Helvetica 22"),sg.Push()],
         [sg.VPush()],
         [sg.Push(),sg.Button("RESET",size=(8,1),pad=(10,5)),sg.Button("QUIT",size=(8,1),pad=(10,5)),sg.Push()]
          ]
sc_win = sg.Window("Score Window",sc_lo,size=(540,165),no_titlebar=True)

while True:
    window, event, values = sg.read_all_windows()
    print(event, values)
    if event in ("QUIT","MATHS","SCIENCE","ENGLISH","COMPUTER SCIENCE","GK","@Solidsilvr"):
        print(f'closing window = {window.Title}')
        menuwin.close()
        window_background.close()
        fin_bg_menu=False
        kot_menu=False
    if event == "QUIT":
        break
    if event == "@Solidsilvr":
        import webbrowser
        webbrowser.open("https://github.com/Solidsilvr")
        if sg.popup(Exit_code,button_justification='c') in ("OK",sg.WIN_CLOSED):
            break
    if event == "MATHS": 
        while timecount >= 0:
            event2 , values2 = qz_win.read(timeout=1000)
            qz_win["Timer"].update(timecount)
            timecount=timecount-1
            if event2 == "A":
                Score=Score+1
                break
        qz_win.close()
        while loopbreaker1 == True:
            scev , scva = sc_win.read(timeout=1000)
            sc_win["-score-"].update(Score)
            if scev == "QUIT":
                sc_win.close()
                loopbreaker1=False
                break
        break
