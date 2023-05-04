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

class createCategoryModel(BaseModel):
    name: str
    code: str

class editCategoryModel(BaseModel):
    name: str | None

@router.get("/{category_code}/positions")
async def getOneCategoryPositions(
    category_code: str,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        return await Food.objects.all(category = category_code)
    else:
        return await Food.objects.all(category = category_code, active = True)

@router.put("/")
async def addCategory(
    data_model: createCategoryModel,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        current_category = await Category.objects.get_or_none(code = data_model.code)

        if current_category == None:
            result = await Category.objects.create(
                name = data_model.name,
                code = data_model.code
            )
            raise HTTPException(status_code=201, detail={ "type" : "success", "code" : result.code})
        else:
            raise HTTPException(status_code=302, detail={ "type" : "error", "code" : current_category.code})
    else:
        return errAuth()

@router.post("/{category_code}")
async def editCategory(
    category_code: str,
    data_model: editCategoryModel,
    request: Request
):
    if "Authorization" in request.headers and check_token(request.headers.get('Authorization')):
        try:
            current_object = await Category.objects.get(code = category_code)

            await Category.objects.update_or_create(
                code = current_object.code,
                name = data_model.name if data_model.name != None else current_object.name
            )
        except:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
        raise HTTPException(status_code=302, detail={ "type" : "success"})
    else:
        return errAuth()

@router.delete("/{category_code}")
async def deleteCategory(
    category_code: str,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        await Category.objects.delete(code = category_code)
        raise HTTPException(status_code=200, detail={ "type" : "success"})
    else:
        return errAuth()

@router.get("/")
async def getAllCategory(
    request: Request
):
    list = await Category.objects.all()
    return list

@router.get("/{category_code}")
async def getOneCategory(
    category_code: str,
    request: Request
):
    
    category = await Category.objects.get_or_none(code = category_code)

    if category:
        return category
    else:
        raise HTTPException(status_code=404, detail={ "type" : "error"})