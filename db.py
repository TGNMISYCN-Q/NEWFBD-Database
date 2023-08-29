import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connection_string=os.environ['db_connection_str']

engine=create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
      }
  })

def feedback_db():
  with engine.connect() as conn:
    result_dicts=[]
    result = conn.execute(text("select * from feedback"))
    column_names = result.keys()
    for row in result:
      result_dicts.append(dict(zip(column_names, row)))
  return result_dicts

def questionform():
  with engine.connect() as conn:
    question_store=[]
    #result = conn.execute(text("select * from questionstore"))
    column_names = result.keys()
    for row in result:
      result_dicts.append(dict(zip(column_names, row)))
  return question_store


