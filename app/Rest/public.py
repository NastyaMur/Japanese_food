from fastapi import FastAPI, APIRouter
from app.Utils.db import generalPosrgresBase, engine, session, User, Order, Food

router = APIRouter()

@router.get("/order")
async def getOrders():
    list = await Order.objects.all()
    return list

@router.get("/user")
async def getUsers():
    list = await User.objects.all()
    return list

@router.get("/food")
async def getFoods():
    list = await Food.objects.all()
    return list

@router.get("/food/{food_number}")
async def getOneFood(food_number: int):
    return await Food.objects.get(number = food_number)