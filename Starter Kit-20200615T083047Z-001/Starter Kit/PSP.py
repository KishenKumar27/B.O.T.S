import psphelper;

title = "Battle Of the Sexes(B.O.T.S)"
fillchar = "="
print(title.center(77, fillchar))

marksP1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
marksP2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

marks2 = [ marksP1, marksP2 ]

turn_1 = 0
turn_2 = 0

score_1 = 0
score_2 = 0

while turn_1 < 9 or turn_2 < 9:

    title = "Scoreboard"
    player = ["Player 1","Player 2"]
    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
    psphelper.ShowTableByList(title,player,categories,marks2)

    print("Player 1:" ,score_1 )
    print("Player 2:" , score_2)

    print("\nPlayer 1")
    print('='*8)
    enter = input('Press ENTER to roll dice.\n')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Roll 1 for player 1


    
    import random
    list_1 = [1,2,3,4,5]

    for i in range(len(list_1)):
       list_1[i] = random.randint(1,4)
    print("Roll #1 : ",list_1)
    print(' ')

    sum_1 = sum(list_1[:5])
    ones_1S = (list_1[:5]).count(1)
    twos_2S = (list_1[:5]).count(2)
    twos_4S = twos_2S * 2
    threes_3S = (list_1[:5]).count(3)
    threes_9S = threes_3S * 3
    fours_4S = (list_1[:5]).count(4)
    fours_16S = fours_4S * 4
    if (ones_1S == 3) or (twos_2S == 3) or (threes_3S == 3) or (fours_4S == 3):
        trio = sum_1
        
    else:
        trio = 0
        

    if (ones_1S == 4) or (twos_2S == 4) or (threes_3S == 4) or (fours_4S == 4):
        quartet = sum_1
        
    else:
        quartet = 0
        

    if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
        doremi = 20
    else:
        doremi = 0

    if quartet > 0:
        band = 0
    elif (ones_1S == 3) and (twos_2S == 2):
        band = 30
    elif (ones_1S == 3) and (threes_3S == 2):
        band = 30
    elif (ones_1S == 3) and (fours_4S == 2):
        band = 30
    elif (twos_2S == 3) and (ones_1S == 2):
        band = 30
    elif (twos_2S == 3) and (threes_3S == 2):
        band = 30
    elif (twos_2S == 3) and (fours_4S == 2):
        band = 30
    elif (threes_3S == 3) and (ones_1S == 2):
        band = 30
    elif (threes_3S == 3) and (twos_2S == 2):
        band = 30
    elif (threes_3S == 3) and (fours_4S == 2):
        band = 30
    elif (fours_4S == 3) and (ones_1S == 2):
        band = 30
    elif (fours_4S == 3) and (twos_2S == 2):
        band = 30
    elif (fours_4S == 3) and (threes_3S == 2):
        band = 30
    else:
        band = 0
             
    if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
        orchestra = 40
    else:
        orchestra = 0

    marksList = [
        [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
        ]

    marksP1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    marksP2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    marks2 = [ marksP1, marksP2 ]

    title = 'Category Scores'
    player = ["Player 1","Player 2"]
    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
    psphelper.ShowTableByList(title,[],categories,marksList)

    print("")
    print("Input Options:")
    print(" SAVE           :- Accept these dice.")
    print(" ROLL           :- Re-roll ALL dice.")
    print(" ROLL d1 ... dn :- Re-roll specified dice only.")
        
    input_1 = input("\nInput > ").lower()

    wordList = input_1.split(' ')

    while wordList[0] != 'save' and wordList[0] != 'roll' and wordList[0] != 'cheat' :
        print("ERROR: Invalid Input")
        input_1 = input("Input > ").lower()
        wordList = input_1.split(' ')
        
    if len(wordList) == 1:
        if wordList[0] == 'save'.lower():
            desired_category = (input("Enter your desired category: "))

            if desired_category == '1S'.lower():
                      del(marksP1[0])
                      marksP1.insert(0,ones_1S)
                      score_1 += ones_1S

            elif desired_category == '2S'.lower():
                      del(marksP1[1])
                      marksP1.insert(1,twos_4S)
                      score_1 += twos_4S

            elif desired_category == '3S'.lower():
                      del(marksP1[2])
                      marksP1.insert(2,threes_9S)
                      score_1 += threes_9S

            elif desired_category == '4S'.lower():
                      del(marksP1[3])
                      marksP1.insert(3,fours_16S)
                      score_1 += fours_16S

            elif desired_category == 'Trio'.lower():
                      del(marksP1[4])
                      marksP1.insert(4,trio)
                      score_1 += trio
            elif desired_category == 'Quartet'.lower():
                      del(marksP1[5])
                      marksP1.insert(5,quartet)
                      score_1 += quartet

            elif desired_category == 'Band'.lower():
                      del(marksP1[6])
                      marksP1.insert(6,band)
                      score_1 += band

            elif desired_category == 'Doremi'.lower():
                      del(marksP1[7])
                      marksP1.insert(7,doremi)
                      score_1 += doremi

            elif desired_category == 'Orchestra'.lower():
                      del(marksP1[8])
                      marksP1.insert(8,orchestra)
                      score_1 += orchestra
    #-------------------------------------------------------------------------------------------------------------
    #2nd Roll for player 1
        elif wordList[0] == 'roll'.lower():
            score_1 = 0
            score_2 = 0
            import random
            list_1 = [1,2,3,4,5]

            for i in range(len(list_1)):
              list_1[i] = random.randint(1,4)
            print("Roll #2 : ",list_1)
            print(' ')          
            sum_1 = sum(list_1[:5])
            ones_1S = (list_1[:5]).count(1)
            twos_2S = (list_1[:5]).count(2)
            twos_4S = twos_2S * 2
            threes_3S = (list_1[:5]).count(3)
            threes_9S = threes_3S * 3
            fours_4S = (list_1[:5]).count(4)
            fours_16S = fours_4S * 4
            if (ones_1S == 3) or (twos_2S == 3) or (threes_3S == 3) or (fours_4S == 3):
                trio = sum_1
            
            else:
                trio = 0
                

            if (ones_1S == 4) or (twos_2S == 4) or (threes_3S == 4) or (fours_4S == 4):
                quartet = sum_1
                
            else:
                quartet = 0
                

            if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                doremi = 20
            else:
                doremi = 0

            if quartet > 0:
                band = 0
            elif (ones_1S == 3) and (twos_2S == 2):
                band = 30
            elif (ones_1S == 3) and (threes_3S == 2):
                band = 30
            elif (ones_1S == 3) and (fours_4S == 2):
                band = 30
            elif (twos_2S == 3) and (ones_1S == 2):
                band = 30
            elif (twos_2S == 3) and (threes_3S == 2):
                band = 30
            elif (twos_2S == 3) and (fours_4S == 2):
                band = 30
            elif (threes_3S == 3) and (ones_1S == 2):
                band = 30
            elif (threes_3S == 3) and (twos_2S == 2):
                band = 30
            elif (threes_3S == 3) and (fours_4S == 2):
                band = 30
            elif (fours_4S == 3) and (ones_1S == 2):
                band = 30
            elif (fours_4S == 3) and (twos_2S == 2):
                band = 30
            elif (fours_4S == 3) and (threes_3S == 2):
                band = 30
            else:
                band = 0
                 
            if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                orchestra = 40
            else:
                orchestra = 0

            marksList = [
                [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                ]

            marksP1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            marksP2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

            marks2 = [ marksP1, marksP2 ]

            title = 'Category Scores'
            player = ["Player 1","Player 2"]
            categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
            psphelper.ShowTableByList(title,[],categories,marksList)

            print("")
            print("Input Options:")
            print(" SAVE           :- Accept these dice.")
            print(" ROLL           :- Re-roll ALL dice.")
            print(" ROLL d1 ... dn :- Re-roll specified dice only.")
            
            input_1 = input("\nInput > ") . lower()

            wordList = input_1.split(' ')

            while wordList[0] != 'save' and wordList[0] != 'roll' and wordList[0] != 'cheat' :
                print("ERROR: Invalid Input")
                input_1 = input("Input > ") . lower()
                wordList = input_1.split(' ')
            
            if len(wordList) == 1:
                if wordList[0] == 'save'.lower():
                    if desired_category == '1S'.lower():
                      del(marksP1[0])
                      marksP1.insert(0,ones_1S)
                      score_1 += ones_1S

                    elif desired_category == '2S'.lower():
                        del(marksP1[1])
                        marksP1.insert(1,twos_4S)
                        score_1 += twos_4S

                    elif desired_category == '3S'.lower():
                        del(marksP1[2])
                        marksP1.insert(2,threes_9S)
                        score_1 += threes_9S

                    elif desired_category == '4S'.lower():
                        del(marksP1[3])
                        marksP1.insert(3,fours_16S)
                        score_1 += fours_16S

                    elif desired_category == 'Trio'.lower():
                        del(marksP1[4])
                        marksP1.insert(4,trio)
                        score_1 += trio
                    elif desired_category == 'Quartet'.lower():
                        del(marksP1[5])
                        marksP1.insert(5,quartet)
                        score_1 += quartet

                    elif desired_category == 'Band'.lower():
                        del(marksP1[6])
                        marksP1.insert(6,band)
                        score_1 += band

                    elif desired_category == 'Doremi'.lower():
                        del(marksP1[7])
                        marksP1.insert(7,doremi)
                        score_1 += doremi

                    elif desired_category == 'Orchestra'.lower():
                        del(marksP1[8])
                        marksP1.insert(8,orchestra)
                        score_1 += orchestra
    #----------------------------------------------------------------------------------------------------------------------
    #3rd and final roll for Player 1
                elif wordList[0] == 'roll'.lower():
                    import random
                    list_1 = [1,2,3,4,5]

                    for i in range(len(list_1)):
                       list_1[i] = random.randint(1,4)
                    print("Roll #3 : ",list_1)
                    print(' ')
                    sum_1 = sum(list_1[:5])
                    ones_1S = (list_1[:5]).count(1)
                    twos_2S = (list_1[:5]).count(2)
                    twos_4S = twos_2S * 2
                    threes_3S = (list_1[:5]).count(3)
                    threes_9S = threes_3S * 3
                    fours_4S = (list_1[:5]).count(4)
                    fours_16S = fours_4S * 4
                    if (ones_1S >= 3) or (twos_2S >= 3) or (threes_3S >= 3) or (fours_4S >= 3):
                        trio = sum_1
                
                    else:
                        trio = 0
                        

                    if (ones_1S >= 4) or (twos_2S >= 4) or (threes_3S >= 4) or (fours_4S >= 4):
                        quartet = sum_1
                        
                    else:
                        quartet = 0
                        

                    if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                        doremi = 20
                    else:
                        doremi = 0

                    if quartet > 0:
                        band = 0
                    elif (ones_1S == 3) and (twos_2S == 2):
                        band = 30
                    elif (ones_1S == 3) and (threes_3S == 2):
                        band = 30
                    elif (ones_1S == 3) and (fours_4S == 2):
                        band = 30
                    elif (twos_2S == 3) and (ones_1S == 2):
                        band = 30
                    elif (twos_2S == 3) and (threes_3S == 2):
                        band = 30
                    elif (twos_2S == 3) and (fours_4S == 2):
                        band = 30
                    elif (threes_3S == 3) and (ones_1S == 2):
                        band = 30
                    elif (threes_3S == 3) and (twos_2S == 2):
                        band = 30
                    elif (threes_3S == 3) and (fours_4S == 2):
                        band = 30
                    elif (fours_4S == 3) and (ones_1S == 2):
                        band = 30
                    elif (fours_4S == 3) and (twos_2S == 2):
                        band = 30
                    elif (fours_4S == 3) and (threes_3S == 2):
                        band = 30
                    else:
                        band = 0
                     
                    if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                        orchestra = 40
                    else:
                        orchestra = 0

                    marksList = [
                        [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                        ]

                    marksP1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                    marksP2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

                    marks2 = [ marksP1, marksP2 ]

                    title = 'Category Scores'
                    player = ["Player 1","Player 2"]
                    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
                    psphelper.ShowTableByList(title,[],categories,marksList)
                
                    desired_category = (input("Enter your desired category: "))
                    
                    if desired_category == '1S'.lower():
                              del(marksP1[0])
                              marksP1.insert(0,ones_1S)
                              score_1 += ones_1S

                    elif desired_category == '2S'.lower():
                              del(marksP1[1])
                              marksP1.insert(1,twos_4S)
                              score_1 += twos_4S

                    elif desired_category == '3S'.lower():
                              del(marksP1[2])
                              marksP1.insert(2,threes_9S)
                              score_1 += threes_9S

                    elif desired_category == '4S'.lower():
                              del(marksP1[3])
                              marksP1.insert(3,fours_16S)
                              score_1 += fours_16S

                    elif desired_category == 'Trio'.lower():
                              del(marksP1[4])
                              marksP1.insert(4,trio)
                              score_1 += trio
                    elif desired_category == 'Quartet'.lower():
                              del(marksP1[5])
                              marksP1.insert(5,quartet)
                              score_1 += quartet

                    elif desired_category == 'Band'.lower():
                              del(marksP1[6])
                              marksP1.insert(6,band)
                              score_1 += band

                    elif desired_category == 'Doremi'.lower():
                              del(marksP1[7])
                              marksP1.insert(7,doremi)
                              score_1 += doremi

                    elif desired_category == 'Orchestra'.lower():
                              del(marksP1[8])
                              marksP1.insert(8,orchestra)
                              score_1 += orchestra

    #===================================================================================================
            else:
                if wordList[0] == "roll".lower():
                    del(wordList[0])
                    if (wordList[0] == '1' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '2' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '3' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '4' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '5' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])           
                    elif (wordList[0] == "1" and wordList[1] == "2") or (wordList[0] == "2" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[2])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "3" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "3"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "3" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "3"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "4" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "4"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    else:
                        print("ERROR: Invalid Input")

                    sum_1 = sum(list_1[:5])
                    ones_1S = (list_1[:5]).count(1)
                    twos_2S = (list_1[:5]).count(2)
                    twos_4S = twos_2S * 2
                    threes_3S = (list_1[:5]).count(3)
                    threes_9S = threes_3S * 3
                    fours_4S = (list_1[:5]).count(4)
                    fours_16S = fours_4S * 4

                    if (ones_1S == 3) or (twos_2S == 3) or (threes_3S == 3) or (fours_4S == 3):
                        trio = sum_1
                        
                    else:
                        trio = 0
                        

                    if (ones_1S == 4) or (twos_2S == 4) or (threes_3S == 4) or (fours_4S == 4):
                        quartet = sum_1
                        
                    else:
                        quartet = 0
                        

                    if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                        doremi = 20
                    else:
                        doremi = 0

                    if quartet > 0:
                        band = 0
                    elif (ones_1S == 3) and (twos_2S == 2):
                        band = 30
                    elif (ones_1S == 3) and (threes_3S == 2):
                        band = 30
                    elif (ones_1S == 3) and (fours_4S == 2):
                        band = 30
                    elif (twos_2S == 3) and (ones_1S == 2):
                        band = 30
                    elif (twos_2S == 3) and (threes_3S == 2):
                        band = 30
                    elif (twos_2S == 3) and (fours_4S == 2):
                        band = 30
                    elif (threes_3S == 3) and (ones_1S == 2):
                        band = 30
                    elif (threes_3S == 3) and (twos_2S == 2):
                        band = 30
                    elif (threes_3S == 3) and (fours_4S == 2):
                        band = 30
                    elif (fours_4S == 3) and (ones_1S == 2):
                        band = 30
                    elif (fours_4S == 3) and (twos_2S == 2):
                        band = 30
                    elif (fours_4S == 3) and (threes_3S == 2):
                        band = 30
                    else:
                        band = 0
                             
                    if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                        orchestra = 40
                    else:
                        orchestra = 0

                    marksList = [
                        [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                        ]

                    marksP1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                    marksP2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

                    marks2 = [ marksP1, marksP2 ]

                    title = 'Category Scores'
                    player = ["Player 1","Player 2"]
                    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
                    psphelper.ShowTableByList(title,[],categories,marksList)
                
                    desired_category = (input("Enter your desired category: "))
                    
                    if desired_category == '1S'.lower():
                      del(marksP1[0])
                      marksP1.insert(0,ones_1S)
                      score_1 += ones_1S

                    elif desired_category == '2S'.lower():
                      del(marksP1[1])
                      marksP1.insert(1,twos_4S)
                      score_1 += twos_4S

                    elif desired_category == '3S'.lower():
                      del(marksP1[2])
                      marksP1.insert(2,threes_9S)
                      score_1 += threes_9S

                    elif desired_category == '4S'.lower():
                      del(marksP1[3])
                      marksP1.insert(3,fours_16S)
                      score_1 += fours_16S

                    elif desired_category == 'Trio'.lower():
                      del(marksP1[4])
                      marksP1.insert(4,trio)
                      score_1 += trio
                    elif desired_category == 'Quartet'.lower():
                      del(marksP1[5])
                      marksP1.insert(5,quartet)
                      score_1 += quartet

                    elif desired_category == 'Band'.lower():
                      del(marksP1[6])
                      marksP1.insert(6,band)
                      score_1 += band

                    elif desired_category == 'Doremi'.lower():
                      del(marksP1[7])
                      marksP1.insert(7,doremi)
                      score_1 += doremi

                    elif desired_category == 'Orchestra'.lower():
                      del(marksP1[8])
                      marksP1.insert(8,orchestra)
                      score_1 += orchestra
                
    #1st specific roll for player 1-------------------------------------------------
    else:
        if wordList[0] == "roll":
            del(wordList[0])
            if (wordList[0] == '1' and wordList[1] == ""):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[0])
                list_1.insert(0,list_2[0])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == '2' and wordList[1] == ""):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[1])
                list_1.insert(1,list_2[1])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == '3' and wordList[1] == ""):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[2])
                list_1.insert(2,list_2[2])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == '4' and wordList[1] == ""):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[3])
                list_1.insert(3,list_2[3])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == '5' and wordList[1] == ""):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[4])
                list_1.insert(4,list_2[4])
                print("\nRoll#2:",list_1[:5])           
            elif (wordList[0] == "1" and wordList[1] == "2") or (wordList[0] == "2" and wordList[1] == "1"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[0])
                list_1.insert(0,list_2[0])
                del(list_1[1])
                list_1.insert(1,list_2[1])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "1" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "1"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[0])
                list_1.insert(0,list_2[0])
                del(list_1[2])
                list_1.insert(2,list_2[2])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "1" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "1"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[0])
                list_1.insert(0,list_2[0])
                del(list_1[3])
                list_1.insert(3,list_2[3])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "1" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "1"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[0])
                list_1.insert(0,list_2[0])
                del(list_1[4])
                list_1.insert(4,list_2[4])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "2" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "2"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[1])
                list_1.insert(1,list_2[1])
                del(list_1[2])
                list_1.insert(2,list_2[2])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "2" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "2"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[1])
                list_1.insert(1,list_2[2])
                del(list_1[3])
                list_1.insert(3,list_2[3])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "2" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "2"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[1])
                list_1.insert(1,list_2[1])
                del(list_1[4])
                list_1.insert(4,list_2[4])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "3" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "3"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[2])
                list_1.insert(2,list_2[2])
                del(list_1[3])
                list_1.insert(3,list_2[3])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "3" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "3"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[2])
                list_1.insert(2,list_2[2])
                del(list_1[4])
                list_1.insert(4,list_2[4])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "4" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "4"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[3])
                list_1.insert(3,list_2[3])
                del(list_1[4])
                list_1.insert(4,list_2[4])
                print("\nRoll#2:",list_1[:5])
            else:
                print("ERROR: Invalid Input")
            
            sum_1 = sum(list_1[:5])
            ones_1S = (list_1[:5]).count(1)
            twos_2S = (list_1[:5]).count(2)
            twos_4S = twos_2S * 2
            threes_3S = (list_1[:5]).count(3)
            threes_9S = threes_3S * 3
            fours_4S = (list_1[:5]).count(4)
            fours_16S = fours_4S * 4

            if (ones_1S == 3) or (twos_2S == 3) or (threes_3S == 3) or (fours_4S == 3):
                trio = sum_1
                
            else:
                trio = 0
                

            if (ones_1S == 4) or (twos_2S == 4) or (threes_3S == 4) or (fours_4S == 4):
                quartet = sum_1
                
            else:
                quartet = 0
                

            if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                doremi = 20
            else:
                doremi = 0

            if quartet > 0:
                band = 0
            elif (ones_1S == 3) and (twos_2S == 2):
                band = 30
            elif (ones_1S == 3) and (threes_3S == 2):
                band = 30
            elif (ones_1S == 3) and (fours_4S == 2):
                band = 30
            elif (twos_2S == 3) and (ones_1S == 2):
                band = 30
            elif (twos_2S == 3) and (threes_3S == 2):
                band = 30
            elif (twos_2S == 3) and (fours_4S == 2):
                band = 30
            elif (threes_3S == 3) and (ones_1S == 2):
                band = 30
            elif (threes_3S == 3) and (twos_2S == 2):
                band = 30
            elif (threes_3S == 3) and (fours_4S == 2):
                band = 30
            elif (fours_4S == 3) and (ones_1S == 2):
                band = 30
            elif (fours_4S == 3) and (twos_2S == 2):
                band = 30
            elif (fours_4S == 3) and (threes_3S == 2):
                band = 30
            else:
                band = 0
                     
            if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                orchestra = 40
            else:
                orchestra = 0
            marksList = [
                [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                ]

            marksP1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            marksP2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

            marks2 = [ marksP1, marksP2 ]

            title = '\nCategory Scores'
            player = ["Player 1","Player 2"]
            categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
            psphelper.ShowTableByList(title,[],categories,marksList)

            print("")
            print("Input Options:")
            print(" SAVE           :- Accept these dice.")
            print(" ROLL           :- Re-roll ALL dice.")
            print(" ROLL d1 ... dn :- Re-roll specified dice only.")

            input_1 = input("\nInput > ") . lower()

            wordList = input_1.split(' ')

            while wordList[0] != 'save' and wordList[0] != 'roll' and wordList[0] != 'cheat' :
                print("ERROR: Invalid Input")
                input_1 = input("Input > ") . lower()
                wordList = input_1.split(' ')
            
    #============================================================================================
            if len(wordList) == 1:
                if wordList[0] == 'save'.lower():
                    desired_category = (input("Enter your desired category: "))
                    if desired_category == '1S':
                      del(marksP1[0])
                      marksP1.insert(0,ones_1S)
                      score_1 += ones_1S

                    elif desired_category == '2S'.lower():
                      del(marksP1[1])
                      marksP1.insert(1,twos_4S)
                      score_1 += twos_4S

                    elif desired_category == '3S'.lower():
                      del(marksP1[2])
                      marksP1.insert(2,threes_9S)
                      score_1 += threes_9S

                    elif desired_category == '4S'.lower():
                      del(marksP1[3])
                      marksP1.insert(3,fours_16S)
                      score_1 += fours_16S

                    elif desired_category == 'Trio'.lower():
                      del(marksP1[4])
                      marksP1.insert(4,trio)
                      score_1 += trio
                    elif desired_category == 'Quartet'.lower():
                      del(marksP1[5])
                      marksP1.insert(5,quartet)
                      score_1 += quartet

                    elif desired_category == 'Band'.lower():
                      del(marksP1[6])
                      marksP1.insert(6,band)
                      score_1 += band

                    elif desired_category == 'Doremi'.lower():
                      del(marksP1[7])
                      marksP1.insert(7,doremi)
                      score_1 += doremi

                    elif desired_category == 'Orchestra'.lower():
                      del(marksP1[8])
                      marksP1.insert(8,orchestra)
                      score_1 += orchestra
    #------------------------------------------------------------------------------------------------
                elif wordList[0] == 'roll'.lower():
                    
                    import random
                    list_1 = [1,2,3,4,5]

                    for i in range(len(list_1)):
                       list_1[i] = random.randint(1,4)
                    print("Roll #2 : ",list_1)
                    print(' ')
                    
                    sum_1 = sum(list_1[:5])
                    ones_1S = (list_1[:5]).count(1)
                    twos_2S = (list_1[:5]).count(2)
                    twos_4S = twos_2S * 2
                    threes_3S = (list_1[:5]).count(3)
                    threes_9S = threes_3S * 3
                    fours_4S = (list_1[:5]).count(4)
                    fours_16S = fours_4S * 4
                    if (ones_1S >= 3) or (twos_2S >= 3) or (threes_3S >= 3) or (fours_4S >= 3):
                        trio = sum_1
                        
                    else:
                        trio = 0
                        

                    if (ones_1S >= 4) or (twos_2S >= 4) or (threes_3S >= 4) or (fours_4S >= 4):
                        quartet = sum_1
                        
                    else:
                        quartet = 0
                        

                    if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                        doremi = 20
                    else:
                        doremi = 0

                    if quartet > 0:
                        band = 0
                    elif (ones_1S == 3) and (twos_2S == 2):
                        band = 30
                    elif (ones_1S == 3) and (threes_3S == 2):
                        band = 30
                    elif (ones_1S == 3) and (fours_4S == 2):
                        band = 30
                    elif (twos_2S == 3) and (ones_1S == 2):
                        band = 30
                    elif (twos_2S == 3) and (threes_3S == 2):
                        band = 30
                    elif (twos_2S == 3) and (fours_4S == 2):
                        band = 30
                    elif (threes_3S == 3) and (ones_1S == 2):
                        band = 30
                    elif (threes_3S == 3) and (twos_2S == 2):
                        band = 30
                    elif (threes_3S == 3) and (fours_4S == 2):
                        band = 30
                    elif (fours_4S == 3) and (ones_1S == 2):
                        band = 30
                    elif (fours_4S == 3) and (twos_2S == 2):
                        band = 30
                    elif (fours_4S == 3) and (threes_3S == 2):
                        band = 30
                    else:
                        band = 0
                             
                    if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                        orchestra = 40
                    else:
                        orchestra = 0
                    marksList = [
                        [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                        ]

                    marksP1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                    marksP2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

                    marks2 = [ marksP1, marksP2 ]
                                        
                    title = '\nCategory Scores'
                    player = ["Player 1","Player 2"]
                    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
                    psphelper.ShowTableByList(title,[],categories,marksList)

                    desired_category = (input("Enter your desired category: "))
                        
                    if desired_category == '1S'.lower():
                      del(marksP1[0])
                      marksP1.insert(0,ones_1S)
                      score_1 += ones_1S

                    elif desired_category == '2S'.lower():
                              del(marksP1[1])
                              marksP1.insert(1,twos_4S)
                              score_1 += twos_4S

                    elif desired_category == '3S'.lower():
                              del(marksP1[2])
                              marksP1.insert(2,threes_9S)
                              score_1 += threes_9S

                    elif desired_category == '4S'.lower():
                              del(marksP1[3])
                              marksP1.insert(3,fours_16S)
                              score_1 += fours_16S

                    elif desired_category == 'Trio'.lower():
                              del(marksP1[4])
                              marksP1.insert(4,trio)
                              score_1 += trio
                    elif desired_category == 'Quartet'.lower():
                              del(marksP1[5])
                              marksP1.insert(5,quartet)
                              score_1 += quartet

                    elif desired_category == 'Band'.lower():
                              del(marksP1[6])
                              marksP1.insert(6,band)
                              score_1 += band

                    elif desired_category == 'Doremi'.lower():
                              del(marksP1[7])
                              marksP1.insert(7,doremi)
                              score_1 += doremi

                    elif desired_category == 'Orchestra'.lower():
                              del(marksP1[8])
                              marksP1.insert(8,orchestra)
                              score_1 += orchestra
#========================================================================================================================================================================================
            else:
                if wordList[0] == "roll".lower():
                    del(wordList[0])
                    if (wordList[0] == '1' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        print(list_1[:5])
                        print(list_2[:5])
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '2' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '3' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '4' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '5' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])           
                    elif (wordList[0] == "1" and wordList[1] == "2") or (wordList[0] == "2" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[2])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "3" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "3"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "3" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "3"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "4" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "4"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    else:
                        print("ERROR: Invalid Input")

                    sum_1 = sum(list_1[:5])
                    ones_1S = (list_1[:5]).count(1)
                    twos_2S = (list_1[:5]).count(2)
                    twos_4S = twos_2S * 2
                    threes_3S = (list_1[:5]).count(3)
                    threes_9S = threes_3S * 3
                    fours_4S = (list_1[:5]).count(4)
                    fours_16S = fours_4S * 4
                    if (ones_1S == 3) or (twos_2S == 3) or (threes_3S == 3) or (fours_4S == 3):
                        trio = sum_1
                        
                    else:
                        trio = 0
                        

                    if (ones_1S == 4) or (twos_2S == 4) or (threes_3S == 4) or (fours_4S == 4):
                        quartet = sum_1
                        
                    else:
                        quartet = 0
                        

                    if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                        doremi = 20
                    else:
                        doremi = 0

                    if quartet > 0:
                        band = 0
                    elif (ones_1S == 3) and (twos_2S == 2):
                        band = 30
                    elif (ones_1S == 3) and (threes_3S == 2):
                        band = 30
                    elif (ones_1S == 3) and (fours_4S == 2):
                        band = 30
                    elif (twos_2S == 3) and (ones_1S == 2):
                        band = 30
                    elif (twos_2S == 3) and (threes_3S == 2):
                        band = 30
                    elif (twos_2S == 3) and (fours_4S == 2):
                        band = 30
                    elif (threes_3S == 3) and (ones_1S == 2):
                        band = 30
                    elif (threes_3S == 3) and (twos_2S == 2):
                        band = 30
                    elif (threes_3S == 3) and (fours_4S == 2):
                        band = 30
                    elif (fours_4S == 3) and (ones_1S == 2):
                        band = 30
                    elif (fours_4S == 3) and (twos_2S == 2):
                        band = 30
                    elif (fours_4S == 3) and (threes_3S == 2):
                        band = 30
                    else:
                        band = 0
                             
                    if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                        orchestra = 40
                    else:
                        orchestra = 0
                    marksList = [
                        [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                        ]

                    marksP1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                    marksP2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

                    marks2 = [ marksP1, marksP2 ]
                                        

                    title = 'Category Scores'
                    player = ["Player 1","Player 2"]
                    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
                    psphelper.ShowTableByList(title,[],categories,marksList)
                
                    desired_category = (input("Enter your desired category: "))
                        
                    if desired_category == '1S'.lower():
                      del(marksP1[0])
                      marksP1.insert(0,ones_1S)
                      score_1 += ones_1S

                    elif desired_category == '2S'.lower():
                              del(marksP1[1])
                              marksP1.insert(1,twos_4S)
                              score_1 += twos_4S

                    elif desired_category == '3S'.lower():
                              del(marksP1[2])
                              marksP1.insert(2,threes_9S)
                              score_1 += threes_9S

                    elif desired_category == '4S'.lower():
                              del(marksP1[3])
                              marksP1.insert(3,fours_16S)
                              score_1 += fours_16S

                    elif desired_category == 'Trio'.lower():
                              del(marksP1[4])
                              marksP1.insert(4,trio)
                              score_1 += trio
                    elif desired_category == 'Quartet'.lower():
                              del(marksP1[5])
                              marksP1.insert(5,quartet)
                              score_1 += quartet

                    elif desired_category == 'Band'.lower():
                              del(marksP1[6])
                              marksP1.insert(6,band)
                              score_1 += band

                    elif desired_category == 'Doremi'.lower():
                              del(marksP1[7])
                              marksP1.insert(7,doremi)
                              score_1 += doremi

                    elif desired_category == 'Orchestra'.lower():
                              del(marksP1[8])
                              marksP1.insert(8,orchestra)
                              score_1 += orchestra

          
                elif wordList[0] == "cheat".lower():
                    del(wordList[0])
                    print(wordList)
                    if (wordList == ['1','1','1','1','1']) or (wordList == ['2','2','2','2','2']) or (wordList == ['3','3','3','3','3']) or (wordList == ['4','4','4','4','4']):
                        orchestra == "40"
                        print(orchestra)
                    else:
                        print("ERROR: Invalid Input")

    turn_1 += 1
    psphelper.ClearScreen()

#Player2#======================================================================================================================================================================================
    print(' ')
    title = "Battle Of the Sexes(B.O.T.S)"
    fillchar = "="
    print(title.center(77, fillchar))

    title2 = '\nScoreboard'
    player2 = ['Player 1','Player 2']
    categories2 = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]

    psphelper.ShowTableByList(title2,player2,categories2,marks2)

    print("Player 1:" , score_1)
    print("Player 2:" , score_2)

    print("\nPlayer 2")
    print("="*8)

    enter = input('Press ENTER to roll dice.\n')

    import random
    list_1 = [1,2,3,4,5]

    for i in range(len(list_1)):
      list_1[i] = random.randint(1,4)
    print("Roll #1 : ",list_1)
    print(' ')

    sum_1 = sum(list_1[:5])
    ones_1S = (list_1[:5]).count(1)
    twos_2S = (list_1[:5]).count(2)
    twos_4S = twos_2S * 2
    threes_3S = (list_1[:5]).count(3)
    threes_9S = threes_3S * 3
    fours_4S = (list_1[:5]).count(4)
    fours_16S = fours_4S * 4
    if (ones_1S == 3) or (twos_2S == 3) or (threes_3S == 3) or (fours_4S == 3):
        trio = sum_1
        
    else:
        trio = 0
        

    if (ones_1S == 4) or (twos_2S == 4) or (threes_3S == 4) or (fours_4S == 4):
        quartet = sum_1
        
    else:
        quartet = 0
        

    if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
        doremi = 20
    else:
        doremi = 0

    if quartet > 0:
        band = 0
    elif (ones_1S == 3) and (twos_2S == 2):
        band = 30
    elif (ones_1S == 3) and (threes_3S == 2):
        band = 30
    elif (ones_1S == 3) and (fours_4S == 2):
        band = 30
    elif (twos_2S == 3) and (ones_1S == 2):
        band = 30
    elif (twos_2S == 3) and (threes_3S == 2):
        band = 30
    elif (twos_2S == 3) and (fours_4S == 2):
        band = 30
    elif (threes_3S == 3) and (ones_1S == 2):
        band = 30
    elif (threes_3S == 3) and (twos_2S == 2):
        band = 30
    elif (threes_3S == 3) and (fours_4S == 2):
        band = 30
    elif (fours_4S == 3) and (ones_1S == 2):
        band = 30
    elif (fours_4S == 3) and (twos_2S == 2):
        band = 30
    elif (fours_4S == 3) and (threes_3S == 2):
        band = 30
    else:
        band = 0
             
    if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
        orchestra = 40
    else:
        orchestra = 0

    marksList = [
        [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
        ]

    title = 'Category Scores'
    player = ["Player 1","Player 2"]
    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
    psphelper.ShowTableByList(title,[],categories,marksList)

    print("")
    print("Input Options:")
    print(" SAVE           :- Accept these dice.")
    print(" ROLL           :- Re-roll ALL dice.")
    print(" ROLL d1 ... dn :- Re-roll specified dice only.")

    input_1 = input("\nInput > ") . lower()

    wordList = input_1.split(' ')

    while wordList[0] != 'save' and wordList[0] != 'roll' and wordList[0] != 'cheat' :
        print("ERROR: Invalid Input")
        input_1 = input("Input > ") . lower()
        wordList = input_1.split(' ')
        
    if len(wordList) == 1:
        if wordList[0] == 'save'.lower():
            desired_category = (input("Enter your desired category: "))
            if desired_category == '1S'.lower():
                      del(marksP2[0])
                      marksP2.insert(0,ones_1S)
                      score_2 += ones_1S
                      

            elif desired_category == '2S'.lower():
                      del(marksP2[1])
                      marksP2.insert(1,twos_4S)
                      score_2 += twos_4S

            elif desired_category == '3S'.lower():
                      del(marksP2[2])
                      marksP2.insert(2,threes_9S)
                      score_2 += threes_9S

            elif desired_category == '4S'.lower():
                      del(marksP2[3])
                      marksP2.insert(3,fours_16S)
                      score_2 += fours_16S

            elif desired_category == 'Trio'.lower():
                      del(marksP2[4])
                      marksP2.insert(4,trio)
                      score_2 += trio
            elif desired_category == 'Quartet'.lower():
                      del(marksP2[5])
                      marksP2.insert(5,quartet)
                      score_2 += quartet

            elif desired_category == 'Band'.lower():
                      del(marksP2[6])
                      marksP2.insert(6,band)
                      score_2 += band

            elif desired_category == 'Doremi'.lower():
                      del(marksP2[7])
                      marksP2.insert(7,doremi)
                      score_2 += doremi

            elif desired_category == 'Orchestra'.lower():
                      del(marksP2[8])
                      marksP2.insert(8,orchestra)
                      score_2 += orchestra
    #-------------------------------------------------------------------------------------------------------------
    #2nd Roll for player 2
        elif wordList[0] == 'roll'.lower():
            score_1 = 0
            score_2 = 0
            
            import random
            list_1 = [1,2,3,4,5]
        
            for i in range(len(list_1)):
             list_1[i] = random.randint(1,4)
            print("Roll #2 : ",list_1)
            print(' ')
            sum_1 = sum(list_1[:5])
            ones_1S = (list_1[:5]).count(1)
            twos_2S = (list_1[:5]).count(2)
            twos_4S = twos_2S * 2
            threes_3S = (list_1[:5]).count(3)
            threes_9S = threes_3S * 3
            fours_4S = (list_1[:5]).count(4)
            fours_16S = fours_4S * 4
            if (ones_1S == 3) or (twos_2S == 3) or (threes_3S == 3) or (fours_4S == 3):
                trio = sum_1
            
            else:
                trio = 0
                

            if (ones_1S == 4) or (twos_2S == 4) or (threes_3S == 4) or (fours_4S == 4):
                quartet = sum_1
                
            else:
                quartet = 0
                

            if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                doremi = 20
            else:
                doremi = 0

            if quartet > 0:
                band = 0
            elif (ones_1S == 3) and (twos_2S == 2):
                band = 30
            elif (ones_1S == 3) and (threes_3S == 2):
                band = 30
            elif (ones_1S == 3) and (fours_4S == 2):
                band = 30
            elif (twos_2S == 3) and (ones_1S == 2):
                band = 30
            elif (twos_2S == 3) and (threes_3S == 2):
                band = 30
            elif (twos_2S == 3) and (fours_4S == 2):
                band = 30
            elif (threes_3S == 3) and (ones_1S == 2):
                band = 30
            elif (threes_3S == 3) and (twos_2S == 2):
                band = 30
            elif (threes_3S == 3) and (fours_4S == 2):
                band = 30
            elif (fours_4S == 3) and (ones_1S == 2):
                band = 30
            elif (fours_4S == 3) and (twos_2S == 2):
                band = 30
            elif (fours_4S == 3) and (threes_3S == 2):
                band = 30
            else:
                band = 0
                 
            if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                orchestra = 40
            else:
                orchestra = 0

            marksList = [
                [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                ]

            title = 'Category Scores'
            player = ["Player 1","Player 2"]
            categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
            psphelper.ShowTableByList(title,[],categories,marksList)

            print("")
            print("Input Options:")
            print(" SAVE           :- Accept these dice.")
            print(" ROLL           :- Re-roll ALL dice.")
            print(" ROLL d1 ... dn :- Re-roll specified dice only.")

            marks2 = [
                    [' ',' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' '] ]
            
            input_1 = input("\nInput > ") . lower()

            wordList = input_1.split(' ')

            while wordList[0] != 'save' and wordList[0] != 'roll' and wordList[0] != 'cheat' :
                print("ERROR: Invalid Input")
                input_1 = input("Input > ") . lower()
                wordList = input_1.split(' ')
            
            if len(wordList) == 1:
                if wordList[0] == 'save'.lower():
                    desired_category = (input("Enter your desired category: "))
                    if desired_category == '1S'.lower():
                      del(marksP2[0])
                      marksP2.insert(0,ones_1S)
                      score_2 += ones_1S
                      

                    elif desired_category == '2S'.lower():
                              del(marksP2[1])
                              marksP2.insert(1,twos_4S)
                              score_2 += twos_4S

                    elif desired_category == '3S'.lower():
                              del(marksP2[2])
                              marksP2.insert(2,threes_9S)
                              score_2 += threes_9S

                    elif desired_category == '4S'.lower():
                              del(marksP2[3])
                              marksP2.insert(3,fours_16S)
                              score_2 += fours_16S

                    elif desired_category == 'Trio'.lower():
                              del(marksP2[4])
                              marksP2.insert(4,trio)
                              score_2 += trio
                    elif desired_category == 'Quartet'.lower():
                              del(marksP2[5])
                              marksP2.insert(5,quartet)
                              score_2 += quartet

                    elif desired_category == 'Band'.lower():
                              del(marksP2[6])
                              marksP2.insert(6,band)
                              score_2 += band

                    elif desired_category == 'Doremi'.lower():
                              del(marksP2[7])
                              marksP2.insert(7,doremi)
                              score_2 += doremi

                    elif desired_category == 'Orchestra'.lower():
                              del(marksP2[8])
                              marksP2.insert(8,orchestra)
                              score_2 += orchestra
    #----------------------------------------------------------------------------------------------------------------------
    #3rd and final roll for Player 2
                elif wordList[0] == 'roll'.lower():
                    import random
                    list_1 = [1,2,3,4,5]

                    for i in range(len(list_1)):
                      list_1[i] = random.randint(1,4)
                    print("Roll #3 : ",list_1)
                    print(' ')

                    sum_1 = sum(list_1[:5])
                    ones_1S = (list_1[:5]).count(1)
                    twos_2S = (list_1[:5]).count(2)
                    twos_4S = twos_2S * 2
                    threes_3S = (list_1[:5]).count(3)
                    threes_9S = threes_3S * 3
                    fours_4S = (list_1[:5]).count(4)
                    fours_16S = fours_4S * 4
                    if (ones_1S >= 3) or (twos_2S >= 3) or (threes_3S >= 3) or (fours_4S >= 3):
                        trio = sum_1
                
                    else:
                        trio = 0
                        

                    if (ones_1S >= 4) or (twos_2S >= 4) or (threes_3S >= 4) or (fours_4S >= 4):
                        quartet = sum_1
                        
                    else:
                        quartet = 0
                        

                    if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                        doremi = 20
                    else:
                        doremi = 0

                    if quartet > 0:
                        band = 0
                    elif (ones_1S == 3) and (twos_2S == 2):
                        band = 30
                    elif (ones_1S == 3) and (threes_3S == 2):
                        band = 30
                    elif (ones_1S == 3) and (fours_4S == 2):
                        band = 30
                    elif (twos_2S == 3) and (ones_1S == 2):
                        band = 30
                    elif (twos_2S == 3) and (threes_3S == 2):
                        band = 30
                    elif (twos_2S == 3) and (fours_4S == 2):
                        band = 30
                    elif (threes_3S == 3) and (ones_1S == 2):
                        band = 30
                    elif (threes_3S == 3) and (twos_2S == 2):
                        band = 30
                    elif (threes_3S == 3) and (fours_4S == 2):
                        band = 30
                    elif (fours_4S == 3) and (ones_1S == 2):
                        band = 30
                    elif (fours_4S == 3) and (twos_2S == 2):
                        band = 30
                    elif (fours_4S == 3) and (threes_3S == 2):
                        band = 30
                    else:
                        band = 0
                     
                    if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                        orchestra = 40
                    else:
                        orchestra = 0

                    marksList = [
                        [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                        ]

                    title = 'Category Scores'
                    player = ["Player 1","Player 2"]
                    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
                    psphelper.ShowTableByList(title,[],categories,marksList)

                    marks2 = [
                            [' ',' ',' ',' ',' ',' ',' ',' ',' '],
                            [' ',' ',' ',' ',' ',' ',' ',' ',' '] ]
                
                    desired_category = (input("Enter your desired category: "))
                    
                    if desired_category == '1S'.lower():
                      del(marksP2[0])
                      marksP2.insert(0,ones_1S)
                      score_2 += ones_1S
                      

                    elif desired_category == '2S'.lower():
                              del(marksP2[1])
                              marksP2.insert(1,twos_4S)
                              score_2 += twos_4S

                    elif desired_category == '3S'.lower():
                              del(marksP2[2])
                              marksP2.insert(2,threes_9S)
                              score_2 += threes_9S

                    elif desired_category == '4S'.lower():
                              del(marksP2[3])
                              marksP2.insert(3,fours_16S)
                              score_2 += fours_16S

                    elif desired_category == 'Trio'.lower():
                              del(marksP2[4])
                              marksP2.insert(4,trio)
                              score_2 += trio
                    elif desired_category == 'Quartet'.lower():
                              del(marksP2[5])
                              marksP2.insert(5,quartet)
                              score_2 += quartet

                    elif desired_category == 'Band'.lower():
                              del(marksP2[6])
                              marksP2.insert(6,band)
                              score_2 += band

                    elif desired_category == 'Doremi'.lower():
                              del(marksP2[7])
                              marksP2.insert(7,doremi)
                              score_2 += doremi

                    elif desired_category == 'Orchestra'.lower():
                              del(marksP2[8])
                              marksP2.insert(8,orchestra)
                              score_2 += orchestra
    #===================================================================================================
            else:
                if wordList[0] == "roll".lower():
                    del(wordList[0])
                    if (wordList[0] == '1' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '2' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '3' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '4' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '5' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])           
                    elif (wordList[0] == "1" and wordList[1] == "2") or (wordList[0] == "2" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[2])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "3" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "3"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "3" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "3"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "4" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "4"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    else:
                        print("ERROR: Invalid Input")

                    sum_1 = sum(list_1[:5])
                    ones_1S = (list_1[:5]).count(1)
                    twos_2S = (list_1[:5]).count(2)
                    twos_4S = twos_2S * 2
                    threes_3S = (list_1[:5]).count(3)
                    threes_9S = threes_3S * 3
                    fours_4S = (list_1[:5]).count(4)
                    fours_16S = fours_4S * 4

                    if (ones_1S == 3) or (twos_2S == 3) or (threes_3S == 3) or (fours_4S == 3):
                        trio = sum_1
                        
                    else:
                        trio = 0
                        

                    if (ones_1S == 4) or (twos_2S == 4) or (threes_3S == 4) or (fours_4S == 4):
                        quartet = sum_1
                        
                    else:
                        quartet = 0
                        

                    if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                        doremi = 20
                    else:
                        doremi = 0

                    if quartet > 0:
                        band = 0
                    elif (ones_1S == 3) and (twos_2S == 2):
                        band = 30
                    elif (ones_1S == 3) and (threes_3S == 2):
                        band = 30
                    elif (ones_1S == 3) and (fours_4S == 2):
                        band = 30
                    elif (twos_2S == 3) and (ones_1S == 2):
                        band = 30
                    elif (twos_2S == 3) and (threes_3S == 2):
                        band = 30
                    elif (twos_2S == 3) and (fours_4S == 2):
                        band = 30
                    elif (threes_3S == 3) and (ones_1S == 2):
                        band = 30
                    elif (threes_3S == 3) and (twos_2S == 2):
                        band = 30
                    elif (threes_3S == 3) and (fours_4S == 2):
                        band = 30
                    elif (fours_4S == 3) and (ones_1S == 2):
                        band = 30
                    elif (fours_4S == 3) and (twos_2S == 2):
                        band = 30
                    elif (fours_4S == 3) and (threes_3S == 2):
                        band = 30
                    else:
                        band = 0
                             
                    if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                        orchestra = 40
                    else:
                        orchestra = 0

                    marksList = [
                        [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                        ]

                    title = 'Category Scores'
                    player = ["Player 1","Player 2"]
                    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
                    psphelper.ShowTableByList(title,[],categories,marksList)

                    marks2 = [
                            [' ',' ',' ',' ',' ',' ',' ',' ',' '],
                            [' ',' ',' ',' ',' ',' ',' ',' ',' '] ]
                
                    desired_category = (input("Enter your desired category: "))
                    
                    if desired_category == '1S'.lower():
                      del(marksP2[0])
                      marksP2.insert(0,ones_1S)
                      score_2 += ones_1S
                      

                    elif desired_category == '2S'.lower():
                              del(marksP2[1])
                              marksP2.insert(1,twos_4S)
                              score_2 += twos_4S

                    elif desired_category == '3S'.lower():
                              del(marksP2[2])
                              marksP2.insert(2,threes_9S)
                              score_2 += threes_9S

                    elif desired_category == '4S'.lower():
                              del(marksP2[3])
                              marksP2.insert(3,fours_16S)
                              score_2 += fours_16S

                    elif desired_category == 'Trio'.lower():
                              del(marksP2[4])
                              marksP2.insert(4,trio)
                              score_2 += trio
                    elif desired_category == 'Quartet'.lower():
                              del(marksP2[5])
                              marksP2.insert(5,quartet)
                              score_2 += quartet

                    elif desired_category == 'Band'.lower():
                              del(marksP2[6])
                              marksP2.insert(6,band)
                              score_2 += band

                    elif desired_category == 'Doremi'.lower():
                              del(marksP2[7])
                              marksP2.insert(7,doremi)
                              score_2 += doremi

                    elif desired_category == 'Orchestra'.lower():
                              del(marksP2[8])
                              marksP2.insert(8,orchestra)
                              score_2 += orchestra
    #1st specific roll for player 1-------------------------------------------------
    else:
        if wordList[0] == "roll":
            del(wordList[0])
            if (wordList[0] == '1' and wordList[1] == ""):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[0])
                list_1.insert(0,list_2[0])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == '2' and wordList[1] == ""):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[1])
                list_1.insert(1,list_2[1])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == '3' and wordList[1] == ""):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[2])
                list_1.insert(2,list_2[2])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == '4' and wordList[1] == ""):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[3])
                list_1.insert(3,list_2[3])
                print("\noll#2:",list_1[:5])
            elif (wordList[0] == '5' and wordList[1] == ""):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[4])
                list_1.insert(4,list_2[4])
                print("\nRoll#2:",list_1[:5])           
            elif (wordList[0] == "1" and wordList[1] == "2") or (wordList[0] == "2" and wordList[1] == "1"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[0])
                list_1.insert(0,list_2[0])
                del(list_1[1])
                list_1.insert(1,list_2[1])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "1" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "1"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[0])
                list_1.insert(0,list_2[0])
                del(list_1[2])
                list_1.insert(2,list_2[2])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "1" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "1"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[0])
                list_1.insert(0,list_2[0])
                del(list_1[3])
                list_1.insert(3,list_2[3])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "1" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "1"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[0])
                list_1.insert(0,list_2[0])
                del(list_1[4])
                list_1.insert(4,list_2[4])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "2" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "2"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[1])
                list_1.insert(1,list_2[1])
                del(list_1[2])
                list_1.insert(2,list_2[2])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "2" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "2"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[1])
                list_1.insert(1,list_2[2])
                del(list_1[3])
                list_1.insert(3,list_2[3])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "2" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "2"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[1])
                list_1.insert(1,list_2[1])
                del(list_1[4])
                list_1.insert(4,list_2[4])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "3" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "3"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[2])
                list_1.insert(2,list_2[2])
                del(list_1[3])
                list_1.insert(3,list_2[3])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "3" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "3"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[2])
                list_1.insert(2,list_2[2])
                del(list_1[4])
                list_1.insert(4,list_2[4])
                print("\nRoll#2:",list_1[:5])
            elif (wordList[0] == "4" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "4"):
                list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                random.shuffle(list_2)
                del(list_1[3])
                list_1.insert(3,list_2[3])
                del(list_1[4])
                list_1.insert(4,list_2[4])
                print("\nRoll#2:",list_1[:5])
            else:
                print("ERROR: Invalid Input")

            sum_1 = sum(list_1[:5])
            ones_1S = (list_1[:5]).count(1)
            twos_2S = (list_1[:5]).count(2)
            twos_4S = twos_2S * 2
            threes_3S = (list_1[:5]).count(3)
            threes_9S = threes_3S * 3
            fours_4S = (list_1[:5]).count(4)
            fours_16S = fours_4S * 4

            if (ones_1S == 3) or (twos_2S == 3) or (threes_3S == 3) or (fours_4S == 3):
                trio = sum_1
                
            else:
                trio = 0
                

            if (ones_1S == 4) or (twos_2S == 4) or (threes_3S == 4) or (fours_4S == 4):
                quartet = sum_1
                
            else:
                quartet = 0
                

            if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                doremi = 20
            else:
                doremi = 0

            if quartet > 0:
                band = 0
            elif (ones_1S == 3) and (twos_2S == 2):
                band = 30
            elif (ones_1S == 3) and (threes_3S == 2):
                band = 30
            elif (ones_1S == 3) and (fours_4S == 2):
                band = 30
            elif (twos_2S == 3) and (ones_1S == 2):
                band = 30
            elif (twos_2S == 3) and (threes_3S == 2):
                band = 30
            elif (twos_2S == 3) and (fours_4S == 2):
                band = 30
            elif (threes_3S == 3) and (ones_1S == 2):
                band = 30
            elif (threes_3S == 3) and (twos_2S == 2):
                band = 30
            elif (threes_3S == 3) and (fours_4S == 2):
                band = 30
            elif (fours_4S == 3) and (ones_1S == 2):
                band = 30
            elif (fours_4S == 3) and (twos_2S == 2):
                band = 30
            elif (fours_4S == 3) and (threes_3S == 2):
                band = 30
            else:
                band = 0
                     
            if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                orchestra = 40
            else:
                orchestra = 0
            marksList = [
                [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                ]

            title = '\nCategory Scores'
            player = ["Player 1","Player 2"]
            categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
            psphelper.ShowTableByList(title,[],categories,marksList)

            print("")
            print("Input Options:")
            print(" SAVE           :- Accept these dice.")
            print(" ROLL           :- Re-roll ALL dice.")
            print(" ROLL d1 ... dn :- Re-roll specified dice only.")
            
            input_1 = input("\nInput > ") . lower()

            wordList = input_1.split(' ')

            while wordList[0] != 'save' and wordList[0] != 'roll' and wordList[0] != 'cheat' :
                print("ERROR: Invalid Input")
                input_1 = input("Input > ") . lower()
                wordList = input_1.split(' ')
            
    #============================================================================================
            if len(wordList) == 1:
                if wordList[0] == 'save'.lower():
                    desired_category = (input("Enter your desired category: "))
                    if desired_category == '1S'.lower():
                      del(marksP2[0])
                      marksP2.insert(0,ones_1S)
                      score_2 += ones_1S
                      

                    elif desired_category == '2S'.lower():
                              del(marksP2[1])
                              marksP2.insert(1,twos_4S)
                              score_2 += twos_4S

                    elif desired_category == '3S'.lower():
                              del(marksP2[2])
                              marksP2.insert(2,threes_9S)
                              score_2 += threes_9S

                    elif desired_category == '4S'.lower():
                              del(marksP2[3])
                              marksP2.insert(3,fours_16S)
                              score_2 += fours_16S

                    elif desired_category == 'Trio'.lower():
                              del(marksP2[4])
                              marksP2.insert(4,trio)
                              score_2 += trio
                    elif desired_category == 'Quartet'.lower():
                              del(marksP2[5])
                              marksP2.insert(5,quartet)
                              score_2 += quartet

                    elif desired_category == 'Band'.lower():
                              del(marksP2[6])
                              marksP2.insert(6,band)
                              score_2 += band

                    elif desired_category == 'Doremi'.lower():
                              del(marksP2[7])
                              marksP2.insert(7,doremi)
                              score_2 += doremi

                    elif desired_category == 'Orchestra'.lower():
                              del(marksP2[8])
                              marksP2.insert(8,orchestra)
                              score_2 += orchestra
    #------------------------------------------------------------------------------------------------
                elif wordList[0] == 'roll'.lower():
                    
                    import random
                    list_1 = [1,2,3,4,5]

                    for i in range(len(list_1)):
                       list_1[i] = random.randint(1,4)
                   
                    print ("\nRoll #3:",list_1[:5])
                    print(' ')
                    
                    sum_1 = sum(list_1[:5])
                    ones_1S = (list_1[:5]).count(1)
                    twos_2S = (list_1[:5]).count(2)
                    twos_4S = twos_2S * 2
                    threes_3S = (list_1[:5]).count(3)
                    threes_9S = threes_3S * 3
                    fours_4S = (list_1[:5]).count(4)
                    fours_16S = fours_4S * 4
                    if (ones_1S >= 3) or (twos_2S >= 3) or (threes_3S >= 3) or (fours_4S >= 3):
                        trio = sum_1
                        
                    else:
                        trio = 0
                        

                    if (ones_1S >= 4) or (twos_2S >= 4) or (threes_3S >= 4) or (fours_4S >= 4):
                        quartet = sum_1
                        
                    else:
                        quartet = 0
                        

                    if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                        doremi = 20
                    else:
                        doremi = 0

                    if quartet > 0:
                        band = 0
                    elif (ones_1S == 3) and (twos_2S == 2):
                        band = 30
                    elif (ones_1S == 3) and (threes_3S == 2):
                        band = 30
                    elif (ones_1S == 3) and (fours_4S == 2):
                        band = 30
                    elif (twos_2S == 3) and (ones_1S == 2):
                        band = 30
                    elif (twos_2S == 3) and (threes_3S == 2):
                        band = 30
                    elif (twos_2S == 3) and (fours_4S == 2):
                        band = 30
                    elif (threes_3S == 3) and (ones_1S == 2):
                        band = 30
                    elif (threes_3S == 3) and (twos_2S == 2):
                        band = 30
                    elif (threes_3S == 3) and (fours_4S == 2):
                        band = 30
                    elif (fours_4S == 3) and (ones_1S == 2):
                        band = 30
                    elif (fours_4S == 3) and (twos_2S == 2):
                        band = 30
                    elif (fours_4S == 3) and (threes_3S == 2):
                        band = 30
                    else:
                        band = 0
                             
                    if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                        orchestra = 40
                    else:
                        orchestra = 0
                    marksList = [
                        [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                        ]
                    title = '\nCategory Scores'
                    player = ["Player 1","Player 2"]
                    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
                    psphelper.ShowTableByList(title,[],categories,marksList)

                    desired_category = (input("Enter your desired category: "))
                        
                    if desired_category == '1S'.lower():
                      del(marksP2[0])
                      marksP2.insert(0,ones_1S)
                      score_2 += ones_1S
                      

                    elif desired_category == '2S'.lower():
                              del(marksP2[1])
                              marksP2.insert(1,twos_4S)
                              score_2 += twos_4S

                    elif desired_category == '3S'.lower():
                              del(marksP2[2])
                              marksP2.insert(2,threes_9S)
                              score_2 += threes_9S

                    elif desired_category == '4S'.lower():
                              del(marksP2[3])
                              marksP2.insert(3,fours_16S)
                              score_2 += fours_16S

                    elif desired_category == 'Trio'.lower():
                              del(marksP2[4])
                              marksP2.insert(4,trio)
                              score_2 += trio
                    elif desired_category == 'Quartet'.lower():
                              del(marksP2[5])
                              marksP2.insert(5,quartet)
                              score_2 += quartet

                    elif desired_category == 'Band'.lower():
                              del(marksP2[6])
                              marksP2.insert(6,band)
                              score_2 += band

                    elif desired_category == 'Doremi'.lower():
                              del(marksP2[7])
                              marksP2.insert(7,doremi)
                              score_2 += doremi

                    elif desired_category == 'Orchestra'.lower():
                              del(marksP2[8])
                              marksP2.insert(8,orchestra)
                              score_2 += orchestra
    #====================================================================================================
            else:
                if wordList[0] == "roll".lower():
                    del(wordList[0])
                    if (wordList[0] == '1' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '2' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '3' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '4' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == '5' and wordList[1] == ""):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])           
                    elif (wordList[0] == "1" and wordList[1] == "2") or (wordList[0] == "2" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "1" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "1"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[0])
                        list_1.insert(0,list_2[0])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "3") or (wordList[0] == "3" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[2])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "2" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "2"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[1])
                        list_1.insert(1,list_2[1])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "3" and wordList[1] == "4") or (wordList[0] == "4" and wordList[1] == "3"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "3" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "3"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[2])
                        list_1.insert(2,list_2[2])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    elif (wordList[0] == "4" and wordList[1] == "5") or (wordList[0] == "5" and wordList[1] == "4"):
                        list_2 = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
                        random.shuffle(list_2)
                        del(list_1[3])
                        list_1.insert(3,list_2[3])
                        del(list_1[4])
                        list_1.insert(4,list_2[4])
                        print("\nRoll#3:",list_1[:5])
                    else:
                        print("ERROR: Invalid Input")

                    sum_1 = sum(list_1[:5])
                    ones_1S = (list_1[:5]).count(1)
                    twos_2S = (list_1[:5]).count(2)
                    twos_4S = twos_2S * 2
                    threes_3S = (list_1[:5]).count(3)
                    threes_9S = threes_3S * 3
                    fours_4S = (list_1[:5]).count(4)
                    fours_16S = fours_4S * 4
                    if (ones_1S == 3) or (twos_2S == 3) or (threes_3S == 3) or (fours_4S == 3):
                        trio = sum_1
                        
                    else:
                        trio = 0
                        

                    if (ones_1S == 4) or (twos_2S == 4) or (threes_3S == 4) or (fours_4S == 4):
                        quartet = sum_1
                        
                    else:
                        quartet = 0
                        

                    if (1 in list_1[:5]) and (2 in list_1[:5]) and (3 in list_1[:5]) and (4 in list_1[:5]):
                        doremi = 20
                    else:
                        doremi = 0

                    if quartet > 0:
                        band = 0
                    elif (ones_1S == 3) and (twos_2S == 2):
                        band = 30
                    elif (ones_1S == 3) and (threes_3S == 2):
                        band = 30
                    elif (ones_1S == 3) and (fours_4S == 2):
                        band = 30
                    elif (twos_2S == 3) and (ones_1S == 2):
                        band = 30
                    elif (twos_2S == 3) and (threes_3S == 2):
                        band = 30
                    elif (twos_2S == 3) and (fours_4S == 2):
                        band = 30
                    elif (threes_3S == 3) and (ones_1S == 2):
                        band = 30
                    elif (threes_3S == 3) and (twos_2S == 2):
                        band = 30
                    elif (threes_3S == 3) and (fours_4S == 2):
                        band = 30
                    elif (fours_4S == 3) and (ones_1S == 2):
                        band = 30
                    elif (fours_4S == 3) and (twos_2S == 2):
                        band = 30
                    elif (fours_4S == 3) and (threes_3S == 2):
                        band = 30
                    else:
                        band = 0
                             
                    if (list_1[:5] == [1,1,1,1,1]) or (list_1[:5] == [2,2,2,2,2]) or (list_1[:5] == [3,3,3,3,3]) or (list_1[:5] == [4,4,4,4,4]):
                        orchestra = 40
                    else:
                        orchestra = 0
                    marksList = [
                        [ones_1S,twos_4S,threes_9S,fours_16S,trio,quartet,band,doremi,orchestra]
                        ]

                    title = 'Category Scores'
                    player = ["Player 1","Player 2"]
                    categories = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]
                    psphelper.ShowTableByList(title,[],categories,marksList)
                
                    desired_category = (input("Enter your desired category: "))
                        
                    if desired_category == '1S'.lower():
                      del(marksP2[0])
                      marksP2.insert(0,ones_1S)
                      score_2 += ones_1S
                      

                    elif desired_category == '2S'.lower():
                              del(marksP2[1])
                              marksP2.insert(1,twos_4S)
                              score_2 += twos_4S

                    elif desired_category == '3S'.lower():
                              del(marksP2[2])
                              marksP2.insert(2,threes_9S)
                              score_2 += threes_9S

                    elif desired_category == '4S'.lower():
                              del(marksP2[3])
                              marksP2.insert(3,fours_16S)
                              score_2 += fours_16S

                    elif desired_category == 'Trio'.lower():
                              del(marksP2[4])
                              marksP2.insert(4,trio)
                              score_2 += trio
                    elif desired_category == 'Quartet'.lower():
                              del(marksP2[5])
                              marksP2.insert(5,quartet)
                              score_2 += quartet

                    elif desired_category == 'Band'.lower():
                              del(marksP2[6])
                              marksP2.insert(6,band)
                              score_2 += band

                    elif desired_category == 'Doremi'.lower():
                              del(marksP2[7])
                              marksP2.insert(7,doremi)
                              score_2 += doremi

                    elif desired_category == 'Orchestra'.lower():
                              del(marksP2[8])
                              marksP2.insert(8,orchestra)
                              score_2 += orchestra
          
                elif wordList[0] == "cheat".lower():
                    del(wordList[0])
                    print(wordList)
                    if (wordList == ['1','1','1','1','1']) or (wordList == ['2','2','2','2','2']) or (wordList == ['3','3','3','3','3']) or (wordList == ['4','4','4','4','4']):
                        orchestra == "40"
                        print(orchestra)
                    else:
                        print("ERROR: Invalid Input")
    
    turn_2 += 1
    psphelper.ClearScreen()
    

#===========================================================================================================================================================================================

print(' ')
title = "Battle Of the Sexes(B.O.T.S)"
fillchar = "="
print(title.center(77, fillchar))
title2 = '\nScoreboard'
player2 = ['Player 1','Player 2']
categories2 = ["1S","2S","3S","4S","Trio","Quartet","Band","Doremi","Orchestra"]

psphelper.ShowTableByList(title2,player2,categories2,marks2)

print("\nPlayer 1:" , score_1)
print("Player 2:" , score_2)

    

if score_1 > score_2:
    print("\nCongratulations!! Player 1 wins!!")
elif score_1 == score_2:
    print("Player 1 and Player 2 tied")
else:
    print("\nCongratulations!! Player 2 wins!!")

enter = input('\nPress ENTER to end the game.')

psphelper.ClearScreen()






        
        
        

    









    
