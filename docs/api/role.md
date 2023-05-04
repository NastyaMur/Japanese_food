# API | Роли

## Оглавление
* [Получить весь перечень ролей](#getAll) <img src="https://img.shields.io/badge/-Auth-red">
* [Создании новой роли](#create) <img src="https://img.shields.io/badge/-Auth-red">
* [Редактирование роли](#edit) <img src="https://img.shields.io/badge/-Auth-red">
* [Удалить роли](#delete) <img src="https://img.shields.io/badge/-Auth-red">

<a name="getAll"></a>
#### Получить весь перечень ролей
`GET` /api/role
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
[
    {
        "name": "Админ",
        "code": "admin"
    }
]
```

<a name="create"></a>
#### Создании новой роли
`PUT` /api/role
##### Параметры
``` json
{
    "name" : "Админ",
    "code" : "admin"
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|name|Строковое название роли|Строка|✅|
|code|Кодовое значение|Строка|✅|

##### Ответ в случае успеха
Код ответа `201`
``` json
{
    "detail": {
        "type": "success",
        "code": "admin"
    }
}
```

##### Ответ в случае ошибки
Код ответа `302`
> Роль с таким кодом уже существует
``` json
{
    "detail": {
        "type": "error",
        "code": "admin"
    }
}
```

<a name="edit"></a>
#### Редактирование роли
`POST` /api/role/admin
##### Параметры
admin - Код роли
``` json
{
    "name" : "Админ запасной"
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|name|Строковое название роли|Строка|✅|

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
#### Удалить роль
`DELETE` /api/role/admin
##### Параметры
admin - Код роли

##### Ответ
Код ответа `200`
``` json
{
    "detail": {
        "type": "success"
    }
}
```