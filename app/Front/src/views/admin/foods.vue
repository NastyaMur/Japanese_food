<script setup>
    import navbar from '@/components/admin/navbar.vue'
</script>

<template>
    <navbar />

    <div class="modal fade" id="createFood" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Создание новой позиции меню</h1>
            <button type="button" id="createFoodClosed" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-2">
                <label for="name" class="form-label">Название товара <span class="text-danger">*</span></label>
                <input id="name" type="text" class="form-control">
              </div>
              <div class="mb-2">
                <label for="description" class="form-label">Описание</label>
                <input id="description" type="text" class="form-control">
                <div class="form-text">Используйте состав продукта для большей пользы</div>
              </div>
              <div class="mb-2">
                <label for="price" class="form-label">Цена <span class="text-danger">*</span></label>
                <input id="price" type="number" class="form-control">
              </div>
              <div class="mb-2">
                <label for="weight" class="form-label">Масса блюда (г.) <span class="text-danger">*</span></label>
                <input id="weight" type="number" class="form-control">
              </div>
              <div class="mb-2">
                <label for="category" class="form-label">Категория <span class="text-danger">*</span></label>
                <select id="category" class="form-select">
                  <option v-for="category in categories">
                    {{category.name}}
                  </option>
                </select>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Отменить</button>
            <button type="button" class="btn btn-primary" v-on:click="create()">Создать</button>
          </div>
        </div>
      </div>
    </div>

    <div class="view">
      <div class="container">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="/admin">Панель администратора</a></li>
            <li class="breadcrumb-item active" aria-current="page">Товары</li>
          </ol>
        </nav>
        <h2>Товары</h2>
        <div class="btn-toolbar mb-4" role="toolbar">
          <div class="btn-group btn-group-sm me-2" role="group">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createFood">
              <font-awesome-icon :icon="['fas', 'plus']" class="me-2"/>
              Добавить
            </button>
          </div>
        </div>
        <div class="row">
          <div class="col-12">
            <div class="card-text">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">Наименование</th>
                    <th scope="col">Категория</th>
                    <th class="text-center" scope="col">Цена</th>
                    <th scope="col">Описание</th>
                    <th class="text-center" scope="col">Активен</th>
                    <th class="text-center" scope="col">Удалить</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="food in items">
                    <th scope="row" v-on:click="openFood(food.number)">{{food.number}}</th>
                    <td v-on:click="openFood(food.number)">{{food.name}}</td>
                    <td v-on:click="openFood(food.number)">{{food.category.name}}</td>
                    <td class="text-center" v-on:click="openFood(food.number)">{{food.price}} ₽</td>
                    <td v-on:click="openFood(food.number)">{{food.description}}</td>
                    <td class="text-center" v-on:click="openFood(food.number)"><span v-if="food.active">✅</span><span v-if="!food.active">❌</span></td>
                    <td class="text-center text-danger" v-on:click="deleteFood(food.number)"><font-awesome-icon :icon="['fas', 'trash']" :class="'delete-food-' + food.number"/></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<style scoped>
  .view {
    margin-top: 20px;
  }
</style>

<script>

  import baseURL from "@/config"
  import { useCookies } from "vue3-cookies";

  export default {
        data() {
            return { 
                items: [],
                categories: []
            }
        },
        mounted() {
          this.init()
        },
        methods: {
          async init() {
            this.getCategories().then((data) => {
                this.categories = data
                console.log(data)
            })
            this.getFoods().then((data) => {
                this.items = data
                console.log(data)
            })
          },
          async getCategories() {
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/category`, {
              method: "GET",
              mode: "cors",
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            return jsonData
          },
          async getFoods() {
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/food`, {
              method: "GET",
              mode: "cors",
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            return jsonData
          },
          async create() {
            let categoryCode = ''
            let categoryName = document.getElementById('category').value
            for (let index in this.categories) {
                let categoryObject = this.categories[index]
                if (categoryObject.name == categoryName) {
                  categoryCode = categoryObject.code
                }
            }
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/food`, {
              method: "PUT",
              mode: "cors",
              body: JSON.stringify({
                "name" : document.getElementById('name').value,
                "price" : parseInt(document.getElementById('price').value),
                "description" : document.getElementById('description').value,
                "weight" : document.getElementById('weight').value,
                "category" : categoryCode,
              }),
              headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            this.init()
            document.getElementById('createFoodClosed').click()
            document.getElementById('name').value = ''
            document.getElementById('description').value = ''
            document.getElementById('price').value = ''
            document.getElementById('weight').value = ''
          },
          openFood(number) {
            window.location.href = `/admin/food/${number}`
          },
          async deleteFood(number) {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/food/${number}`, {
              method: "DELETE",
              mode: "cors",
              headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            this.init()
          }
        }
    }
</script>