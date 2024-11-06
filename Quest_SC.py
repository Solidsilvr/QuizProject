Quest_SC_E=   ["This is the placeholder text for question Science 1 Easy",
               "This is the placeholder text for question Science 2 Easy",
               "This is the placeholder text for question Science 3 Easy",
               "This is the placeholder text for question Science 4 Easy",
               "This is the placeholder text for question Science 5 Easy",
               "This is the placeholder text for question Science 6 Easy",
               "This is the placeholder text for question Science 7 Easy",
               "This is the placeholder text for question Science 8 Easy",
               "This is the placeholder text for question Science 9 Easy",
               "This is the placeholder text for question Science 10 Easy"]

Quest_SC_M=   ["This is the placeholder text for question Science 1 Medium",
               "This is the placeholder text for question Science 2 Medium",
               "This is the placeholder text for question Science 3 Medium",
               "This is the placeholder text for question Science 4 Medium",
               "This is the placeholder text for question Science 5 Medium",
               "This is the placeholder text for question Science 6 Medium",
               "This is the placeholder text for question Science 7 Medium",
               "This is the placeholder text for question Science 8 Medium",
               "This is the placeholder text for question Science 9 Medium",
               "This is the placeholder text for question Science 10 Medium"]

Quest_SC_H=   ["This is the placeholder text for question Science 1 Hard",
               "This is the placeholder text for question Science 2 Hard",
               "This is the placeholder text for question Science 3 Hard",
               "This is the placeholder text for question Science 4 Hard",
               "This is the placeholder text for question Science 5 Hard",
               "This is the placeholder text for question Science 6 Hard",
               "This is the placeholder text for question Science 7 Hard",
               "This is the placeholder text for question Science 8 Hard",
               "This is the placeholder text for question Science 9 Hard",
               "This is the placeholder text for question Science 10 Hard"]

Opt_SC_E=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Opt_SC_M=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Opt_SC_H=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Ans_SC_E=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Ans_SC_M=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Ans_SC_H=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Wr_Ans_SC_E=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Wr_Ans_SC_M=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Wr_Ans_SC_H=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Quest_SC_E.extend(Quest_SC_M)
Quest_SC_E.extend(Quest_SC_H)
Quest=Quest_SC_E.copy()

Opt_SC_E.extend(Opt_SC_M)
Opt_SC_E.extend(Opt_SC_H)
Opt=Opt_SC_E.copy()

Ans_SC_E.extend(Ans_SC_M)
Ans_SC_E.extend(Ans_SC_H)
Ans=Ans_SC_E.copy()

Wr_Ans_SC_E.extend(Wr_Ans_SC_M)
Wr_Ans_SC_E.extend(Wr_Ans_SC_H)
Wr_Ans=Wr_Ans_SC_E.copy()