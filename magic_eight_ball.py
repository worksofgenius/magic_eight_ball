import random

print('Smarter than AI! Cheaper than a fortune teller! Ask the incredible Magic 8 Ball a question!')

question = input()

print('> ' + question + '!')

print('Well, since you asked...')

def get_answer(answer_num):
    if answer_num == 1:
      return 'It is certain'
    elif answer_num == 2:
        return 'It is decidedly so'
    elif answer_num == 3:
        return 'Yes'
    elif answer_num == 4:
        return 'Reply hazy try again'
    elif answer_num == 5:
        return 'Ask again later'
    elif answer_num == 6:
        return 'Concentrate and ask again'
    elif answer_num == 7:
        return 'My reply is no'
    elif answer_num == 8:
        return 'Outlook not so good'
    elif answer_num == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)