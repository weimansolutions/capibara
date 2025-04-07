### ESTRUCTURA BACKEND FASTAPI COMPLETA

# main.py
from fastapi import FastAPI
from app.db.database import create_db_and_tables
from app.db.init_db import init_superadmin
from app.db.database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import users, companies, auth,modules, roles, permissions  # al inicio


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
    db = SessionLocal()
    init_superadmin(db)
    db.close

app.include_router(users.router)
app.include_router(companies.router)
app.include_router(auth.router)
app.include_router(modules.router)
app.include_router(roles.router)
app.include_router(permissions.router)

