from sqlalchemy.orm import Session
from app.models.users import User
from app.core.security import get_password_hash

def init_superadmin(db: Session):
    existing = db.query(User).filter(User.is_superadmin == True).first()
    if existing:
        return

    superadmin = User(
        username="admin",
        email="admin@example.com",
        name = "admin",
        lastname = "admin",
        hashed_password=get_password_hash("admin123"),  # Podés usar .env para esto
        is_superadmin=True,
        is_active=True
    )
    db.add(superadmin)
    db.commit()
    print("✅ Superadmin creado.")
