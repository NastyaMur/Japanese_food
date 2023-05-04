<template>
  <div class="container">
    <div class="login_header">
      <div class="d-flex">
        <div class="p-2 flex-grow-1 align-self-center">
          <h2>Japanese Food</h2>
        </div>
        <div class="p-2 align-self-center">
          <a href="/login">Уже есть аккаунт?</a>
        </div>
      </div>
      <hr class="m-0">
    </div>
    <div class="bg-1">
      <div class="form text-center">
        <div class="row">
          <p class="display-1">🍱</p>
          <h3>Регистрация</h3>
          <p class="fw-light">Введите ваши данные для доступа к заказу товаров</p>
          <div class="row justify-content-md-center">
            <div class="col-lg-4 col-md-6 col-12">
              <div id="usedMail" class="toast align-items-center text-bg-warning border-0 mb-4">
                <div class="d-flex">
                  <div class="toast-body">
                    К сожалению пользователь с такой почтой уже зарегистрирован!
                  </div>
                  <button type="button" class="btn-close btn-close-white me-2 m-auto" v-on:click="hideToast('fieldEmpty')"></button>
                </div>
              </div>
              <div id="fieldEmpty" class="toast align-items-center text-bg-danger border-0 mb-4">
                <div class="d-flex">
                  <div class="toast-body">
                    Проверьте заполненость всех полей!
                  </div>
                  <button type="button" class="btn-close btn-close-white me-2 m-auto" v-on:click="hideToast('fieldEmpty')"></button>
                </div>
              </div>
              <div id="passNotCurrent" class="toast align-items-center text-bg-danger border-0 mb-4">
                <div class="d-flex">
                  <div class="toast-body">
                    Ваши пароли не совпадают!
                  </div>
                  <button type="button" class="btn-close btn-close-white me-2 m-auto" v-on:click="hideToast('passNotCurrent')"></button>
                </div>
              </div>

              <div class="mb-3">
                <input type="name" class="form-control" id="name" placeholder="Имя">
              </div>
              <div class="mb-3">
                <input type="email" class="form-control" id="email" placeholder="Почта">
              </div>
              <div class="mb-3">
                <input type="password" class="form-control" id="pass" placeholder="Пароль">
              </div>
              <div class="mb-3">
                <input type="password" class="form-control" id="pass2" placeholder="Подтвердите пароль">
              </div>
              <button v-on:click="sumbit()" type="button" class="btn btn-success mt-2">Создать аккаунт</button>
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
          hideToast(id) {
            const toast = document.getElementById(id)
            toast.classList.remove('d-block')
          },
          async register(mail, name, pass) {
            const response = await fetch(`${baseURL}/api/user`, {
              method: "PUT",
              mode: "cors",
              headers: {
                "Content-Type": "application/json"
              },
              body: JSON.stringify({
                'email': mail,
                'name': name,
                "password" : md5(pass)
              })
            });
            const jsonData = await response.json();
            return jsonData
          },
          async login(mail, pass) {
            const response = await fetch(`${baseURL}/api/login`, {
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
            email = document.getElementById('email').value
            name = document.getElementById('name').value
            pass = document.getElementById('pass').value
            pass2 = document.getElementById('pass2').value

            if (email && name && pass && pass2) {
              if (pass == pass2) {
                this.register(email, name, pass).then((data) => {
                  if (data.detail.type == 'error') {
                    const toast = document.getElementById('usedMail')
                    toast.classList.add('d-block')
                  }
                  if (data.detail.type == 'success') {
                    this.login(email, pass).then((data) => {
                      this.cookies.set("token", data.detail.data.token)
                      window.location.href = "/"
                    });
                  }
                });
              } else {
                const toast = document.getElementById('passNotCurrent')
                toast.classList.add('d-block')
              }
            } else {
              const toast = document.getElementById('fieldEmpty')
              toast.classList.add('d-block')
            }
          }
        }
    }
</script>