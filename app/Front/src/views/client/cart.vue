<script setup>
    import navbar from '@/components/client/navbar.vue'
    import downBar from '@/components/client/footer.vue'
</script>

<template>
  <navbar />

  <div class="view">
    <div class="container p-4">
      <h3 class="fw-bolder">Корзина</h3>
      <div class="row mt-4 justify-content-between">
          <div class="col-xl-6 col-md-8 col-12">
            <div class="mt-3 mb-5" v-if="this.foods.length == 0">
              <h5>К сожалению ваша корзина еще пустая, скорей исправьте это!</h5>
            </div>
            <div class="item shadow" v-for="food in this.foods">
              <div class="row align-items-center">
                <div class="col-2 ps-4 text-center">
                  <img v-if="food.photo" class="images" :src="food.photo" alt="">
                  <img v-if="!food.photo" class="images" src="@/assets/image/no_image_food.png" alt="">
                </div>
                <div class="col-4 fw-bolder pse-4">{{food.name}}</div>
                <div class="col-3 text-end">
                  <div class="btn-group btn-group-sm" role="group" aria-label="Basic example">
                    <button type="button" class="btn btn-primary" v-on:click="foodMinus(food.number)">-</button>
                    <button disabled type="button" class="btn btn-primary">{{food.count}}</button>
                    <button type="button" class="btn btn-primary" v-on:click="foodPlus(food.number)">+</button>
                  </div>
                </div>
                <div class="col-3 text-center p-4"><span class="fw-bold">{{food.price * food.count}}</span> ₽</div>
              </div>
            </div>
          </div>
          <div class="col-md-4 col-12">
            <div class="item shadow p-4">
              <h5>Заказ</h5>
              <p>Сумма: <span class="fw-bold">{{this.sum}}</span> ₽</p>
              <button type="button" class="btn btn-primary" v-if="this.foods.length != 0" v-on:click="buy()">Заказать</button>
            </div>
            <div class="item shadow p-4">
              <div class="d-flex justify-content-between">
                  <h5>Аккаунт</h5>
                  <span v-if="user.number" class="text-danger" v-on:click="loggout()">Выйти</span>
              </div>
              <p v-if="!user.number">Необходима <a href="/login">aвторизация</a></p>
              <p v-if="user.number" class="mb-0"><span class="text-muted">Имя: </span>{{this.user.name}}</p>
              <p v-if="user.number" class="mb-0"><span class="text-muted">Почта: </span>{{this.user.mail}}</p>
            </div>
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
  .item {
    margin-bottom: 20px;
    border-radius: 23px;
    transition: .3s;
  }
  .images {
    width: 60%;
  }
</style>

<script>
    import baseURL from "@/config"
    import { useCookies } from "vue3-cookies";

    export default {
        data() {
          return {
            foods: [],
            user: {},
            sum: 0
          }
        },
        setup() {
          const { cookies } = useCookies();
          return { cookies };
        },
        mounted() {
          this.init()
        },
        methods: {
          async init() {
            this.getMe().then((data) => {
                if (data.number) {
                  this.user.name = data.name
                  this.user.mail = data.email
                  this.user.photo = data.photo
                  this.user.number = data.number
                }
            })

            this.foods = []
            this.getCartData().then((data) => {
              this.sum = 0
              for (let index in data) {
                let foodNumber = data[index]
                let accept = false
                
                this.getFood(foodNumber).then((foodData) => {
                  for (let kindex in this.foods) {

                    let currentFood = this.foods[kindex]
                    if (currentFood.number == foodNumber) {
                      accept = true
                      currentFood.count = currentFood.count + 1
                    }
                  }
                  
                  if (!accept) {
                    foodData.count = 1
                    this.foods.push(foodData)
                  }
                  this.sum += foodData.price
                })
              }
            })
            this.foods.sort((a, b) => a.name > b.name ? 1 : -1);
          },
          async getCartData() {
            const { cookies } = useCookies();
            let cart = JSON.parse(cookies.get("cart"))
            if (cart == null || cart == '') {
              cart = []
            }
            return cart
          },
          foodPlus(foodNumber) {
            const { cookies } = useCookies();
            let cart = JSON.parse(cookies.get("cart"))
            if (cart == null || cart == '') {
              cart = []
            }
            cart.push(foodNumber)
            cookies.set("cart", JSON.stringify(cart))
            this.init()
          },
          foodMinus(foodNumber) {
            const { cookies } = useCookies();
            let cart = JSON.parse(cookies.get("cart"))
            if (cart == null || cart == '') {
              cart = []
            }

            delete cart[cart.indexOf(foodNumber)]
            cookies.set("cart", JSON.stringify(cart.filter(element => element != null)))
            this.init()
          },
          async getFood(foodNumber) {
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/food/${foodNumber}`, {
              method: "GET",
              mode: "cors",
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            return jsonData
          },
          async getMe() {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/user/me`, {
              method: "GET",
              mode: "cors",
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            return jsonData
          },
          async loggout() {
            const { cookies } = useCookies();
            cookies.remove("token", null)
            window.location.href = `/`
          },
          async buy() {
            const { cookies } = useCookies();
            let cart = JSON.parse(cookies.get("cart"))

            const response = await fetch(`${baseURL}/api/order`, {
              method: "PUT",
              body: JSON.stringify({
                "positions" : cart
              }),
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`,
                "Content-Type": "application/json"
              },
            });
            const jsonData = await response.json();
            cookies.set("cart", JSON.stringify([]))
            this.init()
            return jsonData
          }
        }
    }
</script>

