"""
Definition of views.
"""
from random import randint
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
# global values all to be used for the hangman game and its logic
CurrentClue = "Something"
CurrentGame = ["t","e","s","t","/","d","a","t","a"]
CurrentBoard =  ["_","_","_","_","/","_","_","_","_"]
GuessedAndWrong = []
#Lives = 6 < currently broken


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
def generateBoard(answer, clue = "Something"):
    CurrentClue = clue
    CurrentGame = [*answer.replace(" ", "/")]
    CurrentBoard =  ["_" if x != "/" else x for x in CurrentGame]
    
        
        
def hangmanRequestValidation(request):
    pass

def updateBoard(guessedLetter):
    print("world")

    numb = CurrentGame.count(guessedLetter)
    print(numb)
    lastFound = 0
    while numb > 0:
        lastFound = CurrentGame.index(guessedLetter, lastFound)
        CurrentBoard[lastFound] = guessedLetter
        print(CurrentBoard)
        numb -=1
        lastFound+=1
    print("go")
  
    
    
def failedGuess(guessedLetter):
    GuessedAndWrong.append(guessedLetter)


def hangmanRequest(request):
    correct = "untouched"
    guessedLetter = request.POST['Guess_txt'].lower()
    # take the input. checks and sanatises it
    if len(guessedLetter) == 0:
        return
        
    elif len(guessedLetter) == 1:
        if guessedLetter in CurrentGame:
            correct = "Correct"
            print("hello")
            updateBoard(guessedLetter)
        else:
            failedGuess(guessedLetter)
            #Lives = Lives - 1
            correct = "Wrong"
            
    else:
        if guessedLetter.replace(" ", "/") == "".join(CurrentGame):
            correct = "YOU FUCKING DID IT"
        else:
            failedGuess(guessedLetter)
            #Lives = Lives - 1
            correct = "Wrong"
        
        
    

    # render the page
    print(request.POST)
    return render(
        request,
        'app/hangman/play.html',
        {
            'current': " ".join(CurrentBoard)+ "  " + str(randint(0,10)),
            'correct': correct,
            "GuessedAndWrong": " ".join(GuessedAndWrong),
            'title':'Play Page',
            'year':datetime.now().year,
        }
    )



def play(request):
    if request.method =='POST':
        return hangmanRequest(request)
        
    else:    
        

        """Renders the home page."""
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/hangman/play.html',
            {
                'current':'____ / ____',
                'correct': 'Wrong',
                'title':'Play Page',

                'year':datetime.now().year,
            }
        )
    #            'HangmanStage':  str(Lives), < broken. needs to be added back to the request


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
