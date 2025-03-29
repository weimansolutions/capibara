### ESTRUCTURA BACKEND FASTAPI COMPLETA

# main.py
from fastapi import FastAPI
from app.api import auth, users, tasks
from app.db.database import create_db_and_tables

app = FastAPI(title="WebApp Modular")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(tasks.router, prefix="/tasks")



