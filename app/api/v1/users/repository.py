from .schemas import UserCreate

db=["admin@gmail.com", "test@gmail.com", "john@gmail.com"]

def save_user_to_database(user: UserCreate):
    db.append(user.email)
    return {"id": db.index(user.email) + 1,
            "name": user.name,
            "email":user.email
    }

def user_exists_by_email(email:str):
    if email in db: #just taken a db as reference
        return True
    return False