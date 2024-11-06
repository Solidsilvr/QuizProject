Quest_Eg_E=   ["This is the placeholder text for question English 1 Easy",
               "This is the placeholder text for question English 2 Easy",
               "This is the placeholder text for question English 3 Easy",
               "This is the placeholder text for question English 4 Easy",
               "This is the placeholder text for question English 5 Easy",
               "This is the placeholder text for question English 6 Easy",
               "This is the placeholder text for question English 7 Easy",
               "This is the placeholder text for question English 8 Easy",
               "This is the placeholder text for question English 9 Easy",
               "This is the placeholder text for question English 10 Easy"]

Quest_Eg_M=   ["This is the placeholder text for question English 1 Medium",
               "This is the placeholder text for question English 2 Medium",
               "This is the placeholder text for question English 3 Medium",
               "This is the placeholder text for question English 4 Medium",
               "This is the placeholder text for question English 5 Medium",
               "This is the placeholder text for question English 6 Medium",
               "This is the placeholder text for question English 7 Medium",
               "This is the placeholder text for question English 8 Medium",
               "This is the placeholder text for question English 9 Medium",
               "This is the placeholder text for question English 10 Medium"]

Quest_Eg_H=   ["This is the placeholder text for question English 1 Hard",
               "This is the placeholder text for question English 2 Hard",
               "This is the placeholder text for question English 3 Hard",
               "This is the placeholder text for question English 4 Hard",
               "This is the placeholder text for question English 5 Hard",
               "This is the placeholder text for question English 6 Hard",
               "This is the placeholder text for question English 7 Hard",
               "This is the placeholder text for question English 8 Hard",
               "This is the placeholder text for question English 9 Hard",
               "This is the placeholder text for question English 10 Hard"]

Opt_Eg_E=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Opt_Eg_M=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Opt_Eg_H=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Ans_Eg_E=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Ans_Eg_M=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Ans_Eg_H=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Wr_Ans_Eg_E=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Wr_Ans_Eg_M=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Wr_Ans_Eg_H=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Quest_Eg_E.extend(Quest_Eg_M)
Quest_Eg_E.extend(Quest_Eg_H)
Quest=Quest_Eg_E.copy()

Opt_Eg_E.extend(Opt_Eg_M)
Opt_Eg_E.extend(Opt_Eg_H)
Opt=Opt_Eg_E.copy()

Ans_Eg_E.extend(Ans_Eg_M)
Ans_Eg_E.extend(Ans_Eg_H)
Ans=Ans_Eg_E.copy()

Wr_Ans_Eg_E.extend(Wr_Ans_Eg_M)
Wr_Ans_Eg_E.extend(Wr_Ans_Eg_H)
Wr_Ans=Wr_Ans_Eg_E.copy()