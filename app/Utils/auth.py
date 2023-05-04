import uuid
from fastapi import HTTPException
from datetime import datetime,timezone
from app.Utils.db import generalPosrgresBase, engine, session, User, Order, Food, Auth

async def check_token(accessToken: str):
    # Время жизни токена в часах
    token_live = 24
    current_token = accessToken.split(' ')[1]
    current_session = await Auth.objects.get_or_none(
        token = current_token,
        active = True
    )

    if current_session:
        if int(current_session.created) + ( int(token_live) * 60 * 60 * 1000 ) > int( datetime.now(timezone.utc).timestamp() * 1000 ):
            return True
        else:
            return False
    else:
        return False

def errAuth():
    raise HTTPException(status_code=401, detail={ "type" : "error", "data": "Not authentication"})

async def createAuth(
    user_email: str,
):
    token_value = str( uuid.uuid4().hex )
    created_value = str( int( datetime.now(timezone.utc).timestamp() * 1000 ) )

    current_sessions = await Auth.objects.all( 
        user = user_email,
        active = True
    )

    for session_object in current_sessions:
        await Auth.objects.update_or_create (
            token = session_object.token,
            active = False
        )

    result = await Auth.objects.create(
        user = user_email,
        created = created_value,
        token = token_value,
        active = True
    )

    raise HTTPException(status_code=200, detail={ "type" : "success", "data": {"created" : created_value, "token" : token_value}})