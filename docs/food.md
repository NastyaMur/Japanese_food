# API | Позиция меню

## Оглавление
* [Получить весь перечень позиций в меню](#getAll) <img src="https://img.shields.io/badge/-All-green">
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
        "number": 37,
        "name": "Названние 1",
        "price": 200,
        "description": "Описание 1",
        "active": true
    },
    {
        "number": 38,
        "name": "Названние 2",
        "price": 200,
        "description": "Описание 2",
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
    "number": 37,
    "name": "Названние 1",
    "price": 200,
    "description": "Описание 1",
    "active": true
}
```

<a name="create"></a>
#### Создании новой позиции
`PUT` /api/food
##### Параметры
``` json
{
    "name" : "Названние",
    "price" : 100,
    "description" : "description",
    "active": true
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|name|Имя позиции меню|Строка|✅|
|price|Цена|Целое число|✅|
|description|Описание позиции меню|Текст|✅|
|active|Будет ли видна позиция всем (По-умолчанию стоит **true**)|Логический атрибут|❌|

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
                "description"
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
    "name" : "Названние",
    "price" : 100,
    "description" : "description",
    "active": true
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|name|Имя позиции меню|Строка|❌|
|price|Цена|Целое число|❌|
|description|Описание позиции меню|Текст|❌|
|active|Будет ли видна позиция всем (По-умолчанию стоит **true**)|Логический атрибут|❌|

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