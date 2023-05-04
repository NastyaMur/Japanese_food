<template>
  <div class="container">
    <div class="login_header">
      <div class="d-flex">
        <div class="p-2 flex-grow-1 align-self-center">
          <h2>Japanese Food</h2>
        </div>
        <div class="p-2 align-self-center">
          <a href="/register">Регистрация</a>
        </div>
      </div>
      <hr class="m-0">
    </div>
    <div class="bg-1">
      <div class="form text-center">
        <div class="row">
          <p class="display-1">🍱</p>
          <p class="fw-light">Введите ваши данные указанные при регистрации для доступа</p>
          <div class="row justify-content-md-center">
            <div class="col-lg-4 col-md-6 col-12">
              <div id="errorAuthToast" class="toast align-items-center text-bg-danger border-0 mb-4">
                <div class="d-flex">
                  <div class="toast-body">
                    Логин или пароль введен не верно!
                  </div>
                  <button type="button" class="btn-close btn-close-white me-2 m-auto" v-on:click="hideToast()"></button>
                </div>
              </div>

              <div class="mb-3">
                <input type="email" class="form-control" id="login" placeholder="Логин">
              </div>
              <div class="mb-3">
                <input type="password" class="form-control" id="pass" placeholder="Пароль">
              </div>
              <button v-on:click="sumbit()" type="button" class="btn btn-dark">Войти</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
  .form {
    width: 80%;
    padding: 40px;
    border-radius: 23px;
    background-color: white;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
</style>

<script>
    import baseURL from "@/config"
    import { useCookies } from "vue3-cookies";
    import md5 from "js-md5"

    export default {
        data() {
            return { 
                data: {}
            }
        },
        setup() {
          const { cookies } = useCookies();
          return { cookies };
        },
        created() {
        },
        mounted() {
        },
        methods: {
          hideToast() {
            const toast = document.getElementById('errorAuthToast')
            toast.classList.remove('d-block')
          },
          async login(mail, pass) {
            const response = await fetch(`${baseURL}/api/user/login`, {
              method: "POST",
              mode: "cors",
              headers: {
                "Content-Type": "application/json"
              },
              body: JSON.stringify({
                'email': mail,
                "hash_pass" : md5(pass)
              })
            });
            const jsonData = await response.json();
            return jsonData
          },
          async sumbit() {
            let login = document.getElementById('login').value
            let pass = document.getElementById('pass').value

            this.login(login, pass).then((data) => {
              if (data.detail.type == 'error') {
                const toast = document.getElementById('errorAuthToast')
                toast.classList.add('d-block')
              }
              if (data.detail.type == 'success') {
                this.cookies.set("token", data.detail.data.token)
                window.location.href = "/admin"
              }
            });
          }
        }
    }
</script>