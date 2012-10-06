from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER, 	DATE, VARCHAR

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

engine = create_engine('mysql://ganyue:stulistening@localhost/listening?charset=utf8')

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class BBC(Base):
	__tablename__ = 'BBC'

	indexID = Column(INTEGER, primary_key = True)
	date = Column(DATE)
	title = Column(VARCHAR)
	fileName = Column(VARCHAR)

	def __init__(self, indexID, date, title, fileName):
		self.indexID = indexID
		self.date = date
		self.title = title
		self.fileName = fileName
	'''
	def __repr__(self):
		return [self.indexID, self.date, self.title, self.fileName]
	'''
BBC_table = BBC.__table__
metadata = Base.metadata

if __name__ == '__main__':
	metadata.create_all(engine)
