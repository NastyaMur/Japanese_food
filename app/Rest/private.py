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
