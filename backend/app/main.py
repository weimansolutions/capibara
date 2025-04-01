### ESTRUCTURA BACKEND FASTAPI COMPLETA

# main.py
from fastapi import FastAPI
from app.api import auth, users, tasks
from app.db.database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="WebApp Modular")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # o ["*"] para no restringir,  # o ["http://localhost:5173"] si querés restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(tasks.router, prefix="/tasks")



