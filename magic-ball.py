import random
import time
answers = ['здесь указать да нет и вариативность данных ответов']
print('Привет,я шарик,который знает совершенно все!')
user_name=input('Как тебя зовут---> ')

print(user_name,'велком')
while True:
    ball = input('Задайте свой вопрос -->>')
    print(random.choice(answers))
    again = input('Попробовать снова? да, нет')
    if again == 'нет':
        print('Возвращайся если возникнут вопросы!')
        break