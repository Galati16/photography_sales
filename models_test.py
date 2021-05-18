from sqlalchemy import Column, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "photography_sales_test"
database_path = "postgres://postgres:hallo@{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.session.remove()
    db.drop_all()
    db.create_all()
    # add one demo row which is helping in POSTMAN test
    image = Image(
        description='Pebbles on beach',
        active_since='2021-05-08 08:52:40'
    )
    sale = Sale(
        image_id= 1,
        sales_date='2020-05-08 08:52:40',
        income= 0.50,
        platform = 'Dreamstime'
    )
    image.insert()
    sale.insert()


'''
Image stats

'''
class Image(db.Model):  
  __tablename__ = 'images'

  id = Column(Integer, primary_key=True)
  description = Column(db.String(500), nullable=False)
  active_since = Column(db.DateTime, nullable=False)
  children = db.relationship("Sale")

  def __init__(self, description, active_since):
    self.description = description
    self.active_since = active_since

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'description': self.description,
      'active_since': self.active_since
    }

'''
Sale

'''
class Sale(db.Model):  
  __tablename__ = 'sales'

  id = Column(Integer, primary_key=True)
  image_id = Column( Integer, db.ForeignKey('images.id'))
  sales_date = Column(db.DateTime, nullable=False)
  income = Column(db.Float, nullable=False)
  platform = Column(db.String(120))
  

  def __init__(self, image_id, sales_date, income, platform):
    self.image_id = image_id
    self.sales_date = sales_date
    self.income = income
    self.platform = platform


  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'image_id': self.image_id,
      'sales_date': self.sales_date,
      'income': self.income,
      'platform': self.platform
    }