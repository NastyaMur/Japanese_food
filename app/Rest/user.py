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

class createUserModel(BaseModel):
    name: str
    email: str
    password: str

class editUserModel(BaseModel):
    name: str | None
    photo: str | None
    email: str | None
    password: str | None
    roles: list | None

class deleteUserModel(BaseModel):
    email: str

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

@router.put("/")
async def addUsers(
    data_model: createUserModel,
    request: Request
):
    current_user = await User.objects.get_or_none(email = data_model.email)

    if current_user == None:
        result = await User.objects.create(
            name = data_model.name,
            email = data_model.email,
            password = data_model.password,
            created = str( int( datetime.now(timezone.utc).timestamp() * 1000 ) ),
            roles = json.dumps( ['user'] )
        )
        raise HTTPException(status_code=201, detail={ "type" : "success", "email" : result.email})
    else:
        raise HTTPException(status_code=302, detail={ "type" : "error", "email" : current_user.email})

@router.post("/{user_number}")
async def editUser(
    user_number: int,
    data_model: editUserModel,
    request: Request
):
    if "Authorization" in request.headers and check_token(request.headers.get('Authorization')):
        try:
            current_object = await User.objects.get(number = user_number)
            await User.objects.update_or_create(
                number = current_object.number,
                email = data_model.email if data_model.email != None else current_object.email,
                name = data_model.name if data_model.name != None else current_object.name,
                photo = data_model.photo if data_model.photo != None else current_object.photo,
                password = data_model.password if data_model.password != None else current_object.password,
                roles = json.dumps(data_model.roles) if data_model.roles != None else current_object.roles
            )
        except:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
            raise HTTPException(status_code=302, detail={ "type" : "success"})
    else:
        return errAuth()

@router.get("/")
async def getAllUsers(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        returnData = []
        list = await User.objects.all()
        for user_item in list:
            returnData.append({
                "number" : user_item.number,
                # "password" : user_item.password,
                "name" : user_item.name,
                "photo" : user_item.photo,
                "email" : user_item.email,
                "roles" : json.loads(user_item.roles)
            })
        return returnData
    else:
        return errAuth()

@router.delete("/")
async def deleteUser(
    data_model: deleteUserModel,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        await Auth.objects.delete(user = data_model.email)
        await User.objects.delete(email = data_model.email)
        raise HTTPException(status_code=200, detail={ "type" : "success"})
    else:
        return errAuth()

@router.get("/me")
async def getMe(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        current_token = request.headers.get('Authorization').split(' ')[1]
        current_session = await Auth.objects.get_or_none(token = current_token)
        current_user = await User.objects.get_or_none(email = current_session.user)
        current_email = current_user.email
        orders = await Order.objects.all(author = current_email)
        order_numbers = []

        for order_object in orders:
            positionsCurrent = []
            for foodNumber in json.loads(order_object.positions):
                foodObject = await Food.objects.get(number = foodNumber)
                positionsCurrent.append({
                    "number": foodObject.number,
                    "name": foodObject.name,
                    "category": foodObject.category,
                    "price": foodObject.price,
                    "description": foodObject.description
                })
            order_numbers.append({
                "created": order_object.created,
                "author": order_object.author,
                "sum": order_object.sum,
                "number": order_object.number,
                "description": order_object.description,
                "status": order_object.status,
                "positions": positionsCurrent
            })

        user = await User.objects.get(email = current_email)
        return {
            "number" : user.number,
            "name" : user.name,
            "photo" : user.photo,
            "email" : user.email,
            "orders" : order_numbers,
            "roles" : json.loads( user.roles ),
        }
    else:
        return errAuth()

@router.get("/{user_number}")
async def getUserData(
    user_number: int,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        

        current_token = request.headers.get('Authorization').split(' ')[1]
        session = await Auth.objects.get(token = current_token)
        current_user = await User.objects.get(email = session.user)
        user = await User.objects.get_or_none(number = user_number)

        if user:
            orders = await Order.objects.all(author = user.email)
            orderList = []

            if current_user.email == user.email:
                meBool = True
            else:
                meBool = False

            for orderItem in orders:

                positionsCurrent = []
                for foodNumber in json.loads(orderItem.positions):
                    foodObject = await Food.objects.get(number = foodNumber)
                    positionsCurrent.append({
                        "number": foodObject.number,
                        "name": foodObject.name,
                        "category": foodObject.category,
                        "price": foodObject.price,
                        "description": foodObject.description
                    })
                orderList.append({
                    'number' : orderItem.number,
                    'created' : orderItem.created,
                    'status' : orderItem.status,
                    'sum' : orderItem.sum,
                    'description' : orderItem.description,
                    'positions' : positionsCurrent
                })
            return {
                "me" : meBool,
                "number" : user.number,
                "created" : user.created,
                "name" : user.name,
                "photo" : user.photo,
                "email" : user.email,
                "roles" : json.loads( user.roles ),
                "orders" : orderList
            }
        else:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
    else:
        return errAuth()
