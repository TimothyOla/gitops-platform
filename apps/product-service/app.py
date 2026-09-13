from fastapi import FastAPI

app = FastAPI(title="Product Service")

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Phone", "price": 699.99},
    {"id": 3, "name": "Headphones", "price": 149.99},
]

@app.get("/")
def root():
    return {"service": "product-service", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/products")
def get_products():
    return products