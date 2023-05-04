<script setup>
    import navbar from '@/components/admin/navbar.vue'
</script>

<template>
    <navbar />

    <div class="view">
      <div class="container">
        <h2 class="mb-4">Дашборд</h2>
        <div class="row">
          <div class="col-md-3 col-6">
            <div class="alert alert-primary" role="alert">
              <h1 class="mt-0"><font-awesome-icon :icon="['fas', 'user']" /> {{this.counters.user}}</h1>
              <p class="m-0">Пользователей</p>
            </div>
          </div>
          <div class="col-md-3 col-6">
            <div class="alert alert-success" role="alert">
              <h1 class="mt-0"><font-awesome-icon :icon="['fas', 'cart-arrow-down']" /> {{this.counters.order}}</h1>
              <p class="m-0">Заказов</p>
            </div>
          </div>
          <div class="col-md-3 col-6">
            <div class="alert alert-info" role="alert">
              <h1 class="mt-0"><font-awesome-icon :icon="['fas', 'utensils']" /> {{this.counters.food}}</h1>
              <p class="m-0">Товаров</p>
            </div>
          </div>
          <div class="col-md-3 col-6">
            <div class="alert alert-warning" role="alert">
              <h1 class="mt-0"><font-awesome-icon :icon="['fas', 'layer-group']" /> {{this.counters.category}}</h1>
              <p class="m-0">Категорий</p>
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<script>
    import baseURL from "@/config"
    import { useCookies } from "vue3-cookies";
    import md5 from "js-md5"

    export default {
        data() {
            return { 
                counters: {
                  'user': 0,
                  'order': 0,
                  'food': 0,
                  'category': 0,
                }
            }
        },
        setup() {
          const { cookies } = useCookies();
          return { cookies };
        },
        created() {
          this.getUsers().then((data) => {
            this.counters.user = data.length
          })
          this.getOrder().then((data) => {
            this.counters.order = data.length
          })
          this.getFoods().then((data) => {
            this.counters.food = data.length
          })
          this.getCategories().then((data) => {
            this.counters.category = data.length
          })
        },
        mounted() {
        },
        methods: {
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
          async getOrder() {
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/order`, {
              method: "GET",
              mode: "cors",
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            return jsonData
          },
          async getUsers() {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/user`, {
              method: "GET",
              mode: "cors",
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            return jsonData
          },
        }
    }
</script>