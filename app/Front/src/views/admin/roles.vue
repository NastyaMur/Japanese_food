<script setup>
    import navbar from '@/components/admin/navbar.vue'
</script>

<template>
    <navbar />

    <div class="modal fade" id="createRole" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Создание новой роли</h1>
            <button type="button" id="createRoleClosed" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-2">
                <label for="name" class="form-label">Название <span class="text-danger">*</span></label>
                <input id="name" type="text" class="form-control">
              </div>
              <div class="mb-2">
                <label for="code" class="form-label">Код <span class="text-danger">*</span></label>
                <input id="code" type="text" class="form-control">
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
            <li class="breadcrumb-item active" aria-current="page">Роли</li>
          </ol>
        </nav>
        <h2>Роли</h2>
        <div class="btn-toolbar mb-4" role="toolbar">
          <div class="btn-group btn-group-sm me-2" role="group">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createRole">
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
                    <th scope="col">Название</th>
                    <th scope="col">Код</th>
                    <th class="text-center" scope="col">Удалить</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="role in items">
                    <th>{{role.name}}</th>
                    <td class="text-muted">{{role.code}}</td>
                    <td class="text-center text-danger" v-if="!role.lock" v-on:click="deleteRole(role.code)"><font-awesome-icon :icon="['fas', 'trash']"/></td>
                    <td class="text-center text-primary" v-if="role.lock"><font-awesome-icon :icon="['fas', 'lock']"/></td>
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
            this.init()
        },
        methods: {
          async init() {
            this.getRoles().then((data) => {
              this.items = data
              console.log(data)
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
          async create() {
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/role`, {
              method: "PUT",
              mode: "cors",
              body: JSON.stringify({
                "name" : document.getElementById('name').value,
                "code" : document.getElementById('code').value
              }),
              headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            this.init()
            document.getElementById('createRoleClosed').click()
            document.getElementById('name').value = ''
            document.getElementById('code').value = ''
          },
          async deleteRole(code) {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/role/${code}`, {
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