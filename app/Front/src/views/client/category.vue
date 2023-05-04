<script setup>
    import navbar from '@/components/client/navbar.vue'
    import menuTopItem from '@/components/client/menuTopItem.vue'
    import downBar from '@/components/client/footer.vue'
</script>

<template>
    <navbar />

    <div class="view">
      <div class="container p-4">
        <h3 class="fw-bolder">{{this.categoryName}}</h3>
        <div class="row">
            <menuTopItem v-for="food in items"
              :number = food.number
              :name = food.name
              :price = food.price
              :photo = food.photo
              :description = food.description
            />
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
                items: [],
                categoryCode: null,
                categoryCodeOld: null,
                categoryName: null
            }
        },
        created() { 
          this.init()
        },
        updated() { 
          this.getCategoryCode().then((code) => {
            if (code != this.categoryCodeOld) {
              this.categoryCodeOld = code
              this.init()
            }
          })
        },
        methods: {
          async init() {
            this.getCategoryCode().then((code) => {
              this.categoryCode = code

              this.getCategory(code).then((data) => {
                this.categoryName = data.name
              })

              this.getFoods(code).then((foods) => {
                this.items = foods
              })
            })
          },
          async getCategoryCode() {
            let path = this.$route.path
            return path.substring(path.lastIndexOf('/') + 1, path.length)
          },
          async getCategory(code) {
            const response = await fetch(`${baseURL}/api/category/${code}`, {
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
          }
        }
    }
</script>