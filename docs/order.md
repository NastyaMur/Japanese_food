# API | Заказ

## Оглавление
* [Получить список всех заказов](#getAll) <img src="https://img.shields.io/badge/-Auth-red">
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
        "created": "1680873260591",
        "author": "admin@mail.ru",
        "sum": 0,
        "number": 1,
        "description": "text",
        "status": null,
        "positions": "[]"
    },
    {
        "created": "1680876537129",
        "author": "admin2@mail.ru",
        "sum": 0,
        "number": 4,
        "description": null,
        "status": null,
        "positions": "[]"
    }
]
```

<a name="getMe"></a>
#### Получить список моих заказов
`GET` /api/user/order
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
[
    {
        "created": "1680876537129",
        "author": "admin2@mail.ru",
        "sum": 0,
        "number": 4,
        "description": null,
        "status": null,
        "positions": "[]"
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