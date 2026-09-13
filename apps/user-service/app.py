from fastapi import FastAPI

app = FastAPI(title="User Service")

users = [
    {"id": 1, "name": "Timothy Ola", "email": "timothy@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"},
]

@app.get("/")
def root():
    return {"service": "user-service", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/users")
def get_users():
    return users