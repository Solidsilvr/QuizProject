Quest_CS_E=   ["This is the placeholder text for question CS 1 Easy",
               "This is the placeholder text for question CS 2 Easy",
               "This is the placeholder text for question CS 3 Easy",
               "This is the placeholder text for question CS 4 Easy",
               "This is the placeholder text for question CS 5 Easy",
               "This is the placeholder text for question CS 6 Easy",
               "This is the placeholder text for question CS 7 Easy",
               "This is the placeholder text for question CS 8 Easy",
               "This is the placeholder text for question CS 9 Easy",
               "This is the placeholder text for question CS 10 Easy"]

Quest_CS_M=   ["This is the placeholder text for question CS 1 Medium",
               "This is the placeholder text for question CS 2 Medium",
               "This is the placeholder text for question CS 3 Medium",
               "This is the placeholder text for question CS 4 Medium",
               "This is the placeholder text for question CS 5 Medium",
               "This is the placeholder text for question CS 6 Medium",
               "This is the placeholder text for question CS 7 Medium",
               "This is the placeholder text for question CS 8 Medium",
               "This is the placeholder text for question CS 9 Medium",
               "This is the placeholder text for question CS 10 Medium"]

Quest_CS_H=   ["This is the placeholder text for question CS 1 Hard",
               "This is the placeholder text for question CS 2 Hard",
               "This is the placeholder text for question CS 3 Hard",
               "This is the placeholder text for question CS 4 Hard",
               "This is the placeholder text for question CS 5 Hard",
               "This is the placeholder text for question CS 6 Hard",
               "This is the placeholder text for question CS 7 Hard",
               "This is the placeholder text for question CS 8 Hard",
               "This is the placeholder text for question CS 9 Hard",
               "This is the placeholder text for question CS 10 Hard"]

Opt_CS_E=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Opt_CS_M=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Opt_CS_H=   [["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"],
             ["Option 1 Placeholder","Option 2 Placeholder","Option 3 Placeholder","Option 4 Placeholder"]]

Ans_CS_E=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Ans_CS_M=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Ans_CS_H=   ["A",
             "B",
             "C",
             "D",
             "A",
             "B",
             "C",
             "D",
             "A",
             "B"]

Wr_Ans_CS_E=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Wr_Ans_CS_M=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Wr_Ans_CS_H=   [["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"],
                ["A","B","D"],
                ["A","B","C"],
                ["B","C","D"],
                ["A","C","D"]]

Quest_CS_E.extend(Quest_CS_M)
Quest_CS_E.extend(Quest_CS_H)
Quest=Quest_CS_E.copy()

Opt_CS_E.extend(Opt_CS_M)
Opt_CS_E.extend(Opt_CS_H)
Opt=Opt_CS_E.copy()

Ans_CS_E.extend(Ans_CS_M)
Ans_CS_E.extend(Ans_CS_H)
Ans=Ans_CS_E.copy()

Wr_Ans_CS_E.extend(Wr_Ans_CS_M)
Wr_Ans_CS_E.extend(Wr_Ans_CS_H)
Wr_Ans=Wr_Ans_CS_E.copy()