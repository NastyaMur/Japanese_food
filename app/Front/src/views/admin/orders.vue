<script setup>
    import navbar from '@/components/admin/navbar.vue'
</script>

<template>
    <navbar />

    <div class="view">
      <div class="container">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="/admin">Панель администратора</a></li>
            <li class="breadcrumb-item active" aria-current="page">Заказы</li>
          </ol>
        </nav>
        <h2>Заказы</h2>
        <!-- <div class="btn-toolbar mb-4" role="toolbar">
          <div class="btn-group btn-group-sm me-2" role="group">
            <button type="button" class="btn btn-primary"><font-awesome-icon :icon="['fas', 'plus']" class="me-2"/>Добавить</button>
          </div>
        </div> -->
        <div class="row">
          <div class="col-12">
            <div class="card-text">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Номер</th>
                    <th scope="col">Автор</th>
                    <th scope="col">Роль</th>
                    <th scope="col">Товары</th>
                    <th scope="col">Статус</th>
                    <th scope="col">Сумма</th>
                    <th scope="col">Описание</th>
                    <th scope="col">Создан</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="order in items" v-on:click="open(order.number)">
                    <th>{{order.number}}</th>
                    <td>{{order.author.name}}</td>
                    <td><span class="text-muted">{{order.author.roles[0].name}}</span></td>
                    <td>{{order.positions.length}} шт.</td>
                    <td>{{ this.getStatus(order.status)}}</td>
                    <td>{{order.sum}} ₽</td>
                    <td>{{order.description}}</td>
                    <td>{{ getDate(order.created) }}</td>
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
                items: []
            }
        },
        mounted() {
            this.getOrder().then((data) => {
                this.items = data
                console.log(data)
            })
        },
        methods: {
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
          getStatus(statusCode) {
            let order_states = {
                'new' : '🔴 Новый',
                'inprogress' : '🟡 В работе',
                'ontable' : '🔵 На выдаче',
                'closed' : '🟢 Выполнен',
                'canceled' : '⚫️ Отменен'
            }
            return order_states[(statusCode)]
          },
          getDate(strTimeCode) {
              let date = new Date(Number(strTimeCode))

              let day = date.getDate()
              let month = date.getMonth()
              let year = date.getYear() + 1900

              let hours = date.getHours()
              let minuts = date.getMinutes()

              if (day.toString().length == 1) {
                day = '0' + day.toString()
              }
              if (month.toString().length == 1) {
                month = '0' + month.toString()
              }
              if (hours.toString().length == 1) {
                hours = '0' + hours.toString()
              }
              if (minuts.toString().length == 1) {
                minuts = '0' + minuts.toString()
              }


              return `${day}.${month}.${year} ${hours}:${minuts}`
          },
          open(number) {
            window.location.href = `/admin/order/${number}`
          }
        }
    }
</script>