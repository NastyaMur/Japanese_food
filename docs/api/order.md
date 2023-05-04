# API | Заказ

## Оглавление
* [Получить список всех заказов](#getAll) <img src="https://img.shields.io/badge/-Auth-red">
* [Получить информацию по заказу](#getOnce) <img src="https://img.shields.io/badge/-Auth-red">
* [Получить список моих заказов](#getMe) <img src="https://img.shields.io/badge/-Auth-red">
* [Создание нового заказа](#create) <img src="https://img.shields.io/badge/-Auth-red">
* [Редактирование заказа](#edit) <img src="https://img.shields.io/badge/-Auth-red">
* [Удаление заказа](#delete) <img src="https://img.shields.io/badge/-Auth-red">

<a name="getAll"></a>
#### Получить список всех заказов
`GET` /api/order
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
[
    {
        "number": 1,
        "created": "1681476061340",
        "author": {
            "name": "Анастасия",
            "number": 1,
            "email": "admin@mail.ru",
            "roles": [
                {
                    "name": "Администратор",
                    "code": "admin"
                }
            ],
            "orders": [
                1
            ]
        },
        "status": "closed",
        "allow_status": [
            "canceled"
        ],
        "sum": 135,
        "description": null,
        "positions": [
            {
                "number": 1,
                "name": "Чай",
                "category": "water",
                "price": 55,
                "description": "Черный/Зеленый",
                "active": true
            },
            {
                "number": 2,
                "name": "Кофе",
                "category": "water",
                "price": 80,
                "description": "Крепкий",
                "active": true
            }
        ]
    }
]
```

<a name="getOnce"></a>
#### Получить информацию по заказу
`GET` /api/order/1
##### Параметры
1 - Номер заказа

##### Ответ
Код ответа `200`
``` json
{
    "number": 1,
    "created": "1681476061340",
    "status": "closed",
    "allow_status": [
        "canceled"
    ],
    "author": {
        "name": "Анастасия",
        "number": 1,
        "email": "admin@mail.ru",
        "roles": [
            "admin"
        ],
        "orders": [
            1
        ]
    },
    "sum": 130,
    "description": null,
    "positions": [
        {
            "number": 1,
            "name": "Чай",
            "photo": null,
            "category": "water",
            "price": 55,
            "weight": null,
            "description": "Черный/Зеленый",
            "active": true,
            "popular": true
        },
        {
            "number": 2,
            "name": "Кофе",
            "photo": null,
            "category": "water",
            "price": 80,
            "weight": null,
            "description": "Крепкий",
            "active": true,
            "popular": true
        }
    ]
}
```

<a name="getMe"></a>
#### Получить список моих заказов
`GET` /api/order/me
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
[
    {
        "number": 1,
        "created": "1681476061340",
        "author": "admin@mail.ru",
        "status": "closed",
        "allow_status": [
            "canceled"
        ],
        "sum": 130,
        "description": null,
        "positions": [
            {
                "number": 1,
                "name": "Чай",
                "photo": null,
                "category": "water",
                "price": 55,
                "weight": null,
                "description": "Черный/Зеленый",
                "active": true,
                "popular": true
            },
            {
                "number": 2,
                "name": "Кофе",
                "photo": null,
                "category": "water",
                "price": 80,
                "weight": null,
                "description": "Крепкий",
                "active": true,
                "popular": true
            }
        ]
    }
]
```

<a name="create"></a>
#### Создание нового заказа
`PUT` /api/order
##### Параметры
``` json
{
    "description": null,
    "positions": []
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|description|Описание позиции меню|Текст|❌|
|positions|Номера позиций меню в заказе|Массив|✅|

##### Ответ в случае успеха
Код ответа `201`
``` json
{
    "detail": {
        "type": "success",
        "number": 4
    }
}
```

<a name="edit"></a>
#### Редактирование заказа
`POST` /api/order/4
##### Параметры
4 - номер позиции меню
``` json
{
    "status" : "closed",
    "description" : "С собой",
    "positions": []
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|status|Код нового статуса|Текст|❌|
|description|Описание позиции меню|Текст|❌|
|positions|Номера позиций меню в заказе|Массив|❌|

##### Ответ в случае успеха
Код ответа `302`
``` json
{
    "detail": {
        "type": "success"
    }
}
```

##### Ответ в случае ошибки
Код ответа `404`
``` json
{
    "detail": {
        "type": "error"
    }
}
```

<a name="delete"></a>
#### Удалить заказ
`DELETE` /api/order/5
##### Параметры
5 - номер позиции меню

##### Ответ
Код ответа `200`
``` json
{
    "detail": {
        "type": "success"
    }
}
```