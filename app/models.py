
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base() 		# base class for all models

class LogEvent(Base):			# creates table
	__tablename__ = "logs"		# table name

	id = Column(Integer, primary_key=True, index=True)		# auto-incrementing ID
	service = Column(String, index=True)				# indexed for faster search
	level = Column(String)
	message = Column(String)					# log message included
	timestamp = Column(DateTime, default=datetime.utcnow)		# auto timestamp
