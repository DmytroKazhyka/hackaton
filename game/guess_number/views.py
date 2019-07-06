from django.shortcuts import render
from guess_number.models import Game
from random import randrange


def start_game(request):
    number = randrange(0, 11)
    print(number)
    game = Game.objects.create(attempts=0)
    while game.attempts < 3:

        if request.method == "POST":
            guess = int(request.POST['guess'])
            if guess == number:
                message = "Congratulations, you won the game"
            elif guess > number:
                message = 'Your number is too high'
            else:
                message = 'Your number is too low'
            return render(request, 'guess_number/guess_number.html', {'message': message, 'answer': number, 'guess': guess})
        return render(request, 'guess_number/guess_number.html')
