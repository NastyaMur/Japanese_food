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

class createRoleModel(BaseModel):
    name: str
    code: str

class editRoleModel(BaseModel):
    name: str | None

@router.get("/")
async def getAllRole(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        list = await Role.objects.all()
        return list
    else:
        return errAuth()

@router.put("/")
async def addRole(
    data_model: createRoleModel,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        current_role = await Role.objects.get_or_none(code = data_model.code)

        if current_role == None:
            result = await Role.objects.create(
                name = data_model.name,
                code = data_model.code,
                lock = False
            )
            raise HTTPException(status_code=201, detail={ "type" : "success", "code" : result.code})
        else:
            raise HTTPException(status_code=302, detail={ "type" : "error", "code" : current_role.code})
    else:
        return errAuth()

@router.post("/{role_code}")
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

@router.delete("/{role_code}")
async def deleteRole(
    role_code: str,
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        await Role.objects.delete(code = role_code)
        raise HTTPException(status_code=200, detail={ "type" : "success"})
    else:
        return errAuth()