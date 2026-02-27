#tavabe 
from sqlalchemy.orm import Session
#4 ta jadval ro mirimesh tooye in file
from models import User, Questions, Choice, Answers


#CRUD.py --> tavabe ke shoma too databse (table ) write, read


def create_user(db:Session, name:str):

    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

    #create_user(db, name='ali')
    #create_user(db,name='reza')

def create_question(db:Session,text:str):
    question = Questions(text=text)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


def add_choice(db:Session,question : Questions , text:str, is_correct= False):
    choice = Choice(text=text, is_correct=is_correct, question=question)
    db.add(choice)
    db.commit()
    db.refresh(choice)
    return choice




#tabeye read 
def list_questions(db:Session):
    #kole soal haro behet mide 
    return db.query(Questions).all()


#------
# 3 ta tabe besazid
#---->dgaggh tiozih bdid khat b khat chra

#- 2,3 saat ino zaman bzarid


def submit_answer(db: Session, user_id :int , question_id : int, choice_id:int):
    pass



def calculate_score(db:Session ,user_id:int):
    pass


def get_unanswere_qeuestions(db:Session, user_id:int):
    pass

def get_top_users(db:Session, n=3):
    pass



def reset_user_answers(db:Session, user_id:int):
    pass


def get_choice_distribution(db: Session , user_id:int):
    pass








