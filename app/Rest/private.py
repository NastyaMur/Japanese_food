from fastapi import FastAPI, APIRouter, Request, HTTPException
from sqlalchemy import inspect
from pydantic import BaseModel
from datetime import datetime,timezone
from app.Utils.db import generalPosrgresBase, engine, session, User, Order, Food, Auth, Role
from app.Utils.auth import *
import json

router = APIRouter()

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
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
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
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        await Food.objects.delete(number = food_number)
        raise HTTPException(status_code=200, detail={ "type" : "success"})
    else:
        return errAuth()


class createUserModel(BaseModel):
    name: str
    email: str
    password: str
    roles: list = []

class deleteUserModel(BaseModel):
    email: str

@router.put("/user")
async def addUsers(
    data_model: createUserModel,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):

        current_user = await User.objects.get_or_none(email = data_model.email)

        if current_user == None:
            result = await User.objects.create(
                name = data_model.name,
                email = data_model.email,
                password = data_model.password,
                created = str( int( datetime.now(timezone.utc).timestamp() * 1000 ) ),
                roles = json.dumps( data_model.roles )
            )
            raise HTTPException(status_code=201, detail={ "type" : "success", "email" : result.email})
        else:
            raise HTTPException(status_code=302, detail={ "type" : "error", "email" : current_user.email})
    else:
        return errAuth()

@router.delete("/user")
async def deleteUser(
    data_model: deleteUserModel,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        await User.objects.delete(email = data_model.email)
        raise HTTPException(status_code=200, detail={ "type" : "success"})
    else:
        return errAuth()

@router.get("/sessions")
async def getSessions(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        list = await Auth.objects.all()
        return list
    else:
        return errAuth()

@router.get("/user")
async def getMe(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        current_token = request.headers.get('Authorization').split(' ')[1]
        current_session = await Auth.objects.get_or_none(token = current_token)
        current_user = await User.objects.get_or_none(email = current_session.user)
        current_email = current_user.email

        user = await User.objects.get(email = current_email)
        return {
            "name" : user.name,
            "email" : user.email,
            "roles" : json.loads( user.roles ),
        }
    else:
        return errAuth()


class createOrderModel(BaseModel):
    description: str | None
    positions: list = []

class editOrderModel(BaseModel):
    status: str | None
    description: str | None
    positions: list | None

@router.get("/order")
async def getAllOrders(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        list = await Order.objects.all()
        return list
    else:
        return errAuth()

@router.put("/order")
async def addOrder(
    data_model: createOrderModel,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        current_token = request.headers.get('Authorization').split(' ')[1]
        current_session = await Auth.objects.get_or_none(token = current_token)
        current_user = await User.objects.get_or_none(email = current_session.user)
        current_email = current_user.email

        result = await Order.objects.create(
            author = current_email,
            sum = 0,
            description = data_model.description,
            positions = json.dumps( data_model.positions ),
            created = str( int( datetime.now(timezone.utc).timestamp() * 1000 ) )
        )
        raise HTTPException(status_code=201, detail={ "type" : "success", "number" : result.number})
    else:
        return errAuth()

@router.post("/order/{order_number}")
async def editOrder(
    order_number: int,
    data_model: editOrderModel,
    request: Request
):
    if "Authorization" in request.headers and check_token(request.headers.get('Authorization')):
        try:
            current_object = await Order.objects.get(number = order_number)

            await Order.objects.update_or_create(
                number = current_object.number,
                status = data_model.status if data_model.status != None else current_object.status,
                description = data_model.description if data_model.description != None else current_object.description,
                positions = data_model.positions if data_model.positions != None else current_object.positions
            )
        except:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
        raise HTTPException(status_code=302, detail={ "type" : "success"})
    else:
        return errAuth()

@router.delete("/order/{order_number}")
async def deleteOrder(
    order_number: int,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        await Order.objects.delete(number = order_number)
        raise HTTPException(status_code=200, detail={ "type" : "success"})
    else:
        return errAuth()

@router.get("/user/order")
async def getMeOrder(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):

        current_token = request.headers.get('Authorization').split(' ')[1]
        current_session = await Auth.objects.get_or_none(token = current_token)
        current_user = await User.objects.get_or_none(email = current_session.user)
        current_email = current_user.email

        order_list = await Order.objects.all(author = current_email)
        return order_list
    else:
        return errAuth()


class createRoleModel(BaseModel):
    name: str
    code: str

class editRoleModel(BaseModel):
    name: str | None

@router.get("/role")
async def getAllRole(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        list = await Role.objects.all()
        return list
    else:
        return errAuth()

@router.put("/role")
async def addRole(
    data_model: createRoleModel,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        current_role = await Role.objects.get_or_none(code = data_model.code)

        if current_role == None:
            result = await Role.objects.create(
                name = data_model.name,
                code = data_model.code
            )
            raise HTTPException(status_code=201, detail={ "type" : "success", "code" : result.code})
        else:
            raise HTTPException(status_code=302, detail={ "type" : "error", "code" : current_role.code})
    else:
        return errAuth()

@router.post("/role/{role_code}")
async def editRole(
    role_code: str,
    data_model: editRoleModel,
    request: Request
):
    if "Authorization" in request.headers and check_token(request.headers.get('Authorization')):
        try:
            current_object = await Role.objects.get(code = role_code)

            await Role.objects.update_or_create(
                code = current_object.code,
                name = data_model.name if data_model.name != None else current_object.name
            )
        except:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
        raise HTTPException(status_code=302, detail={ "type" : "success"})
    else:
        return errAuth()

@router.delete("/role/{role_code}")
async def deleteRole(
    role_code: str,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        await Role.objects.delete(code = role_code)
        raise HTTPException(status_code=200, detail={ "type" : "success"})
    else:
        return errAuth()
