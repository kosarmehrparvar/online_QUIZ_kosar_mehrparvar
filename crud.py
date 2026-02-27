
from sqlalchemy.orm import Session
from models import User, Questions, Choice, Answers

# ساخت یک کاربر جدید
user = User(name="Koko")
db.add(user)      # اضافه کردن به دیتابیس
db.commit()       # ذخیره تغییرات
db.refresh(user)  # بروزرسانی شیء از دیتابیس
print(user)       # نمایش کاربر


pip install SQLAlchemydef 

create_user(db: Session, name: str):
    """ایجاد یک کاربر جدید"""
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_question(db: Session, text: str):
    """ایجاد یک سؤال جدید"""
    question = Questions(text=text)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


def add_choice(db: Session, question: Questions, text: str, is_correct=False):
    """اضافه کردن یک گزینه به یک سؤال"""
    choice = Choice(text=text, is_correct=is_correct, question=question)
    db.add(choice)
    db.commit()
    db.refresh(choice)
    return choice

def submit_answer(db: Session, user_id: int, question_id: int, choice_id: int):
    """ثبت پاسخ کاربر برای یک سؤال"""
    answer = Answers(user_id=user_id, question_id=question_id, choice_id=choice_id)
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer


def calculate_score(db: Session, user_id: int):
    """محاسبه تعداد پاسخ صحیح کاربر"""
    correct_answers = db.query(Answers).join(Choice).filter(
        Answers.user_id == user_id,
        Choice.is_correct == True,
        Answers.choice_id == Choice.id
    ).count()
    return correct_answers


def get_unanswere_qeuestions(db: Session, user_id: int):
    """لیست سؤالاتی که کاربر هنوز جواب نداده"""
    answered_questions = db.query(Answers.question_id).filter(Answers.user_id == user_id)
    unanswered_questions = db.query(Questions).filter(~Questions.id.in_(answered_questions)).all()
    return unanswered_questions


def get_top_users(db: Session, n=3):
    """ کاربر برتر بر اساس بیشترین جواب صحیح"""
    from sqlalchemy import func
    scores = db.query(
        User,
        func.count(Answers.id).label("score")
    ).join(Answers, User.id == Answers.user_id)\
     .join(Choice, Answers.choice_id == Choice.id)\
     .filter(Choice.is_correct == True)\
     .group_by(User.id)\
     .order_by(func.count(Answers.id).desc())\
     .limit(n)\
     .all()
    return [(user, score) for user, score in scores]


def reset_user_answers(db: Session, user_id: int):
    """پاک کردن تمام پاسخ‌های کاربر"""
    db.query(Answers).filter(Answers.user_id == user_id).delete()
    db.commit()
    return True


def get_choice_distribution(db: Session, user_id: int):
    """توزیع تعداد انتخاب هر گزینه توسط کاربر"""
    from sqlalchemy import func
    distribution = db.query(
        Choice.text,
        func.count(Answers.id).label("count")
    ).join(Answers, Answers.choice_id == Choice.id)\
     .filter(Answers.user_id == user_id)\
     .group_by(Choice.text)\
     .all()
    return distribution
