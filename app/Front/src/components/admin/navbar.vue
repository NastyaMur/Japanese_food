<script setup>
    import userBloc from './user.vue'
</script>

<template>
    <nav class="navbar">
        <div class="container">
            <button id="settigns-button" class="btn btn-outline-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
                <font-awesome-icon icon="fa-solid fa-cog" />
                Настройки
            </button>
            <userBloc />
        </div>
    </nav>

    <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasRightLabel">Настройки</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <a href="/" class="alert alert-light p-0 text-decoration-none d-block mb-4" role="alert">
                <font-awesome-icon :icon="['fas', 'house']" class="me-3"/>Вернуться на главную страницу сайта
            </a>
            <a href="/admin/foods" class="alert alert-light p-0 text-decoration-none d-block" role="alert">
                <font-awesome-icon :icon="['fas', 'utensils']" class="me-3"/>Товары
            </a>
            <a href="/admin/categories" class="alert alert-light p-0 text-decoration-none d-block" role="alert">
                <font-awesome-icon :icon="['fas', 'layer-group']" class="me-3"/>Категории
            </a>
            <a href="/admin/users" class="alert alert-light p-0 text-decoration-none d-block" role="alert">
                <font-awesome-icon :icon="['fas', 'user']" class="me-3"/>Пользователи
            </a>
            <a href="/admin/orders" class="alert alert-light p-0 text-decoration-none d-block" role="alert">
                <font-awesome-icon :icon="['fas', 'cart-arrow-down']" class="me-3"/>Заказы
            </a>
            <a href="/admin/roles" class="alert alert-light p-0 text-decoration-none d-block" role="alert">
                <font-awesome-icon :icon="['fas', 'hand-sparkles']" class="me-3"/>Роли
            </a>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'navbar'
  }
</script>

<style scoped>
    .navbar {
        /* margin-top: 50px; */
    }
    #settigns-button {
        border-radius: 50px;
    }
</style>