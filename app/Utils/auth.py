import uuid
from fastapi import HTTPException
from datetime import datetime,timezone
from app.Utils.db import generalPosrgresBase, engine, session, User, Order, Food, Auth

async def check_token(accessToken: str):
    current_token = accessToken.split(' ')[1]
    current_session = await Auth.objects.get_or_none(token = current_token)

    if current_session:
        return True
    else:
        return False

# def create_token(accessToken: str):
#     if accessToken == 'Bearer AIzaSyDl9t5fkFmSeSzSw8baa0preiSntsTH6Ik=':
#         return True
#     else:
#         return False

def errAuth():
    raise HTTPException(status_code=401, detail={ "type" : "error", "data": "Not authentication"})

async def createAuth(
    user_email: str,
):
    token_value = str( uuid.uuid4().hex )
    created_value = str( int( datetime.now(timezone.utc).timestamp() * 1000 ) )

    result = await Auth.objects.create(
        user = user_email,
        created = created_value,
        token = token_value
    )

    raise HTTPException(status_code=200, detail={ "type" : "success", "data": {"created" : created_value, "token" : token_value}})