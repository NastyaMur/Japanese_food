# API | Позиция меню

## Оглавление
* [Получить весь перечень позиций в меню](#getAll) <img src="https://img.shields.io/badge/-All-green">
* [Получить перечень популярных позиций в меню](#getPopular) <img src="https://img.shields.io/badge/-All-green">
* [Получить одну позицию в меню по номеру](#getOnce) <img src="https://img.shields.io/badge/-All-green">
* [Создании новой позиции](#create) <img src="https://img.shields.io/badge/-Auth-red">
* [Редактирование позиции](#edit) <img src="https://img.shields.io/badge/-Auth-red">
* [Удалить позицию в меню](#delete) <img src="https://img.shields.io/badge/-Auth-red">

<a name="getAll"></a>
#### Получить весь перечень позиций в меню
`GET` /api/food
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
[
    {
        "number": 1,
        "name": "Чай",
        "photo": null,
        "weight": 100,
        "category": {
            "name": "Напитки",
            "code": "water"
        },
        "price": 55,
        "description": "Черный/Зеленый",
        "active": true
    },
    {
        "number": 2,
        "name": "Кофе",
        "weight": 100,
        "photo": null,
        "category": {
            "name": "Напитки",
            "code": "water"
        },
        "price": 80,
        "description": "Крепкий",
        "active": true
    },
    {
        "number": 7,
        "name": "Домашний",
        "photo": null,
        "weight": 900,
        "category": {
            "name": "Сеты",
            "code": "sets"
        },
        "price": 1200,
        "description": "Очень вкусный",
        "active": true
    }
]
```

<a name="getPopular"></a>
#### Получить весь перечень позиций в меню
`GET` /api/food/popular
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
[
    {
        "number": 7,
        "name": "Домашний",
        "photo": null,
        "weight": 900,
        "category": {
            "name": "Сеты",
            "code": "sets"
        },
        "price": 1200,
        "description": "Очень вкусный",
        "active": true
    }
]
```

<a name="getOnce"></a>
#### Получить одну позицию в меню по номеру
`GET` /api/food/37
##### Параметры
37 - номер позиции меню

##### Ответ
Код ответа `200`
``` json
{
    "number": 1,
    "name": "Чай",
    "photo": null,
    "weight": 100,
    "category": "water",
    "price": 55,
    "weight": null,
    "description": "Черный/Зеленый",
    "active": true,
    "popular": true
}
```

<a name="create"></a>
#### Создании новой позиции
`PUT` /api/food
##### Параметры
``` json
{
    "name" : "Лимонад",
    "price" : 100,
    "weight": 200,
    "description" : "В ассортименте",
    "photo" : BASE64,
    "category" : "water",
    "active" : true,
    "popular": true
}
```

|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|name|Имя позиции меню|Строка|✅|
|price|Цена|Целое число|✅|
|weight|Масса блюда в граммах|Целое число|✅|
|description|Описание позиции меню|Текст|❌|
|photo|Картинка в формате base64|Текст|❌|
|category|Код категории|Текст|✅|
|active|Будет ли видна позиция всем (По-умолчанию стоит **true**)|Логический атрибут|❌|
|popular|Будет ли позиция показываться в топе (По-умолчанию стоит **true**)|Логический атрибут|❌|

##### Ответ в случае успеха
Код ответа `201`
``` json
{
    "detail": {
        "type": "success",
        "number": 26
    }
}
```

##### Ответ в случае ошибки
Код ответа `422`
> В теле ответа будет описание ошибки как в примере
``` json
{
    "detail": [
        {
            "loc": [
                "body",
                "category"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```

<a name="edit"></a>
#### Редактирование позиции
`POST` /api/food/37
##### Параметры
37 - номер позиции меню
``` json
{
    "price" : 100
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|name|Имя позиции меню|Строка|❌|
|price|Цена|Целое число|❌|
|weight|Масса блюда в граммах|Целое число|❌|
|description|Описание позиции меню|Текст|❌|
|photo|Картинка в формате base64|Текст|❌|
|category|Код категории|Текст|❌|
|active|Будет ли видна позиция всем (По-умолчанию стоит **true**)|Логический атрибут|❌|
|popular|Будет ли позиция показываться в топе (По-умолчанию стоит **true**)|Логический атрибут|❌|

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
Код ответа `422`
> В теле ответа будет описание ошибки как в примере
``` json
{
    "detail": [
        {
            "loc": [
                "body",
                "price"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```

<a name="delete"></a>
#### Удалить позицию в меню
`DELETE` /api/food/37
##### Параметры
37 - номер позиции меню

##### Ответ
Код ответа `200`
``` json
{
    "detail": {
        "type": "success"
    }
}
```