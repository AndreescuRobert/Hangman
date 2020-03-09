import random

def random_word(stream):
    it = iter(stream)
    result = next(it)
    for n,item in enumerate(it):
        if random.randint(0,n+1) == 0:
            result = item
    return result


file = open("words_list.txt", "r")
rw = random_word(file)
progress = []
wrong_guesses = []
for i in range(len(rw)-1):
    progress.append('_')
number_of_tries = 6
print('''
Welcome to Hang Man!!!
        
You have 6 tries to guess the word.
        
The word has ''' + str(len(rw) - 1) +  " letters: ")
print(*progress)
while number_of_tries:
    ok = 1
    for i in range(len(progress)):
        if str(progress[i]) != rw[i]:
            ok = 0
            break
    if ok:
        print('Congratulations! You have won!')
        print('The word was: ' + rw)
        break
    guess = input('Your guess is: ')
    if guess in rw:
        for i in range(len(rw)):
            if rw[i] == guess:
                progress[i] = guess
        print(guess + ' exits in the word: ')
        print(*progress)
    else:
        number_of_tries -= 1
        wrong_guesses.append(guess)
        print('Sorry, there is no ' + guess + ' in the word: ')
        print(*progress)
    print('The letters that do not exist in the word are: ')
    print(*wrong_guesses, sep = ', ')
    print('You have ' + str(number_of_tries) + ' tries remaining')
if(not number_of_tries):
    print('Sorry, you lost, the word was: ' + rw)