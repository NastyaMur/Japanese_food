import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

from app.Rest import food, category, user, order, role, session
from app.Utils.db import generalPosrgresBase, User, Role

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    if not generalPosrgresBase.is_connected:
        await generalPosrgresBase.connect()

        try:
            # Дефолтные обьект
            await Role.objects.create( name = 'Администратор', code = 'admin', lock = True)
            await Role.objects.create( name = 'Пользователь', code = 'user', lock = True)
            # Password 123
            await User.objects.create( name = 'Анастасия', email = 'admin@mail.ru', password = '202cb962ac59075b964b07152d234b70', roles = '["admin"]' ) 
        except:
            print('Don`t first started')


@app.on_event("shutdown")
async def shutdown():
    if generalPosrgresBase.is_connected:
        await generalPosrgresBase.disconnect()

app.include_router(food.router, prefix="/api/food")
app.include_router(category.router, prefix="/api/category")
app.include_router(role.router, prefix="/api/role")
app.include_router(user.router, prefix="/api/user")
app.include_router(order.router, prefix="/api/order")
app.include_router(session.router, prefix="/api/session")
