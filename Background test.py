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
Total_E=5
Total_M=10
Total_H=15
loopbreaker1=True
loopbreaker0=True
loopbreaker2=True
loopbreaker3=True
Pushfall0=True
Pushfall1=True
Rd_fixdex_E=[]
Rd_fixdex_M=[]
Rd_fixdex_H=[]
Rd_loopfix_E=1

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
menuwin = sg.Window("Main Menu",menu,size=(1280,720),finalize=fin_menu, keep_on_top=True, grab_anywhere=False,  transparent_color=sg.theme_background_color(), no_titlebar=True,modal=True)

qz_bg_lo=[[sg.Image(source="qz_bg_image.png")]]
qz_bg_win=sg.Window('qz_Background', qz_bg_lo, no_titlebar=True, finalize=fin_qz, margins=(0, 0), element_padding=(0,0))

qz_lo  =[[sg.Text("Question",pad=((9,0),(11,0))),sg.Text(key="QuizNum",pad=((2,0),(11,0))),sg.Push(),sg.Text(key="Timer",font="Verdana 26 italic",text_color="white",size=(6,1),justification='right',pad=((0,9),(11,0)))],
         [sg.Text(key="-Question-",pad=((9,0),(4,0))),sg.Push()],
         [sg.VPush()],
         [sg.Push(),sg.Button(key="A",size=(15,1),pad=((8,5),(0,9))),sg.Button(key="B",size=(15,1),pad=(5,(0,9))),sg.Button(key="C",size=(15,1),pad=(5,(0,9))),sg.Button(key="D",size=(15,1),pad=((5,7),(0,9))),sg.Push()]
          ]
qz_win = sg.Window("Quiz Window",qz_lo,size=(1280,386),no_titlebar=True,finalize=fin_qz,keep_on_top=True,grab_anywhere=False,transparent_color=sg.theme_background_color(),modal=True)

sc_bg_lo=[[sg.Image(source="sc_bg_image.png")]]
sc_bg_win=sg.Window('sc_Background', sc_bg_lo, no_titlebar=True, finalize=fin_sc, margins=(0, 0), element_padding=(0,0))

sc_lo  =[[sg.Push(),sg.Text("Your Score = ",font="Helvetica 22",pad=((5,0),(16,0))),sg.Text(key="-score-",font="Helvetica 22",justification='c',pad=((1,3),(16,0))),sg.Text("/",font="Helvetica 22",pad=((2,2),(16,0))),sg.Text(key="-Total-",font="Helvetica 22",justification='c',pad=((0,5),(16,0))),sg.Push()],
         [sg.Push(),sg.Text("Return To Main Menu",font="Helvetica 22"),sg.Push()],
         [sg.VPush()],
         [sg.Push(),sg.Button("RESET",size=(8,1),pad=(10,12)),sg.Button("QUIT",size=(8,1),pad=(10,12)),sg.Push()]
          ]
sc_win = sg.Window("Score Window",sc_lo,size=(861,524),no_titlebar=True,finalize=fin_sc,keep_on_top=True,transparent_color=sg.theme_background_color(),grab_anywhere=False,modal=True)

quit_bg_lo=[[sg.Image(source="quitsc_bg_image.png")]]
quit_bg_win=sg.Window('quitsc_Background', quit_bg_lo, no_titlebar=True, finalize=fin_quit, margins=(0, 0), element_padding=(0,0),keep_on_top=fin_quit)

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
            quit_bg_ev, quit_bg_va = quit_bg_win.read(timeout=3000)
            quit_bg_win.close()
            loopbreaker2=False        
            break
    if event in ("MATHS","SCIENCE","COMPUTER SCIENCE","ENGLISH","GK"): 
        fin_qz=True
        if event == "MATHS":
            import Quest_Maths as Qst
        elif event == "COMPUTER SCIENCE":
            import Quest_CS as Qst
        elif event == "SCIENCE":
            import Quest_SC as Qst
        elif event == "ENGLISH":
            import Quest_Eg as Qst
        elif event == "GK":
            import Quest_GK as Qst
        import random as rd
        while loopbreaker0 == True:
            qz_bg_ev, qz_bg_va = qz_bg_win.read(timeout=10)
            while loopbreaker3 == True:
                if (Rd_loopfix_E >= 1 and Rd_loopfix_E <= 5):
                    Rd_Num=rd.randint(0,9)
                    if Rd_Num not in Rd_fixdex_E:                   
                        Rd_fixdex_E.append(Rd_Num)
                    else:
                        continue
                elif (Rd_loopfix_E >= 6 and Rd_loopfix_E <= 10):
                    Rd_Num=rd.randint(10,19)
                    if Rd_Num not in Rd_fixdex_M:                   
                        Rd_fixdex_M.append(Rd_Num)
                    else:
                        continue
                elif (Rd_loopfix_E >= 11 and Rd_loopfix_E <= 15):
                    Rd_Num=rd.randint(20,29)
                    if Rd_Num not in Rd_fixdex_H:                   
                        Rd_fixdex_H.append(Rd_Num)
                    else:
                        continue    
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
                    if (event2 == Qst.Ans[Rd_Num]):
                        Score=Score+1
                        break
                    elif (event2 in Qst.Wr_Ans[Rd_Num]):
                        break
                    if Pushfall0 == True:
                        qz_win["QuizNum"].update(Rd_loopfix_E)
                        qz_win["-Question-"].update(Qst.Quest[Rd_Num])
                        qz_win["A"].update(Qst.Opt[Rd_Num][0])  
                        qz_win["B"].update(Qst.Opt[Rd_Num][1])
                        qz_win["C"].update(Qst.Opt[Rd_Num][2])
                        qz_win["D"].update(Qst.Opt[Rd_Num][3])
                        Pushfall0=False
                Rd_loopfix_E += 1
                if values == {0: 1.0}:
                    if (Rd_loopfix_E <= 5 and Rd_loopfix_E >= 1):
                        Pushfall0=True
                        Pushfall1=True
                        timecount=30
                        tickcount=60
                        continue
                    else:
                        loopbreaker3 = False
                        break
                elif values == {0: 2.0}:
                    if (Rd_loopfix_E <= 5 and Rd_loopfix_E >= 1):
                        Pushfall0=True
                        Pushfall1=True
                        timecount=30
                        tickcount=60
                        continue
                    elif (Rd_loopfix_E <= 10 and Rd_loopfix_E >= 6):
                        Pushfall0=True
                        Pushfall1=True
                        timecount=30
                        tickcount=60
                        continue
                    else:
                        loopbreaker3 = False
                        break
                elif values == {0: 3.0}:
                    if (Rd_loopfix_E <= 5 and Rd_loopfix_E >= 1):
                        Pushfall0=True
                        Pushfall1=True
                        timecount=30
                        tickcount=60
                        continue
                    elif (Rd_loopfix_E <= 10 and Rd_loopfix_E >= 6):
                        Pushfall0=True
                        Pushfall1=True
                        timecount=30
                        tickcount=60
                        continue
                    elif (Rd_loopfix_E <= 15 and Rd_loopfix_E >= 11):
                        Pushfall0=True
                        Pushfall1=True
                        timecount=30
                        tickcount=60
                        continue
                    else:
                        loopbreaker3 = False
                        break
            qz_win.close()
            qz_bg_win.close()
            loopbreaker0=False
            break
        fin_qz=False
        while loopbreaker1 == True:
            fin_sc=True
            sc_bg_ev, sc_bg_va = sc_bg_win(timeout=10)
            scev , scva = sc_win.read(timeout=500)
            if values == {0: 1.0}:
                sc_win["-Total-"].update(Total_E)
            elif values == {0: 2.0}:
                sc_win["-Total-"].update(Total_M)
            elif values == {0: 3.0}:
                sc_win["-Total-"].update(Total_H)
            sc_win["-score-"].update(Score)
            if scev == "QUIT":
                sc_win.close()
                sc_bg_win.close()
                loopbreaker1=False
                break
        break
    break