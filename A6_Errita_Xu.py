# Errita Xu
# Friday, March 10, 2023
# A6 - Concentration Card Matching Game
# To create a single screen, interactive, and useful app using GUI and widgets

#import important libraries
import tkinter
from tkinter import *
import random

class MyWindow():
    #define global lists that will be important throughout the program
    global cardNames, difficulty_choices, easy, medium, hard
    cardNames = ['A1','A2','A3','A4','B1','B2','B3','B4','C1','C2','C3','C4']
    difficulty_choices = ["Easy", "Medium", "Hard"]
    easy = ['1', '3', '5', '7', '9', '0']
    medium = ['ty', 'lc', 'oq', 'pn', 'bc', 'eg']
    hard = ['✬⁎', '❈?', '♙❉', '↯✸', '❁✣', '✿♪']
    
    
    #__init__() - to create screen and all attributes & widgets for the game (constructor)
    #@param: self:MyWindow, wn:window
    #@return: none
    def __init__(self, wn):
        
        #create windown attribute
        self.wn=wn
        
        #define variables that store font style & size combinations
        f1 = ('Cardigan', 50)
        f2 = ('Helvetica Neue Condensed Black', 20)
        f3 = ('Andale Mono', 12)
        f4 = ('Andale Mono', 14)
        f5 = ('Andale Mono', 16)
        
        #clear txt file --> clear for the new game
        open('concentration_data.txt', 'w').close()
        
        #create frame 1
        #to display the game's title
        frameOne = Frame(self.wn, bg='powder blue', width=500, height=75)
        frameOne.grid(row=0, columnspan=2)
        frameOne.pack_propagate(False)     #pack propogate --> frame won't resize with other widgets
        #create label for game title
        self.title = Label(frameOne, text='Concentration!', bg='powder blue', font=f1)
        self.title.pack()
        self.title.place(relx=0.5, rely=0.5, anchor=CENTER)     #centers the label
        
        #create frame 2
        #to display the instructions to the game
        frameTwo = Frame(self.wn, bg='lavender', width=250, height=165)
        frameTwo.grid(row=1, column=0)
        frameTwo.pack_propagate(False)
        #create a label for title
        self.instructions_title = Label(frameTwo, text='Instructions', bg='lavender', font=f2, fg='black')
        self.instructions_title.pack(pady=(12,3))
        #create a label for the game's instruction (use \n to create new lines)
        self.instructions = Label(frameTwo, text='1) Select level of difficulty \n 2) Enter and submit 2 cards \n 3) The cards will flip. Click \n Submit/Next button to unflip \n 4) Click Submit/Next to cue the \n computer and unflip the cards \n 6) Continue until all matched!', bg='lavender', font=f3, fg='black')
        self.instructions.pack()
        
        #create frame 3
        #to allow the player to choose a level of difficulty
        frameThree = Frame(self.wn, bg='misty rose', width=250, height=165)
        frameThree.grid(row=1, column=1)
        frameThree.pack_propagate(False)
        
        #create label for title
        self.difficulty_title = Label(frameThree, text='Choose Difficulty Level:', bg='misty rose', font=f2, fg='black')
        self.difficulty_title.pack(pady=(12,3))
        
        #set inital value for the chosen level
        self.level = ''
        
        #create ratio button for each possible level (easy, medium, hard)
        self.radio = IntVar()
        for i in range(0,len(difficulty_choices)):
            self.difficultyChoices = Radiobutton(frameThree, text=difficulty_choices[i], font=f4, variable=self.radio, value=i+1, bg='misty rose')
            self.difficultyChoices.pack()
            
        #button to submit chosen difficulty level --> triggers self.submit_difficulty()
        self.difficulty_button = Button(frameThree, text="Submit", command=self.submit_difficulty)
        self.difficulty_button.pack(pady=(10,0))

        #create main frame (4)
        #contains 12 smaller frame; one frame per card
        frameMain = Frame(self.wn, width=500, height=325)
        frameMain.grid(row=2, columnspan=2)
        frameMain.pack_propagate(False)
        
        #create A1's frame and its corresponding label
        frameA1 = Frame(frameMain, width=75, height=75, relief=GROOVE, borderwidth=15)
        frameA1.grid(row=0, column=0, padx=(50,15), pady=(30,15))     #additional padding for certain widgets based on position
        frameA1.pack_propagate(False)
        self.labelA1 = Label(frameA1, text='A1', font=f2)     #label for the card's "backside"
        self.labelA1.place(relx=0.5, rely=0.5, anchor=CENTER)     #centers the label
        
        #create A2's frame and its corresponding label
        frameA2 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameA2.grid(row=0, column=1, padx=15, pady=(30,15))
        frameA2.pack_propagate(False)
        self.labelA2 = Label(frameA2, text='A2', font=f2)
        self.labelA2.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create A3's frame and its corresponding label
        frameA3 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameA3.grid(row=0, column=2, padx=15, pady=(30,15))
        frameA3.pack_propagate(False)
        self.labelA3 = Label(frameA3, text='A3', font=f2)
        self.labelA3.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create A4's frame and its corresponding label
        frameA4 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameA4.grid(row=0, column=3, padx=(15,50), pady=(30,15))
        frameA4.pack_propagate(False)
        self.labelA4 = Label(frameA4, text='A4', font=f2)
        self.labelA4.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create B1's frame and its corresponding label
        frameB1 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameB1.grid(row=1, column=0, padx=(50,15), pady=15)
        frameB1.pack_propagate(False)
        self.labelB1 = Label(frameB1, text='B1', font=f2)
        self.labelB1.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create B2's frame and its corresponding label
        frameB2 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameB2.grid(row=1, column=1, padx=15, pady=15)
        frameB2.pack_propagate(False)
        self.labelB2 = Label(frameB2, text='B2', font=f2)
        self.labelB2.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create B3's frame and its corresponding label
        frameB3 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameB3.grid(row=1, column=2, padx=15, pady=15)
        frameB3.pack_propagate(False)
        self.labelB3 = Label(frameB3, text='B3', font=f2)
        self.labelB3.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create B4's frame and its corresponding label
        frameB4 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameB4.grid(row=1, column=3, padx=(15,50), pady=15)
        frameB4.pack_propagate(False)
        self.labelB4 = Label(frameB4, text='B4', font=f2)
        self.labelB4.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create C1's frame and its corresponding label
        frameC1 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameC1.grid(row=2, column=0, padx=(50,15), pady=(15,30))
        frameC1.pack_propagate(False)
        self.labelC1 = Label(frameC1, text='C1', font=f2)
        self.labelC1.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create C2's frame and its corresponding label
        frameC2 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameC2.grid(row=2, column=1, padx=15, pady=(15,30))
        frameC2.pack_propagate(False)
        self.labelC2 = Label(frameC2, text='C2', font=f2)
        self.labelC2.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create C3's frame and its corresponding label
        frameC3 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameC3.grid(row=2, column=2, padx=15, pady=(15,30))
        frameC3.pack_propagate(False)
        self.labelC3 = Label(frameC3, text='C3', font=f2)
        self.labelC3.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create C4's frame and its corresponding label
        frameC4 = Frame(frameMain, width=75, height=75, relief = GROOVE, borderwidth=15)
        frameC4.grid(row=2, column=3, padx=(15,50), pady=(15,30))
        frameC4.pack_propagate(False)
        self.labelC4 = Label(frameC4, text='C4', font=f2)
        self.labelC4.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #attribute that stores each card's respective label for easy access
        self.cardLabels = [self.labelA1, self.labelA2, self.labelA3, self.labelA4, self.labelB1, self.labelB2, self.labelB3, self.labelB4, self.labelC1, self.labelC2, self.labelC3, self.labelC4]

        #create frame 5
        #to allow the user to enter their card guesses
        frameFive = Frame(self.wn, bg='light goldenrod yellow', width=500, height=150)
        frameFive.grid(row=3, columnspan=2)
        frameFive.pack_propagate(False)
        
        #create label for title
        self.guess_lbl = Label(frameFive, text='Guess:', bg='light goldenrod yellow', font=f2, fg='black')
        self.guess_lbl.grid(row=0, columnspan=2, pady=(10,5))
        
        #card no.1 entry box
        self.enter_guessOne = Entry(frameFive, width=15)
        self.enter_guessOne.grid(row=1, column=0, padx=(90,12.5))
        #card no.2 entry box
        self.enter_guessTwo = Entry(frameFive, width=15)
        self.enter_guessTwo.grid(row=1, column=1, padx=(12.5,90))
        
        #create frame 6
        #to allow the user to submit and progress the game clicking a button
        frameSix = Frame(self.wn, bg='light goldenrod yellow', width=500, height=50)
        frameSix.grid(row=4, columnspan=2)
        frameSix.pack_propagate(False)
        
        #create submission/next button --> triggers self.submit_next()
        self.submit_guess = Button(frameSix,text="Submit/Next",command=self.submit_next)        
        self.submit_guess.pack()
        self.submit_guess.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create frame 7
        #to output game results throughout the game (ex: invalid input, computer's choices, successful match, etc.)
        frameSeven = Frame(self.wn, bg='honeydew2', width=500, height=100)
        frameSeven.grid(row=5, columnspan=2)
        frameSeven.pack_propagate(False)
        #create results label --> configured accordingly throughout the program
        self.results_lbl = Label(frameSeven, text = '', bg='honeydew2', font=f5, fg='black')
        self.results_lbl.pack()
        self.results_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #stores the game's shuffled cards' position
        self.card_positions = []
        #stores the user's two guesses (updated per turn)
        self.list_userGuess = []
        #stores the computer's two guesses (updated per turn)
        self.list_computerGuess = []
        
        #the index values of user/computer's card guesses
        self.user_indexOne = 0
        self.user_indexTwo = 0
        self.computer_indexOne = 0
        self.computer_indexTwo = 0
        
        #track whose turn it is (user/computer)
        self.player = 'user'
        
        #attribute that tracks if previous player made a match and thus the cards shouldn't be unflipped the cards (boolean)
        self.skip_computer = False
        self.skip_user = False
        
        #stores the cards that have been successfully matched (not in play anymore)
        self.finished = []
    
    
    #submit_difficulty() - to retrieve the level chosen by the user and trigger self.randomize_cards() method
    #@param: self:MyWindow
    #@return: none
    def submit_difficulty(self):
        
        #level has not been chosen yet
        if self.level =='':
            #value corresponding to the selected choice
            val = self.radio.get()
            #if the user didn't select a difficulty level but clicked submit
            if val==0:
                self.results_lbl.config(text='Select a level before submitting!')
            
            else:
                #determine chosen level based on index value
                self.level = difficulty_choices[val-1]
                #display confirmation of chosen level to user
                self.results_lbl.config(text='Difficulty Level: {}'. format(self.level))
                #trigger self.randomize_cards() to shuffle and create card deck
                self.randomize_cards()        
        
        #level has already been chosen (no changes to preceding deck/progress will change)
        else:
            self.results_lbl.config(text='You already chose a level! To play, \n use the entries/submission button below.')
    
    
    #randomize_cards() - to randomize a deck of cards based on the chosen difficulty level
    #@param: self:MyWindow
    #@return: none
    def randomize_cards(self):
        
        #create list of 12 cards based on chosen difficulty level
        if self.level == 'Easy':
            options = easy*2
        elif self.level == 'Medium':
            options = medium*2
        elif self.level == 'Hard':
            options = hard*2
        
        #shuffle card deck
        random.shuffle(options)
        
        #create 2D list with each card's "backside"
        self.card_positions = [['A1'], ['A2'], ['A3'], ['A4'], ['B1'], ['B2'], ['B3'], ['B4'], ['C1'], ['C2'], ['C3'], ['C4']]
        
        #add the shuffled card deck to the 2D list in order
        for i in range(0, 12):
            self.card_positions[i].append(options[i])
        
        
    #clear_guess() - to clear the user's guessing entry boxes
    #@param: self:MyWindow
    #@return: none
    def clear_guess(self):
        self.enter_guessOne.delete(0, END)
        self.enter_guessTwo.delete(0, END)     
             
                    
    #submitGuess() - to retrieve the two guesses inputted by the user and run self.userMain() if valid card name & still in play
    #@param: self:MyWindow
    #@return: none
    def submit_next(self):
        
        if self.player =='user':
            #get guessed values from entry boxes
            guessOne = self.enter_guessOne.get()     
            guessTwo = self.enter_guessTwo.get()
            #reset user's guess list
            self.list_userGuess = []
            
            if guessOne!=guessTwo and guessOne in cardNames and guessOne not in self.finished and guessTwo in cardNames and guessTwo not in self.finished and self.level != '':
                #add the two guessed cards to list
                self.list_userGuess = [guessOne, guessTwo]
                #clear entry boxes
                self.clear_guess()
                #call function to flip guessed cards & configure card labels
                self.userMain()
                
                #if the game is not over
                if self.player !='done':
                    #reassign self.player's value
                    self.player = 'user 2'
            
            #all elifs below deal with invalid input and requests the user to re-enter guesses
            elif self.level == '':
                self.results_lbl.config(text='Choose a level first!')
            elif guessOne =='' or guessTwo=='':
                self.results_lbl.config(text='Input two guesses!')
            elif guessOne==guessTwo:                 
                self.results_lbl.config(text='Input two DIFFERENT cards!')
            elif guessOne not in cardNames or guessTwo not in cardNames:
                self.results_lbl.config(text='Invalid card name!')
            elif guessOne in self.finished or guessTwo in self.finished:
                self.results_lbl.config(text='Card is not in play anymore!')
            
        elif self.player == 'user 2':
            
            #if the cards didn't match, configure labels to "unflip" the user's cards
            if self.skip_user == False:
                self.cardLabels[self.user_indexOne].config(text=self.card_positions[self.user_indexOne][0], fg='black')
                self.cardLabels[self.user_indexTwo].config(text=self.card_positions[self.user_indexTwo][0], fg='black')
            
            #notify the user of the computer's turn
            self.results_lbl.config(text='It\'s the computer\'s turn now!')
            #reassign self.player's value
            self.player = 'computer'
        
        #cards guessed by the computer need to be flipped and tested
        elif self.player == 'computer':
            #run function to randomize the computer's guesses and check them
            self.computerMoves()
            
            #if the game is not over
            if self.player!='done':
                #reassign self.player's value
                self.player = 'computer 2'
              
        elif self.player == 'computer 2':
            
            #if the cards didn't match, configure labels to "unflip" the computer's cards
            if self.skip_computer == False:
                self.cardLabels[self.computer_indexOne].config(text=self.card_positions[self.computer_indexOne][0], fg='black')
                self.cardLabels[self.computer_indexTwo].config(text=self.card_positions[self.computer_indexTwo][0], fg='black')
            
            #cue the user to submit another pair of cards
            self.results_lbl.config(text='Your Turn!')
            #reassign self.player's value
            self.player = 'user'
        
        #the game is complete
        elif self.player=='done':
            self.results_lbl.config(text='The game is done!')
    
    
    #userMain() - to evaluate the two cards guessed by the user and identify a match
    #@param: self:MyWindow
    #@return: none
    def userMain(self):
        
        indexOne = cardNames.index(self.list_userGuess[0])     #identify the card's corresponding index value
        cardOne = self.card_positions[indexOne][1]     #identify the card's backside value
        self.user_indexOne = indexOne
        self.cardLabels[indexOne].config(text=self.card_positions[indexOne][1], fg='blue')     #configure to show the frontside - 'flip' + change to blue so its easy to see
        
        indexTwo = cardNames.index(self.list_userGuess[1])     #identify the corresponding index value
        cardTwo = self.card_positions[indexTwo][1]     #identify the card's frontside value
        self.user_indexTwo = indexTwo
        self.cardLabels[indexTwo].config(text=self.card_positions[indexTwo][1], fg='blue')     #configure to show the frontside - 'flip' + change to blue so its easy to see
    
        #the two guesses match
        if cardOne == cardTwo:
            #the cards shouldn't be unflipped
            self.skip_user = True
            #configure label to notify user
            self.results_lbl.config(text='{} and {} are both {}!'. format(self.list_userGuess[0], self.list_userGuess[1], cardOne))
            #add the move to the working txt file
            self.add_data('user', self.list_userGuess[0], self.list_userGuess[1], True)
            
            #add new successfully matched cards to list
            self.finished.append(self.list_userGuess[0])
            self.finished.append(self.list_userGuess[1])
            
            #change "out of play" cards to red
            self.cardLabels[indexOne].config(fg='red')
            self.cardLabels[indexTwo].config(fg='red')
            
            #check if the game is over
            if self.checkWinner() == True:
                self.player='done'
                self.printWinner()
        
        #the two guesses don't match
        else:
            #the cards should be unflipped
            self.skip_user = False
            #configure label to notify user
            self.results_lbl.config(text='{} and {} are different!'. format(self.list_userGuess[0], self.list_userGuess[1]))
            #add the move to the working txt file
            self.add_data('user', self.list_userGuess[0], self.list_userGuess[1], False)
    
    
    #computerMoves() - to randomize the computer's guesses and identify a match
    #@param: self:MyWindow
    #@return: none
    def computerMoves(self):
        
        #reset the computer's guessing list
        self.list_computerGuess = []
        
        #randomize two guesses
        for i in range(0, 2):
            while True:
                #randomly generate a card
                choice = random.choice(cardNames)
                #ensure validity of the randomly guessed card
                if choice not in self.list_computerGuess and choice not in self.finished:
                    self.list_computerGuess.append(choice)
                    break
                
        indexOne = cardNames.index(self.list_computerGuess[0])     #identify the corresponding index value for guess 1
        self.computer_indexOne = indexOne
        cardOne = self.card_positions[indexOne][1]     #identify the card's name
        self.cardLabels[indexOne].config(text=self.card_positions[indexOne][1], fg='blue')     #configure to show the frontside - 'flip' + change to blue so its easy to see
        
        indexTwo = cardNames.index(self.list_computerGuess[1])     #identify the corresponding index value for guess 2
        self.computer_indexTwo = indexTwo
        cardTwo = self.card_positions[indexTwo][1]     #identify the card's name
        self.cardLabels[indexTwo].config(text=self.card_positions[indexTwo][1], fg='blue')     #configure to show the frontside - 'flip' + change to blue so its easy to see
    
        #the two guesses match
        if cardOne == cardTwo:
            #cards shouldn't be unflipped
            self.skip_computer = True
            #configure label to notify user
            self.results_lbl.config(text='The computer guesed {} and {}, \n which are both {}!'. format(self.list_computerGuess[0], self.list_computerGuess[1], cardOne))
            #add the move to the working txt file
            self.add_data('computer', self.list_computerGuess[0], self.list_computerGuess[1], True)
            
            #add new successfully matched cards to list
            self.finished.append(self.list_computerGuess[0])
            self.finished.append(self.list_computerGuess[1])
            
            #change "out of play" cards to red
            self.cardLabels[indexOne].config(fg='red')
            self.cardLabels[indexTwo].config(fg='red')
            
            #check if the game is over
            if self.checkWinner() == True:
                self.player='done'
                self.printWinner()
        
        #the two guesses don't match
        else:
            #cards will need to be unflipped
            self.skip_computer = False
            #configure label to notify user
            self.results_lbl.config(text='The computer guessed {} and {}, \n which are different!'. format(self.list_computerGuess[0], self.list_computerGuess[1]))
            #add the move to the working txt file
            self.add_data('computer', self.list_computerGuess[0], self.list_computerGuess[1], False)
            
            
    #add_data() - to add data of each player's turn to a txt file
    #@param: self:MyWindow, player:str, g1:str, g2:str, status:bool
    #@return: none
    def add_data(self, player, g1, g2, status):
        
        #open the txt file
        f = open('concentration_data.txt','a')
        #items that will be added - parameters
        a = [player, g1, g2, status]
        #add the new values with a tab between each value
        for i in range(0,4):
            f.write(str(a[i])+"\t")
        f.write('\n')
        f.close()
    
    
    #checkWinner() - to check if the game is done by seeing how many cards have been matched
    #@param: self:MyWindow
    #@return: bool
    def checkWinner(self):
        
        #since there are 12 cards, if less than 12 have been matched, there are still unmatched cards
        if len(self.finished) < 12:
            return False
        else:
            return True
            
            
    #printWinner() - to read the txt file to determine each player's point count
    #@param: self:MyWindow
    #@return: none
    def printWinner(self):
        
        #open the txt file
        f = open('concentration_data.txt')
        #read the lines
        lines = f.readlines()
        #close the txt file
        f.close()
        
        #inital values of counters
        user_count = 0
        computer_count = 0
        
        #store correctedly formatted information
        data = []
            
        #list within list for each line - split text from each row
        for i in range(0, len(lines)):
            #split text
            data.append(lines[i].split('\t'))
            #pop the \n values
            data[i].pop(4)
        
        #check the data list to determine when and who guessed correct matches
        for i in range(0, len(data)):
            #when a match was made...
            if data[i][3] == 'True':
                #user guessed correctly
                if data[i][0]=='user':
                    user_count +=1
                #computer guessed correctly
                elif data[i][0]=='computer':
                    computer_count +=1
        
        #determine the results based on the number of points the user has in comparison to the computer
        if user_count > computer_count:
            string = 'Congrats! You won!'
        elif user_count < computer_count:
            string = 'The computer won this time... \n try again soon!'
        elif user_count == computer_count:
            string = 'Its a tie!'
        
        #configure label to display the results
        self.results_lbl.config(text = string)

#create window & start the game
window = Tk()
win = MyWindow(window)
window.title('A6 - Concentration!')
window.geometry('500x800')
window.mainloop()