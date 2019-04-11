from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , String, Integer, Text

engine = create_engine('mysql+pymysql://root@localhost:3306/seiya?charset=utf8')
print(engine)
Base = declarative_base()

class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer,primary_key = True)
    title = Column(String(64))
    city = Column(String(64))
    salary_lower = Column(Integer)
    salary_upper = Column(Integer)
    exprience_lower = Column(Integer)
    exprience_upper = Column(Integer)
    education = Column(String(16))
    tags = Column(String(256))
    company = Column(String(32))

Base.metadata.create_all(engine)

