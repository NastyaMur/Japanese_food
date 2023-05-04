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

@router.get("/")
async def getSessions(
    request: Request
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        all_auth = await Auth.objects.all()
        return_auth = []
        for auth_object in all_auth:
            return_auth.append({
                "user": auth_object.user,
                "created": auth_object.created,
                "active": auth_object.active
            })
        return return_auth
    else:
        return errAuth()

@router.get("/user/{number_user}")
async def getUserSessions(
    request: Request,
    number_user: int
):
    if "Authorization" in request.headers and await check_token(request.headers.get('Authorization')):
        current_user = await User.objects.get_or_none(number = number_user)
        if current_user:
            all_auth = await Auth.objects.all(user = current_user.email)
            return_auth = []
            for auth_object in all_auth:
                return_auth.append({
                    "user": auth_object.user,
                    "created": auth_object.created,
                    "active": auth_object.active
                })
            return return_auth
        else:
            raise HTTPException(status_code=404, detail={ "type" : "error"})
    else:
        return errAuth()