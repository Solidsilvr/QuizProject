Quest_GK_E=   ["This is the placeholder text for question GK 1 Easy",
               "This is the placeholder text for question GK 2 Easy",
               "This is the placeholder text for question GK 3 Easy",
               "This is the placeholder text for question GK 4 Easy",
               "This is the placeholder text for question GK 5 Easy",
               "This is the placeholder text for question GK 6 Easy",
               "This is the placeholder text for question GK 7 Easy",
               "This is the placeholder text for question GK 8 Easy",
               "This is the placeholder text for question GK 9 Easy",
               "This is the placeholder text for question GK 10 Easy"]

Quest_GK_M=   ["This is the placeholder text for question GK 1 Medium",
               "This is the placeholder text for question GK 2 Medium",
               "This is the placeholder text for question GK 3 Medium",
               "This is the placeholder text for question GK 4 Medium",
               "This is the placeholder text for question GK 5 Medium",
               "This is the placeholder text for question GK 6 Medium",
               "This is the placeholder text for question GK 7 Medium",
               "This is the placeholder text for question GK 8 Medium",
               "This is the placeholder text for question GK 9 Medium",
               "This is the placeholder text for question GK 10 Medium"]

Quest_GK_H=   ["This is the placeholder text for question GK 1 Hard",
               "This is the placeholder text for question GK 2 Hard",
               "This is the placeholder text for question GK 3 Hard",
               "This is the placeholder text for question GK 4 Hard",
               "This is the placeholder text for question GK 5 Hard",
               "This is the placeholder text for question GK 6 Hard",
               "This is the placeholder text for question GK 7 Hard",
               "This is the placeholder text for question GK 8 Hard",
               "This is the placeholder text for question GK 9 Hard",
               "This is the placeholder text for question GK 10 Hard"]

Opt_GK_E=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Opt_GK_M=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Opt_GK_H=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Ans_GK_E=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Ans_GK_M=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Ans_GK_H=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Wr_Ans_GK_E=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Wr_Ans_GK_M=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Wr_Ans_GK_H=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Quest_GK_E.extend(Quest_GK_M)
Quest_GK_E.extend(Quest_GK_H)
Quest=Quest_GK_E.copy()

Opt_GK_E.extend(Opt_GK_M)
Opt_GK_E.extend(Opt_GK_H)
Opt=Opt_GK_E.copy()

Ans_GK_E.extend(Ans_GK_M)
Ans_GK_E.extend(Ans_GK_H)
Ans=Ans_GK_E.copy()

Wr_Ans_GK_E.extend(Wr_Ans_GK_M)
Wr_Ans_GK_E.extend(Wr_Ans_GK_H)
Wr_Ans=Wr_Ans_GK_E.copy()