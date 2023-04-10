# 🍱 Japanese_Food

## Оглавление

В данном репозитории используются badge для классификации уровня доступа запросов 

<img src="https://img.shields.io/badge/-Auth-red"> - Запросы помеченные такой иконкой доступны лишь после авторизации

<img src="https://img.shields.io/badge/-All-green"> - Запросы с такой иконкой доступны для всех

* API
    * [Позиция меню](/docs/food.md) <img src="https://img.shields.io/badge/-Auth-red"> <img src="https://img.shields.io/badge/-All-green">
    * [Роли](/docs/role.md) <img src="https://img.shields.io/badge/-Auth-red"> <img src="https://img.shields.io/badge/-All-green">
    * [Заказ](/docs/order.md) <img src="https://img.shields.io/badge/-Auth-red"> <img src="https://img.shields.io/badge/-All-green">
    * [Пользователь](/docs/user.md) <img src="https://img.shields.io/badge/-Auth-red"> <img src="https://img.shields.io/badge/-All-green">
* [Запуск приложения](#starting)


<a name="starting"></a>

## Запуск приложения
Для запуска проекта нам необходимо скачать исходники проекта и запустить сборку контейнера
> Для данных дейсвтий необходимо иметь установленный git, а так же иметь доступ к текущему репозиторию

``` bash
# Клонируем репозиторий
git clone ...

# Заходим в созданную папку
cd Japanese_Food

# Запускаем сборку докер контейнера
docker-compose up -d --build
```