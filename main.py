from database import Base , engine, get_db
from crud import create_user, create_question, add_choice, list_questions
from models import User, Questions, Choice, Answers

db = get_db()


print(' online quiz ')
print('let's get it started')

name = input('enter your name/user_name: ')

usr1 = create_user(db, name = name)

questions = list_questions(db)


for q in questions:
    print(f'{q.id} - {q.text}')

    #q.choice
    for c in q.choice:
        print(f'{c.id} - {c.text}')
        
 #answer = input('entery your answer:')
