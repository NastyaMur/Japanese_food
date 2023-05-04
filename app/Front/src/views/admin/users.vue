<script setup>
    import navbar from '@/components/admin/navbar.vue'
</script>

<template>
    <navbar />

    <div class="modal fade" id="createUser" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Создание нового пользователя</h1>
            <button type="button" id="createUserClosed" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-2">
                <label for="name" class="form-label">ФИО <span class="text-danger">*</span></label>
                <input id="name" type="text" class="form-control">
              </div>
              <div class="mb-2">
                <label for="email" class="form-label">Почта <span class="text-danger">*</span></label>
                <input id="email" type="email" class="form-control">
              </div>
              <div class="mb-2">
                <label for="roles" class="form-label">Роль</label>
                <select id="roles" class="form-select">
                  <option v-for="role in roles">
                    {{role.name}}
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
            <li class="breadcrumb-item active" aria-current="page">Пользователи</li>
          </ol>
        </nav>
        <h2>Пользователи</h2>
        <div class="btn-toolbar mb-4" role="toolbar">
          <div class="btn-group btn-group-sm me-2" role="group">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createUser">
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
                    <th scope="col">Имя</th>
                    <th scope="col">Почта</th>
                    <th class="text-center" scope="col">Удалить</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="user in items">
                    <th v-on:click="open(user.number)">{{user.number}}</th>
                    <td v-on:click="open(user.number)">{{user.name}}</td>
                    <td v-on:click="open(user.number)">{{user.email}}</td>
                    <td class="text-center text-danger" v-on:click="deleteUser(user.email)"><font-awesome-icon :icon="['fas', 'trash']"/></td>
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
                roles: []
            }
        },
        mounted() {
            this.init()
        },
        methods: {
          async init() {
            this.getRoles().then((data) => {
              this.roles = data
            })
            this.getUsers().then((data) => {
              this.items = data
            })
          },
          async getRoles() {
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/role`, {
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
          async create() {
            let roleCode = ''
            let roleName = document.getElementById('roles').value
            for (let index in this.roles) {
                if (this.roles[index].name == roleName) {
                  roleCode = this.roles[index].code
                }
            }

            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/user`, {
              method: "PUT",
              mode: "cors",
              body: JSON.stringify({
                "name" : document.getElementById('name').value,
                "email" : document.getElementById('email').value,
                "password" : '123',
                "roles" : [roleCode]
              }),
              headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            this.init()
            document.getElementById('createUserClosed').click()
          },
          open(number) {
            window.location.href = `/admin/user/${number}`
          },
          async deleteUser(email) {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/user`, {
              method: "DELETE",
              mode: "cors",
              body: JSON.stringify({
                "email" : email
              }),
              headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json()
            this.init()
          }
        }
    }
</script>