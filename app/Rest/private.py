from fastapi import FastAPI, APIRouter, Request, HTTPException
from sqlalchemy import inspect
from pydantic import BaseModel
from typing import Annotated
from app.Utils.db import generalPosrgresBase, engine, session, User, Order, Food

router = APIRouter()

def check_token(accessToken: str):
    if accessToken == 'Bearer AIzaSyDl9t5fkFmSeSzSw8baa0preiSntsTH6Ik=':
        return True
    else:
        return False

def errAuth():
    raise HTTPException(status_code=401, detail={ "type" : "error", "data": "Not authentication"})

class createFoodModel(BaseModel):
    name: str
    price: int
    description: str
    active: bool = True

class editFoodModel(BaseModel):
    name: str | None
    price: int | None
    description: str | None
    active: bool = True

@router.put("/food")
async def addFoods(
    data_model: createFoodModel,
    request: Request
):
    if "Authorization" in request.headers and check_token(request.headers.get('Authorization')):
        result = await Food.objects.create(
            name = data_model.name,
            price = data_model.price,
            description = data_model.description,
            active = data_model.active
        )
        raise HTTPException(status_code=201, detail={ "type" : "success", "number" : result.number})
    else:
        return errAuth()

@router.post("/food/{food_number}")
async def editFoods(
    food_number: int,
    data_model: editFoodModel,
    request: Request
):
    if "Authorization" in request.headers and check_token(request.headers.get('Authorization')):
        try:
            current_object = await Food.objects.get(number = food_number)

            await Food.objects.update_or_create(
                number = current_object.number,
                name = data_model.name if data_model.name != None else current_object.name,
                price = data_model.price if data_model.price != None else current_object.price,
                description = data_model.description if data_model.description != None else current_object.description,
                active = data_model.active if data_model.active != None else current_object.active
            )
        except:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
        raise HTTPException(status_code=302, detail={ "type" : "success"})
    else:
        return errAuth()

@router.delete("/food/{food_number}")
async def deleteFoods(
    food_number: int,
    request: Request
):
    if "Authorization" in request.headers and check_token(request.headers.get('Authorization')):
        await Food.objects.delete(number = food_number)
        raise HTTPException(status_code=200, detail={ "type" : "success"})
    else:
        return errAuth()