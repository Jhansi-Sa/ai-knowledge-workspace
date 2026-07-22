from fastapi import FastAPI
from app.api.health import router
from app.api.v1.users.router import router as users_router
from app.core.database import Base, engine
from app.api.v1.users import models

print("Loading metadata")
print(Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)
print("Finished create_all()")

app= FastAPI()
app.include_router(router)
app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "Welcome to AI Knowledge Workspace"}

@app.get("/version")
def get_version():
    return {"version": "1.0.0"}

@app.get("/about")
def get_about():
    return {"project": "AI Knowledge Workspace"}