# API | Категории меню

## Оглавление
* [Получить весь перечень категорий](#getAll) <img src="https://img.shields.io/badge/-All-success">
* [Получить все позиции меню по категории](#getAllPositions) <img src="https://img.shields.io/badge/-All-success">
* [Получить категорию](#getOnce) <img src="https://img.shields.io/badge/-All-success">
* [Создании новой категории](#create) <img src="https://img.shields.io/badge/-Auth-red">
* [Редактирование категории](#edit) <img src="https://img.shields.io/badge/-Auth-red">
* [Удалить категорию](#delete) <img src="https://img.shields.io/badge/-Auth-red">

<a name="getAll"></a>
#### Получить весь перечень категорий
`GET` /api/category
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
[
    {
        "name": "Сеты",
        "code": "sets"
    },
    {
        "name": "Напитки",
        "code": "water"
    }
]
```

<a name="getAllPositions"></a>
#### Получить все позиции меню по категории
`GET` /api/category/water/positions
##### Параметры
water - Код категории

> **Внимание!** При запросе от авторизованного пользователя с правами администратора вы получите полный список по категории. В случае не авторизованного пользователя или пользователя с правами ниже, вы получите только активные позиции меню 

##### Ответ
Код ответа `200`
``` json
[
    {
        "number": 1,
        "name": "Чай",
        "photo": null,
        "category": "water",
        "price": 55,
        "weight": 150,
        "description": "Черный/Зеленый",
        "active": true,
        "popular": false
    },
    {
        "number": 2,
        "name": "Кофе",
        "photo": null,
        "category": "water",
        "price": 80,
        "weight": 150,
        "description": "Крепкий",
        "active": true,
        "popular": false
    }
]
```

<a name="#getOnce"></a>
#### Получить категорию
`GET` /api/category/water
##### Параметры
water - Код категории

##### Ответ в случае успеха
Код ответа `200`
``` json
{
    "name": "Напитки",
    "code": "water"
}
```

##### Ответ в случае ошибки
Код ответа `404`
> Категория с таким кодом не найдена
``` json
{
    "detail": {
        "type": "error"
    }
}
```

<a name="create"></a>
#### Создании новой категории
`PUT` /api/category
##### Параметры
``` json
{
    "name" : "Напитки",
    "code" : "water"
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|name|Строковое название категории|Строка|✅|
|code|Кодовое значение|Строка|✅|

##### Ответ в случае успеха
Код ответа `201`
``` json
{
    "detail": {
        "type": "success",
        "code": "water"
    }
}
```

##### Ответ в случае ошибки
Код ответа `302`
> Категория с таким кодом уже существует
``` json
{
    "detail": {
        "type": "error",
        "code": "water"
    }
}
```

<a name="edit"></a>
#### Редактирование категории
`POST` /api/category/water
##### Параметры
water - Код категории
``` json
{
    "name" : "Напитки"
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|name|Строковое название категории|Строка|✅|

##### Ответ в случае успеха
Код ответа `302`
``` json
{
    "detail": {
        "type": "success"
    }
}
```

<a name="delete"></a>
#### Удалить категорию
`DELETE` /api/category/water
##### Параметры
water - Код категории

##### Ответ
Код ответа `200`
``` json
{
    "detail": {
        "type": "success"
    }
}
```