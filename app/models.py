from .import  db





class User(db.Model):
    __tablename__ ='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    admin=db.Column(db.Boolean)


    def __repr__(self):
        return f'User{self.username}'


class Question(db.Model):
    __tablename__ ='questions'
    id=db.Column(db.Integer,primary_key=True)
    question_text=db.Column(db.text)
    answer=db.Column(db.text)
    asked_by_id=db.Column(db.Integer,db.ForeignKey('user_id'))






