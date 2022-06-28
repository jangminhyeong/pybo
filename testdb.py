from pybo.models import Question,Answer
from datetime import datetime
from pybo import db

def test():
    q = Question(subject='질문 1입니다.',content='질문1에 대한 내용입니다.', create_date=datetime.now())
    db.session.add(q)
    db.session.commit()

def test1():
    for temp in range(1,11):
        s='질문{} 입니다.'.format(temp)
        c='질문내용 {}입니다.'.format(temp)
        q=Question(subject=s,content=c, create_date=datetime.now())
        db.session.add(q)

    db.session.commit()

def getall_question():
    result = Question.query.all()

    #for temp in result:
        #print(temp.subject)
        #print(temp.content)

