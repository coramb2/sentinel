# app/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database

app = FastAPI()

# dependency to get database session
def get_db():
	db = database.SessionLocal()
	try:
		yield db
	finally:
		db.close()

@app.get("/")
def read_root():
	return {"message": "Hello Sentinel!"}

@app.get("/health")
def health_check():
	return {"status": "healthy"}
