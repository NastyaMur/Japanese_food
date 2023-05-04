<script setup>
    import navbar from '@/components/admin/navbar.vue'
    import loggout from '@/components/modal/loggout.vue'
</script>

<template>
    <navbar />

    <loggout />

    <div class="modal fade" id="userEdit" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Редактирование "{{this.name}}"</h1>
            <button type="button" id="userEditClose" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
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
                </select>
              </div>
              <div class="mb-2">
                <label for="photo" class="form-label">Фото</label>
                <div class="drop-zone">
                  <span class="drop-zone__prompt">Перетащите сюда фотографию или нажмите для выбора</span>
                  <input type="file" name="myFile" id="photo" class="drop-zone__input">
                </div>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Отменить</button>
            <button type="button" class="btn btn-success" v-on:click="userEdit()">Сохранить</button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="delete" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Внимание!</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <p>Вы уверены что хотите удалить пользователя <b>{{this.name}}</b></p>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Отменить</button>
            <button type="button" class="btn btn-danger" v-on:click="deleteUser()">Удалить</button>
          </div>
        </div>
      </div>
    </div>

    <div class="view">
      <div class="container">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="/admin">Панель администратора</a></li>
            <li class="breadcrumb-item active"><a href="/admin/users">Пользователи</a></li>
            <li class="breadcrumb-item active" aria-current="page">{{ name }}</li>
          </ol>
        </nav>
        <h2>{{ name }}</h2>
        <div class="btn-toolbar mb-4" role="toolbar">
          <div class="btn-group btn-group-sm me-2" role="group">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#userEdit"><font-awesome-icon :icon="['fas', 'pen']" class="me-2"/>Редактировать</button>
          </div>
          <div class="btn-group btn-group-sm me-2" role="group">
            <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#delete"><font-awesome-icon :icon="['fas', 'trash']" class="me-2"/>Удалить</button>
          </div>
          <div class="btn-group btn-group-sm me-2 ms-auto" role="group" v-if="this.me">
            <button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#loggout"><font-awesome-icon :icon="['fas', 'right-from-bracket']" class="me-2"/>Выйти</button>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6 col-12">
            <div class="card mb-4">
              <div class="card-body">
                <h5 class="card-title fw-bold mb-3">Основная информация</h5>
                <div class="card-text">
                  <div class="item d-flex">
                    <div class="col-3">
                        <p class="m-0 me-4 color-white">Имя:</p>
                    </div>
                    <div class="col-9">
                        <p class="m-0 me-4 color-white">{{ name }}</p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-3">
                        <p class="m-0 me-4 color-white">Почта:</p>
                    </div>
                    <div class="col-9">
                        <p class="m-0 me-4 color-white">{{ mail }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="card">
              <div class="card-body">
                <h5 class="card-title fw-bold mb-3">Заказы <span class="text-muted">{{orders.length}} шт.</span></h5>
                <div class="card-text">
                  <div class="item" v-for="orderItem in orders">
                    <div class="orderBloc alert alert-primary" role="alert" v-on:click="openOrder(orderItem.number)">
                      <div class="row justify-content-between">
                        <div class="col-6">
                          Заказ {{orderItem.number}}
                        </div>
                        <div class="col-4 text-end">
                          {{orderItem.sum}} Р
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6 col-12">
            <div class="card mb-4" v-if="this.photo" >
              <div class="card-body">
                <h5 class="card-title fw-bold mb-3">Фото</h5>
                <div class="card-text">
                  <div class="item text-center">
                    <img class="h-100 w-50" :src="this.photo">
                  </div>
                </div>
              </div>
            </div>
            <div class="card mb-4">
              <div class="card-body">
                <h5 class="card-title fw-bold mb-3">Роли</h5>
                <div class="card-text">
                  <div class="item">
                    <span class="badge bg-secondary">{{this.role}}</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="card">
              <div class="card-body">
                <h5 class="card-title fw-bold mb-3">История авторизации</h5>
                <div class="card-text">
                  <div class="item d-flex mb-3">
                    <div class="col-4">
                        <p class="m-0 me-4 color-white">Текущий токен:</p>
                    </div>
                    <div class="col-8">
                        <p class="m-0 me-4 color-white">{{ token }}</p>
                    </div>
                  </div>
                  <div class="m-0 p-0" v-for="auth in auths">
                    <div class="alert alert-success p-2" role="alert" v-if="auth.active">
                      <div class="row justify-content-between">
                        <div class="ms-2">
                          Выполнен вход: {{ getDate(auth.created) }}
                        </div>
                      </div>
                    </div>
                    <div class="alert alert-danger p-2" role="alert" v-if="!auth.active">
                      <div class="row justify-content-between">
                        <div class="ms-2">
                          Выполнен вход: {{ getDate(auth.created) }}
                        </div>
                      </div>
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
.orderBloc {
  cursor: pointer;
  transition: .3s;
}
.orderBloc:hover {
  transform: scale(.99);
}
.drop-zone {
  max-width: 100%;
  height: 200px;
  padding: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-family: "Quicksand", sans-serif;
  font-weight: 500;
  font-size: 20px;
  cursor: pointer;
  color: #cccccc;
  border: 2px dashed #999;
  border-radius: 10px;
}

.drop-zone--over {
  border-style: solid;
}

.drop-zone__input {
  display: none;
}

.drop-zone__thumb {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  overflow: hidden;
  background-color: #cccccc;
  background-size: cover;
  position: relative;
}

.drop-zone > div > div {
  content: attr(data-label);
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 5px 0;
  color: #ffffff;
  background: rgba(0, 0, 0, 0.75);
  font-size: 14px;
  text-align: center;
}


</style>

<script>

  import baseURL from "@/config"
  import { useCookies } from "vue3-cookies"

  export default {
        data() {
            return { 
                name: '............',
                mail: '............',
                number: null,
                token: null,
                photo: null,
                me: false,
                orders: [],
                auths: [],
                role: '.........',
                roles: []
            }
        },
        mounted() {
            this.init()

            document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
              const dropZoneElement = inputElement.closest(".drop-zone");

              dropZoneElement.addEventListener("click", (e) => {
                inputElement.click();
              });

              inputElement.addEventListener("change", (e) => {
                if (inputElement.files.length) {
                  updateThumbnail(dropZoneElement, inputElement.files[0]);
                }
              });

              dropZoneElement.addEventListener("dragover", (e) => {
                e.preventDefault();
                dropZoneElement.classList.add("drop-zone--over");
              });

              ["dragleave", "dragend"].forEach((type) => {
                dropZoneElement.addEventListener(type, (e) => {
                  dropZoneElement.classList.remove("drop-zone--over");
                });
              });

              dropZoneElement.addEventListener("drop", (e) => {
                e.preventDefault();

                if (e.dataTransfer.files.length) {
                  inputElement.files = e.dataTransfer.files;
                  this.updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
                }
                dropZoneElement.classList.remove("drop-zone--over");
              });
            });

        },
        methods: {    
          async init() {
            const path = this.$route.path
            let number = path.substring(path.lastIndexOf('/') + 1, path.length)

            const { cookies } = useCookies();
            this.token = cookies.get("token")

            this.getData(number).then((data) => {
                this.name = data.name
                this.mail = data.email
                this.photo = data.photo
                this.number = data.number
                this.orders = data.orders
                this.me = data.me

                document.getElementById('name').value = this.name
                document.getElementById('email').value = this.mail

                this.getAuths(number).then((data) => {
                  data = data.sort((a, b) => (a.created > b.created) ? -1 : 1)
                  this.auths = data
                })

                this.getRoles().then((roles) => {
                    this.roles = roles

                    for(let index = 0; index < roles.length; index++) {
                      let opt = document.createElement('option')
                      opt.value = roles[index].code
                      opt.innerHTML = roles[index].name

                      let allowed = false
                      for (let kindex in document.getElementById('roles').childNodes) {
                        if ( document.getElementById('roles').childNodes[kindex].value == roles[index].code ) {
                          allowed = true
                        }
                      }
                      if (!allowed) {
                        document.getElementById('roles').appendChild(opt);
                      }

                      if (roles[index].code == data.roles[0]) {
                        this.role = roles[index].name
                        document.getElementById('roles').value = roles[index].code
                      }
                    }
                })
            })
          },
          async userEdit() {
            let bodies = {}

            let name = document.getElementById('name').value
            let email = document.getElementById('email').value
            let role = document.getElementById('roles').value
            let elemPhoto = document.getElementsByClassName('drop-zone__thumb')[0]
            let photo = null
            if ( elemPhoto ) {
              photo = getComputedStyle( elemPhoto ).backgroundImage
              photo = photo.replace('url("', '').replaceAll('")', '')
            }

            if ( name && name != '') { bodies.name = name }
            if ( email && email != '') { bodies.email = email }
            if ( role && role != '') { bodies.roles = [ role ] }
            if ( photo && photo != '') { bodies.photo = photo }
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/user/${this.number}`, {
              method: "POST",
              mode: "cors",
              body: JSON.stringify(bodies),
              headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            this.init();
            document.getElementById('userEditClose').click()
          },
          updateThumbnail(dropZoneElement, file) {
            let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");

            // First time - remove the prompt
            if (dropZoneElement.querySelector(".drop-zone__prompt")) {
              dropZoneElement.querySelector(".drop-zone__prompt").remove();
            }

            // First time - there is no thumbnail element, so lets create it
            if (!thumbnailElement) {
              thumbnailElement = document.createElement("div");
              thumbnailElement.classList.add("drop-zone__thumb");

              thumbnailElement.style.width = '100%'
              thumbnailElement.style.height = '100%'
              thumbnailElement.style.borderRadius = "10px";
              thumbnailElement.style.overflow = "hidden";
              thumbnailElement.style.backgroundColor = "#cccccc";
              thumbnailElement.style.backgroundSize = "cover";
              thumbnailElement.style.position = "relative";

              thumbnailElement.classList.remove("d-none");
              dropZoneElement.appendChild(thumbnailElement);
            }

            thumbnailElement.dataset.label = file.name;

            // Show thumbnail for image files
            if (file.type.startsWith("image/")) {
              const reader = new FileReader();

              reader.readAsDataURL(file);
              reader.onload = () => {
                thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
              };
            } else {
              thumbnailElement.style.backgroundImage = null;
            }
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
          async getAuths() {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/session/user/${this.number}`, {
              method: "GET",
              mode: "cors",
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            return jsonData
          },
          async getData(number) {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/user/${number}`, {
              method: "GET",
              mode: "cors",
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            return jsonData
          },
          openOrder(number) {
            window.location.href = `/admin/order/${number}`
          },
          async deleteUser() {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/user`, {
              method: "DELETE",
              mode: "cors",
              body: JSON.stringify({
                "email" : this.mail
              }),
              headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            window.location.href = "/admin/users"
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
        }
    }
</script>