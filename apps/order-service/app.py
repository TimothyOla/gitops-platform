from fastapi import FastAPI

app = FastAPI(title="Order Service")

orders = [
    {"id": 1, "user_id": 1, "product_id": 1, "status": "completed"},
    {"id": 2, "user_id": 2, "product_id": 3, "status": "pending"},
]

@app.get("/")
def root():
    return {"service": "order-service", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/orders")
def get_orders():
    return orders