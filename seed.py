from database import Base, engine, get_db
from crud import create_user, create_question, add_choice, list_questions

print('Creating tables...')  
Base.metadata.create_all(engine)
print('Tables created successfully')

db = get_db()

print('Creating questions...')

# سوال 1
q1 = create_question(db, text='What does the word "beneficial" mean?')
add_choice(db, q1, text='useful', is_correct=True)
add_choice(db, q1, text='difficult', is_correct=False)
add_choice(db, q1, text='harmful', is_correct=False)

# سوال 2
q2 = create_question(db, text='What does the word "reliable" mean?')
add_choice(db, q2, text='strange', is_correct=False)
add_choice(db, q2, text='weakness', is_correct=False)
add_choice(db, q2, text='Trustworthy', is_correct=True)

# سوال 3
q3 = create_question(db, text='What does the word "improve" mean?')
add_choice(db, q3, text='ignore', is_correct=False)
add_choice(db, q3, text='fix', is_correct=False)
add_choice(db, q3, text='get better', is_correct=True)

# سوال 4
q4 = create_question(db, text='What does the word "ancient" mean?')
add_choice(db, q4, text='modern', is_correct=False)
add_choice(db, q4, text='old', is_correct=True)
add_choice(db, q4, text='expensive', is_correct=False)

print('Questions created successfully')
print('Finalizing...')
