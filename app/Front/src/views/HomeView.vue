<script setup>
    import navbar from '@/components/client/navbar.vue'
    import menuTopItem from '@/components/client/menuTopItem.vue'
    import menuTopItemSale from '@/components/client/menuTopItemSale.vue'
    import downBar from '@/components/client/footer.vue'
</script>

<template>
    <navbar />

    <div class="view">
      <div class="container p-4">
        <h3 class="fw-bolder">🔥 Горячо!</h3>
        <p>Выгодная цена на любимые роллы, успей купить, пока акция еще не закончилась!</p>
        <div class="row">
            <menuTopItemSale/>
            <menuTopItem v-for="food in populars"
                :number = food.number
                :name = food.name
                :price = food.price
                :weight = food.weight
                :photo = food.photo
                :description = food.description
              /> 
        </div>
      </div>

      <div v-for="category in this.categories">
        <div class="container p-4" v-if="category.positions.length != 0">
          <h3 class="fw-bolder">{{category.name}}</h3>
          <div class="row">
              <menuTopItem v-for="food in category.positions"
                :number = food.number
                :name = food.name
                :price = food.price
                :weight = food.weight
                :photo = food.photo
                :description = food.description
              /> 
          </div>
        </div>
      </div>

    </div>

    <downBar />
</template>

<style scoped>
  .view {
    margin-top: 88px;
  }
</style>

<script>
    import baseURL from "@/config"
    export default {
        data() {
            return {
                categories: [],
                populars: []
            }
        },
        mounted() { 
          this.init()
        },
        methods: {
          async init() {
            this.getPopular().then((data) => {
              this.populars = data
            })
            this.getAllCategories().then((data) => {
              for (let index in data) {
                let category = data[index]
                category.positions = []

                this.getFoods(category.code).then((foods) => {
                  category.positions = foods
                  this.categories.push(category)
                })
              }
            })
          },
          async getAllCategories() {
            const response = await fetch(`${baseURL}/api/category`, {
              method: "GET",
              mode: "cors"
            });
            const jsonData = await response.json();
            return jsonData
          },
          async getFoods(categoryCode) {
            const response = await fetch(`${baseURL}/api/category/${categoryCode}/positions`, {
              method: "GET",
              mode: "cors"
            });
            const jsonData = await response.json();
            return jsonData
          },
          async getPopular() {
            const response = await fetch(`${baseURL}/api/food/popular`, {
              method: "GET",
              mode: "cors"
            });
            const jsonData = await response.json();
            return jsonData
          }
        }
    }
</script>