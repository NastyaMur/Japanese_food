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
            <li class="breadcrumb-item active"><a href="/admin/orders">Заказы</a></li>
            <li class="breadcrumb-item active" aria-current="page">Заказ {{ number }}</li>
          </ol>
        </nav>
        <h2 class="mb-3">Заказ {{ number }}</h2>
        <div class="btn-toolbar mb-4" role="toolbar">
          <div class="btn-group btn-group-sm me-2" role="group">
            <button type="button" class="btn btn-danger text-white" v-if="allowStatus.includes('new')" v-on:click="changeState('new')"><font-awesome-icon :icon="['fas', 'square']" class="me-2"/>Новый</button>
            <button type="button" class="btn btn-warning text-white" v-if="allowStatus.includes('inprogress')" v-on:click="changeState('inprogress')"><font-awesome-icon :icon="['fas', 'play']" class="me-2"/>В работу</button>
            <button type="button" class="btn btn-primary" v-if="allowStatus.includes('ontable')" v-on:click="changeState('ontable')"><font-awesome-icon :icon="['fas', 'dolly']" class="me-2"/>На выдаче</button>
            <button type="button" class="btn btn-success" v-if="allowStatus.includes('closed')" v-on:click="changeState('closed')"><font-awesome-icon :icon="['fas', 'check']" class="me-2"/>Выполнен</button>
          </div>
          <div class="btn-group btn-group-sm me-2" role="group">
            <button type="button" class="btn btn-dark" v-if="allowStatus.includes('canceled')" v-on:click="changeState('canceled')"><font-awesome-icon :icon="['fas', 'square']" class="me-2"/>Отменить</button>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6 col-12">
            <div class="card mb-4">
              <div class="card-body">
                <h5 class="card-title fw-bold mb-3">Основная информация</h5>
                <div class="card-text">
                  <div class="item d-flex">
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">Номер заказа</p>
                    </div>
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">{{ number }}</p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">Статус:</p>
                    </div>
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">{{status}}</p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">Сумма:</p>
                    </div>
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">{{ sum }} ₽</p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">Дата создания:</p>
                    </div>
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">
                          {{ created }}
                        </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="card mb-4">
              <div class="card-body">
                <h5 class="card-title fw-bold mb-3">Дополнительно</h5>
                <div class="card-text">
                  <div class="item d-flex">
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">Описание:</p>
                    </div>
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">
                          {{ description }}
                        </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="card">
              <div class="card-body">
                <h5 class="card-title fw-bold mb-3">Позиции заказа <span class="text-muted">{{positions.length}} шт.</span></h5>
                <div class="card-text">
                  <div class="item">
                    <div class="foodBloc alert alert-info" role="alert" v-for="food in positions" v-on:click="openFood(food.number)">
                      <div class="row justify-content-between">
                        <div class="col-6">
                          1 x {{food.name}}
                        </div>
                        <div class="col-4 text-end">
                          {{food.price}} ₽
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6 col-12">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title fw-bold mb-3">Покупатель</h5>
                <div class="card-text">
                  <div class="item d-flex">
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">Имя:</p>
                    </div>
                    <div class="col-6">
                        <a :href="'/admin/user/' + author.number" class="m-0 me-4 color-white">{{ author.name }}</a>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">Почта:</p>
                    </div>
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">{{ author.email }}</p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">Заказов:</p>
                    </div>
                    <div class="col-6">
                        <p class="m-0 me-4 color-white">{{ author?.orders?.length }} шт.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<style scoped>
  .foodBloc {
    cursor: pointer;
    transition: .3s;
  }
  .foodBloc:hover {
    transform: scale(.99);
  }
</style>

<script>

  import baseURL from "@/config"
  import { useCookies } from "vue3-cookies";

  export default {
        data() {
            return { 
                number: '............',
                author: {},
                status: null,
                // allowNew: false,
                allowStatus: [],
                sum: '............',
                created: '............',
                description: '',
                positions: [],
                cookies: null
            }
        },
        mounted() {
            this.init()
        },
        methods: {
          async changeState (statusCode) {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/order/${this.number}`, {
              method: "POST",
              mode: "cors",
              body: JSON.stringify({
                'status' : statusCode
              }),
              headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            this.init()
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
          async getData(number) {
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/order/${number}`, {
              method: "GET",
              mode: "cors",
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            return jsonData
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
          openFood(number) {
            window.location.href = `/admin/food/${number}`
          },
          async init() {
            this.getData(this.$route.params.number).then((data) => {
            console.log(data)
            this.number = data.number
            this.author = data.author
            this.status = this.getStatus(data.status)
            this.sum = data.sum
            this.created = this.getDate(data.created)
            this.positions = data.positions
            this.allowStatus = data.allow_status

            if (data.description != '' && data.description != null && data.description != 'null') {
              this.description = data.description
            } else {
              this.description = 'Отсутствует'
            }
            })
          }
        }
    }
</script>