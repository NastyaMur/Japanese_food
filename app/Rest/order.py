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

class createOrderModel(BaseModel):
    description: str | None
    positions: list = []

class editOrderModel(BaseModel):
    status: str | None
    description: str | None
    positions: list | None

@router.get("/")
async def getAllOrders(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        returnData = []
        for item in await Order.objects.all():

            return_positions = []
            return_sum = 0
            current_positions = json.loads(item.positions)
            for food_number in current_positions:
                getting_food = await Food.objects.get(number = food_number)
                return_positions.append({
                    "number": getting_food.number,
                    "name": getting_food.name,
                    "category": getting_food.category,
                    "price": getting_food.price,
                    "description": getting_food.description,
                    "active": getting_food.active
                })
                return_sum += getting_food.price

            current_author = await User.objects.get_or_none(email = item.author)
            if current_author:
                all_order_in_user = await Order.objects.all(author = item.author)
                all_order_current = []
                for order_in_user in all_order_in_user:
                    all_order_current.append( order_in_user.number )   

                all_roles = json.loads(current_author.roles)
                current_roles = []
                for role_code in all_roles:
                    current_role = await Role.objects.get(code = role_code)
                    current_roles.append({
                        'name': current_role.name,
                        'code': current_role.code
                    })

                current_author_data = {
                    "name": current_author.name,
                    "number": current_author.number,
                    "email": current_author.email,
                    "roles": current_roles,
                    "orders": all_order_current
                }
            else:
                current_author_data = {}

            returnData.append({
                "number" : item.number,
                "created" : item.created,
                "author" : current_author_data,
                "status" : item.status,
                "allow_status" : get_all_flow(item.status),
                "sum" : return_sum,
                "description" : item.description,
                "positions": return_positions
            })
        return returnData
    else:
        return errAuth()

@router.put("/")
async def addOrder(
    data_model: createOrderModel,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        current_token = request.headers.get('Authorization').split(' ')[1]
        current_session = await Auth.objects.get_or_none(token = current_token)
        current_user = await User.objects.get_or_none(email = current_session.user)
        current_email = current_user.email

        current_sum = 0
        for foodNumber in data_model.positions:
            foodObject = await Food.objects.get_or_none(number = int(foodNumber))
            if foodObject:
                current_sum += int(foodObject.price)

        print(current_sum)

        result = await Order.objects.create(
            author = current_email,
            sum = current_sum,
            description = data_model.description,
            status = 'new',
            positions = json.dumps( data_model.positions ),
            created = str( int( datetime.now(timezone.utc).timestamp() * 1000 ) )
        )
        raise HTTPException(status_code=201, detail={ "type" : "success", "number" : result.number})
    else:
        return errAuth()

@router.post("/{order_number}")
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

@router.delete("/{order_number}")
async def deleteOrder(
    order_number: int,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        await Order.objects.delete(number = order_number)
        raise HTTPException(status_code=200, detail={ "type" : "success"})
    else:
        return errAuth()

@router.get("/me")
async def getMeOrder(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):

        current_token = request.headers.get('Authorization').split(' ')[1]
        current_session = await Auth.objects.get_or_none(token = current_token)
        current_user = await User.objects.get_or_none(email = current_session.user)
        current_email = current_user.email

        order_list = await Order.objects.all(author = current_email)

        returnData = []
        for item in order_list:
            return_positions = []
            return_sum = 0
            current_positions = json.loads(item.positions)
            for food_number in current_positions:
                getting_food = await Food.objects.get(number = food_number)
                return_positions.append( getting_food )

            returnData.append({
                "number" : item.number,
                "created" : item.created,
                "author" : item.author,
                "status" : item.status,
                "allow_status" : get_all_flow(item.status),
                "sum" : item.sum,
                "description" : item.description,
                "positions": return_positions
            })
        return returnData
    else:
        return errAuth()

@router.get("/{order_number}")
async def getOneOrder(
    order_number: int,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        try:
            order = await Order.objects.get(number = order_number)
            return_positions = []
            current_positions = json.loads(order.positions)
            for food_number in current_positions:
                getting_food = await Food.objects.get(number = food_number)
                return_positions.append( getting_food )

            current_author = await User.objects.get_or_none(email = order.author)
            if current_author:
                all_order_in_user = await Order.objects.all(author = order.author)
                all_order_current = []
                for order_in_user in all_order_in_user:
                    all_order_current.append( order_in_user.number )   

                current_author_data = {
                    "name": current_author.name,
                    "number": current_author.number,
                    "email": current_author.email,
                    "roles": json.loads(current_author.roles),
                    "orders": all_order_current
                }
            else:
                current_author_data = {}
            
            return {
                "number" : order.number,
                "created" : order.created,
                "status" : order.status,
                "allow_status" : get_all_flow(order.status),
                "author" : current_author_data,
                "sum" : order.sum,
                "description" : order.description,
                "positions": return_positions
            }

        except:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
    else:
        return errAuth()
