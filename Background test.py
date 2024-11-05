import PySimpleGUI as sg
sg.set_options(font=("Helvetica", 20))
sg.theme("LightPurple")
sg.Window._move_all_windows = True
sg.theme_background_color("#B0AAC2")

fin_menu=True
fin_qz=False
fin_sc=False
fin_quit=False

timecount=30
tickcount=60
Score=0
loopbreaker1=True
loopbreaker0=True
loopbreaker2=True
Pushfall0=True
Pushfall1=True
Pushfall2=True
Rd_fixdex=[]
Rd_loopfix_E=1

Quest_E=["This is the placeholder text for question 1 Easy",
         "This is the placeholder text for question 2 Easy",
         "This is the placeholder text for question 3 Easy",
         "This is the placeholder text for question 4 Easy",
         "This is the placeholder text for question 5 Easy",
         "This is the placeholder text for question 6 Easy",
         "This is the placeholder text for question 7 Easy",
         "This is the placeholder text for question 8 Easy",
         "This is the placeholder text for question 9 Easy",
         "This is the placeholder text for question 10 Easy"]

Opt_E=[["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
       ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
       ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
       ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
       ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
       ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
       ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
       ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
       ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
       ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Ans_E=["A",
       "B",
       "C",
       "D",
       "A",
       "B",
       "C",
       "D",
       "A",
       "B"]

Wr_Ans_E=[["B","C","D"],
          ["A","C","D"],
          ["A","B","D"],
          ["A","B","C"],
          ["B","C","D"],
          ["A","C","D"],
          ["A","B","D"],
          ["A","B","C"],
          ["B","C","D"],
          ["A","C","D"]]

background_layout=[[sg.Image(source="Background_image.png")]]
window_background = sg.Window('Background', background_layout, no_titlebar=True, finalize=fin_menu, margins=(0, 0), element_padding=(0,0))

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
menuwin = sg.Window("Main Menu",menu,size=(1200,620),finalize=fin_menu, keep_on_top=True, grab_anywhere=False,  transparent_color=sg.theme_background_color(), no_titlebar=True,modal=True)

qz_bg_lo=[[sg.Image(source="qz_bg_image.png")]]
qz_bg_win=sg.Window('qz_Background', qz_bg_lo, no_titlebar=True, finalize=fin_qz, margins=(0, 0), element_padding=(0,0))

qz_lo  =[[sg.Text("Question",pad=((9,0),(11,0))),sg.Text(key="QuizNum",pad=((2,0),(11,0))),sg.Push(),sg.Text(key="Timer",font="Verdana 26 italic",text_color="white",size=(6,1),justification='right',pad=((0,9),(11,0)))],
         [sg.Text(key="-Question-",pad=((9,0),(4,0))),sg.Push()],
         [sg.VPush()],
         [sg.Push(),sg.Button(key="A",size=(15,1),pad=((8,5),(0,9))),sg.Button(key="B",size=(15,1),pad=(5,(0,9))),sg.Button(key="C",size=(15,1),pad=(5,(0,9))),sg.Button(key="D",size=(15,1),pad=((5,7),(0,9))),sg.Push()]
          ]
qz_win = sg.Window("Quiz Window",qz_lo,size=(1120,199),no_titlebar=True,finalize=fin_qz,keep_on_top=True,grab_anywhere=False,transparent_color=sg.theme_background_color(),modal=True)

sc_bg_lo=[[sg.Image(source="sc_bg_image.png")]]
sc_bg_win=sg.Window('sc_Background', sc_bg_lo, no_titlebar=True, finalize=fin_sc, margins=(0, 0), element_padding=(0,0))

sc_lo  =[[sg.Push(),sg.Text("Your Score = ",font="Helvetica 22",pad=((5,0),(8,0))),sg.Text(key="-score-",font="Helvetica 22",justification='c',pad=((1,2),(8,0))),sg.Text("/ 5",font="Helvetica 22",pad=((1,5),(8,0))),sg.Push()],
         [sg.Push(),sg.Text("Return To Main Menu",font="Helvetica 22"),sg.Push()],
         [sg.VPush()],
         [sg.Push(),sg.Button("RESET",size=(8,1),pad=(10,5)),sg.Button("QUIT",size=(8,1),pad=(10,5)),sg.Push()]
          ]
sc_win = sg.Window("Score Window",sc_lo,size=(540,165),no_titlebar=True,finalize=fin_sc,keep_on_top=True,transparent_color=sg.theme_background_color(),grab_anywhere=False,modal=True)

quit_bg_lo=[[sg.Image(source="quitsc_bg_image.png")]]
quit_bg_win=sg.Window('quitsc_Background', quit_bg_lo, no_titlebar=True, finalize=fin_quit, margins=(0, 0), element_padding=(0,0))

quit_lo=[[sg.VPush()],
         [sg.Push(),sg.Text("QUITTING",font="Verdana 24 italic"),sg.Push()],
         [sg.VPush()]
          ]
quit_win = sg.Window("Quit Window",quit_lo,size=(240,165),no_titlebar=True,finalize=fin_quit,keep_on_top=False,transparent_color=sg.theme_background_color(),grab_anywhere=False)

while True:
    window, event, values = sg.read_all_windows()
    print(event, values)
    if event in ("QUIT","MATHS","SCIENCE","ENGLISH","COMPUTER SCIENCE","GK","@Solidsilvr"):
        menuwin.close()
        window_background.close()
        fin_bg_menu=False
    if event == "QUIT":
        break
    if event == "@Solidsilvr":
        while loopbreaker2 == True:
            fin_quit=True
            import webbrowser
            webbrowser.open("https://github.com/Solidsilvr")
            quit_bg_ev, quit_bg_va = quit_bg_win.read(timeout=10)
            quit_ev, quit_va = quit_win.read(timeout=3000)
            quit_bg_win.close()
            quit_win.close()
            loopbreaker2=False        
            break
    if event in ("MATHS","SCIENCE","COMPUTER SCIENCE","ENGLISH","GK"): 
        fin_qz=True
        import random as rd
        while loopbreaker0 == True:
            qz_bg_ev, qz_bg_va = qz_bg_win.read(timeout=10)
            while Rd_loopfix_E <= 5:
                Rd_Num=rd.randint(0,9)
                if Rd_Num not in Rd_fixdex:                   
                    Rd_fixdex.append(Rd_Num)    
                    while timecount >= 0:
                        event2 , values2 = qz_win.read(timeout=500)
                        if Pushfall1 == True:
                            qz_win["Timer"].update(timecount)
                            Pushfall1=False
                        tickcount=tickcount-1
                        if tickcount%2 == 0:    
                            timecount=timecount-1
                            qz_win["Timer"].update(timecount)
                            if timecount == 0:
                                break
                        if (event2 == Ans_E[Rd_Num]):
                            Score=Score+1
                            break
                        elif (event2 in Wr_Ans_E[Rd_Num]):
                            break
                        if Pushfall0 == True:
                            qz_win["QuizNum"].update(Rd_loopfix_E)
                            qz_win["-Question-"].update(Quest_E[Rd_Num])
                            qz_win["A"].update(Opt_E[Rd_Num][0])  
                            qz_win["B"].update(Opt_E[Rd_Num][1])
                            qz_win["C"].update(Opt_E[Rd_Num][2])
                            qz_win["D"].update(Opt_E[Rd_Num][3])
                            Pushfall0=False
                else:
                    continue
                Rd_loopfix_E += 1
                if Rd_loopfix_E <= 5:
                    Pushfall0=True
                    Pushfall1=True
                    timecount=30
                    continue
                else:
                    break
            qz_win.close()
            qz_bg_win.close()
            loopbreaker0=False
            break
        fin_qz=False
        while loopbreaker1 == True:
            fin_sc=True
            sc_bg_ev, sc_bg_va = sc_bg_win(timeout=10)
            scev , scva = sc_win.read(timeout=1000)
            sc_win["-score-"].update(Score)
            if scev == "QUIT":
                sc_win.close()
                sc_bg_win.close()
                loopbreaker1=False
                break
        break
    break
