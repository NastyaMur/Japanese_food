import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.Rest import public, private
from app.Utils.db import generalPosrgresBase

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

@app.on_event("shutdown")
async def shutdown():
    if generalPosrgresBase.is_connected:
        await generalPosrgresBase.disconnect()

app.include_router(public.router, prefix="/api")
app.include_router(private.router, prefix="/api")
