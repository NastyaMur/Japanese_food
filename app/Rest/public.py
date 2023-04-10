from fastapi import FastAPI, APIRouter, Request, HTTPException
from pydantic import BaseModel
from app.Utils.db import generalPosrgresBase, engine, session, User, Order, Food
from app.Utils.auth import *

router = APIRouter()

@router.get("/food")
async def getFoods():
    list = await Food.objects.all()
    return list

@router.get("/food/{food_number}")
async def getOneFood(food_number: int):
    return await Food.objects.get(number = food_number)

class login_user(BaseModel):
    email: str
    hash_pass: str

@router.post("/login")
async def getLogin(
    data_model : login_user,
    request: Request
):
    current_user = await User.objects.get_or_none(email = data_model.email, password = data_model.hash_pass)

    if current_user != None:
        return await createAuth( str( current_user.email ) )
    else:
        return errAuth()