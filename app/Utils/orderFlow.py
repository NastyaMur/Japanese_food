from fastapi import HTTPException
from datetime import datetime,timezone
from app.Utils.db import generalPosrgresBase, engine, session, User, Order, Food, Auth

order_states = [
    'new',
    'inprogress',
    'ontable',
    'closed',
    'canceled'
]

matrix_states = {
    'new' : ['inprogress', 'closed', 'canceled'],
    'inprogress' : ['new', 'ontable', 'closed', 'canceled'],
    'ontable' : ['inprogress', 'closed', 'canceled'],
    'closed' : ['canceled'],
    'canceled' : []
}

def check_order_status(status: str):
    if status in order_states:
        return True
    else:
        return False

def check_order_flow(oldStatus: str, newStatus: str):
    if oldStatus in order_states and newStatus in order_states:
        if newStatus in matrix_states[(oldStatus)]:
            return True
        else:
            return False
    else:
        return False

def get_all_flow(status: str):
    if status in order_states:
        return matrix_states[(status)]
    else:
        return []
