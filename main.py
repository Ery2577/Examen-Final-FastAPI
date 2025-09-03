from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Characteristic(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

cars_db: List[Car] = []

# a. GET : /ping
@app.get("/ping")
def ping():
    return "pong"  

# b. POST : /cars
@app.post("/cars", status_code=201)
def create_car(car: Car):
    cars_db.append(car)
    return car

# c. GET : /cars
@app.get("/cars")
def get_cars():
    return cars_db

# d. GET : /cars/{id}
@app.get("/cars/{id}")
def get_car(id: str):
    for car in cars_db:
        if car.identifier == id:
            return car
    raise HTTPException(status_code=404, detail=f"La voiture avec l'id '{id}' n'a pas été trouvée.")

# e. PUT : /cars/{id}/characteristics (Bonus)
@app.put("/cars/{id}/characteristics")
def update_car_characteristics(id: str, new_char: Characteristic):
    for car in cars_db:
        if car.identifier == id:
            car.characteristics = new_char
            return car
    raise HTTPException(status_code=404, detail=f"La voiture avec l'id '{id}' n'existe pas.")
