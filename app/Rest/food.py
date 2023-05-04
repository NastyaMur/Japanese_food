from fastapi import FastAPI, APIRouter, Request, HTTPException
from sqlalchemy import inspect
from pydantic import BaseModel
from datetime import datetime,timezone
from app.Utils.db import generalPosrgresBase, engine, session, User, Order, Food, Auth, Role, Category
from app.Utils.orderFlow import *
from app.Utils.auth import *
import json
import base64
import uuid

router = APIRouter()

class createFoodModel(BaseModel):
    name: str
    price: int
    weight: int
    description: str | None
    photo: str | None
    category: str
    active: bool = True
    popular: bool = False

class editFoodModel(BaseModel):
    name: str | None
    price: int | None
    weight: int | None
    category: str | None
    photo: str | None
    description: str | None
    active: bool | None
    popular: bool | None

@router.put("/")
async def addFoods(
    data_model: createFoodModel,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):

        category = await Category.objects.get_or_none(code = data_model.category)

        result = await Food.objects.create(
            name = data_model.name,
            price = data_model.price,
            description = data_model.description,
            category = category.code,
            weight = data_model.weight,
            active = data_model.active,
            popular = data_model.active
        )
        raise HTTPException(status_code=201, detail={ "type" : "success", "number" : result.number})
    else:
        return errAuth()

@router.post("/{food_number}")
async def editFoods(
    food_number: int,
    data_model: editFoodModel,
    request: Request
):
    if "Authorization" in request.headers and check_token(request.headers.get('Authorization')):
        try:
            current_object = await Food.objects.get(number = food_number)

            category = await Category.objects.get_or_none(code = data_model.category)

            await Food.objects.update_or_create(
                number = current_object.number,
                name = data_model.name if data_model.name != None else current_object.name,
                price = data_model.price if data_model.price != None else current_object.price,
                weight = data_model.weight if data_model.weight != None else current_object.weight,
                description = data_model.description if data_model.description != None else current_object.description,
                active = data_model.active if data_model.active != None else current_object.active,
                photo = data_model.photo if data_model.photo != None else current_object.photo,
                popular = data_model.popular if data_model.popular != None else current_object.popular,
                category = category.code if category != None else current_object.category
            )
        except:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
        raise HTTPException(status_code=302, detail={ "type" : "success"})
    else:
        return errAuth()

@router.delete("/{food_number}")
async def deleteFoods(
    food_number: int,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        await Food.objects.delete(number = food_number)
        raise HTTPException(status_code=200, detail={ "type" : "success"})
    else:
        return errAuth()

@router.get("/")
async def getFoods(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        allFood = await Food.objects.all()
        return_food = []
        for food_object in allFood:
            category_object = await Category.objects.get_or_none(code = food_object.category)
            
            if category_object:
                return_category = {
                    'name': category_object.name,
                    'code': category_object.code
                }
            else:
                return_category = {}

            return_food.append({
                "number": food_object.number,
                "name": food_object.name,
                "photo": food_object.photo,
                "category": return_category,
                "price": food_object.price,
                "description": food_object.description,
                "weight": food_object.weight,
                "active": food_object.active,
                "popular": food_object.popular
            })

    else:
        allFood = await Food.objects.all(active = True)
        return_food = []
        for food_object in allFood:
            category_object = await Category.objects.get_or_none(code = food_object.category)
            
            if category_object:
                return_category = {
                    'name': category_object.name,
                    'code': category_object.code
                }
            else:
                return_category = {}

            return_food.append({
                "number": food_object.number,
                "name": food_object.name,
                "photo": food_object.photo,
                "category": return_category,
                "price": food_object.price,
                "description": food_object.description,
                "weight": food_object.weight,
            })

    return return_food

@router.get("/popular")
async def getPopularFoods(
    request: Request
):

    allFood = await Food.objects.all(active = True, popular = True)
    return_food = []
    for food_object in allFood:
        category_object = await Category.objects.get_or_none(code = food_object.category)
        
        if category_object:
            return_category = {
                'name': category_object.name,
                'code': category_object.code
            }
        else:
            return_category = {}

        return_food.append({
            "number": food_object.number,
            "name": food_object.name,
            "photo": food_object.photo,
            "category": return_category,
            "price": food_object.price,
            "description": food_object.description,
            "weight": food_object.weight,
        })

    return return_food


@router.get("/{food_number}")
async def getOneFood(
    food_number: int,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        try:
            return await Food.objects.get(number = food_number)
        except:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
    else:
        try:
            return await Food.objects.get(number = food_number, active = True)
        except:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
