import PySimpleGUI as sg
font = ("Helvetica", 20)
sg.set_options(font=font)
sg.theme("DarkAmber")
sg.theme_background_color("#204969")
Score=0
timecount=30
menu    =[[sg.Push(background_color="#204969"),sg.Text("Sree Narayana Public School Poothotta",background_color="#204969"),sg.Push(background_color="#204969")],
          [sg.Push(background_color="#204969"),sg.Text("ComputerScience Department",background_color="#204969"),sg.Push(background_color="#204969")],
          [sg.Text(background_color="#204969")],
          [sg.Push(background_color="#204969"),sg.Text("Take A Quiz",background_color="#204969"),sg.Push(background_color="#204969")],
          [sg.Text(background_color="#204969")],
          [sg.Text("           Select A Category",background_color="#204969")],
          [sg.Push(background_color="#204969"),sg.Slider((1,3),orientation="horizontal",size=(12,14),background_color="#204969")],
          [sg.Button("MATHS",size=(25,1)),sg.Text("                                                                          Difficulty",background_color="#204969")],
          [sg.Button("COMPUTER SCIENCE",size=(25,1)),sg.Push(background_color="#204969")],
          [sg.Button("SCIENCE",size=(25,1)),sg.Push(background_color="#204969"),sg.Text("Follow Me On Github",background_color="#204969")],
          [sg.Button("ENGLISH",size=(25,1)),sg.Push(background_color="#204969"),sg.Button("@Solidsilvr",size=(9,1))],
          [sg.Button("GK",size=(25,1)),sg.Push(background_color="#204969"),sg.Button("QUIT",size=(9,1))]
          ]
layout  =[[sg.Push(),sg.Text("Question 1"),sg.Push(),sg.Text(key="Timer",font="Courier 24 bold",text_color="white",size=(6,1),justification='right')],
          [sg.Push(),sg.Button("A"),sg.Button("B"),sg.Button("C"),sg.Button("D"),sg.Push()]
          ]
layout2 =[[sg.Text("Question 2")],
          [sg.Button("A"),sg.Button("B"),sg.Button("C"),sg.Button("D")]
          ]
layout3 =[[sg.Text("Question 3")],
          [sg.Button("A"),sg.Button("B"),sg.Button("C"),sg.Button("D")]
          ]
layout4 =[[sg.Text("Question 4")],
          [sg.Button("A"),sg.Button("B"),sg.Button("C"),sg.Button("D")]
          ]
layout5 =[[sg.Text("Question 5")],
          [sg.Button("A"),sg.Button("B"),sg.Button("C"),sg.Button("D")]
          ]
menuwin = sg.Window("Main Menu",menu,size=(1200,620))
window = sg.Window("TitleBar Text",layout)
window2 = sg.Window("TitleBar Text",layout2)
window3 = sg.Window("TitleBar Text",layout3)
window4 = sg.Window("TitleBar Text",layout4)
window5 = sg.Window("TitleBar Text",layout5)
while True :
    event6 , values6 = menuwin.read()
    if event6 in (sg.WIN_CLOSED,"QUIT"):
        break
    elif event6 == "@Solidsilvr":
        import webbrowser
        webbrowser.open("https://github.com/Solidsilvr")
    elif event6 == "MATHS":
        while timecount >= 0:
            event , values = window.read(timeout=1000)
            window["Timer"].update(timecount)
            timecount=timecount-1
            if event == "A":
                Score=Score+1
                print(Score)
                break
            elif event == "B" or event == "C" or event == "D":
                break
        window.close()
    event2 , values2 = window2.read()
    if event2 == "A":
        Score=Score+1
        print(Score)
        window2.close()
    elif event2 == "B" or event2 == "C" or event2 == "D":
        window2.close()
    event3 , values3 = window3.read()
    if event3 == "A":
        Score=Score+1
        print(Score)
        window3.close()
    elif event3 == "B" or event3 == "C" or event3 == "D":
        window3.close()
    event4 , values4 = window4.read()
    if event4 == "A":
        Score=Score+1
        print(Score)
        window4.close()
    elif event4 == "B" or event4 == "C" or event4 == "D":
        window4.close()
    event5 , values5 = window5.read()
    if event5 == "A":
        Score=Score+1
        print(Score)
        read="Your Score = "+str(Score)+"/5\nReturn to Main Menu"
        print(read)
        window5.close()
    elif event5 == "B" or event5 == "C" or event5 == "D":
        window5.close()
    if sg.popup_yes_no(read,no_titlebar=True,modal=True) == "Yes":
        break
print("Done")
