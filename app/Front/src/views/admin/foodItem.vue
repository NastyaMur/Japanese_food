<script setup>
    import navbar from '@/components/admin/navbar.vue'
</script>

<template>
    <navbar />

    <div class="modal fade" id="foodEdit" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Редактирование "{{this.name}}"</h1>
            <button type="button" id="foodEditClosed" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-2">
                <label for="name" class="form-label">Наименование <span class="text-danger">*</span></label>
                <input id="name" type="text" class="form-control">
              </div>
              <div class="mb-2">
                <label for="price" class="form-label">Стоимость <span class="text-danger">*</span></label>
                <input id="price" type="number" class="form-control">
              </div>
              <div class="mb-2">
                <label for="weight" class="form-label">Масса блюда (г.) <span class="text-danger">*</span></label>
                <input id="weight" type="number" class="form-control">
              </div>
              <div class="mb-2">
                <label for="category" class="form-label">Категория</label>
                <select id="category" class="form-select">
                </select>
              </div>
              <div class="mb-2">
                <label for="description" class="form-label">Описание <span class="text-danger">*</span></label>
                <textarea id="description" type="text" class="form-control"></textarea>
              </div>
              <div class="mb-2">
                <label for="popular" class="form-label">Выводить в топе</label>
                <input type="checkbox" id="popular" class="ms-3" checked>
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
            <button type="button" class="btn btn-success" v-on:click="foodEdit()">Сохранить</button>
          </div>
        </div>
      </div>
    </div>

    <div class="view">
      <div class="container">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="/admin">Панель администратора</a></li>
            <li class="breadcrumb-item active"><a href="/admin/foods">Товары</a></li>
            <li class="breadcrumb-item active" aria-current="page">{{ this.name }}</li>
          </ol>
        </nav>
        <h2 class="mb-3">{{ this.name }}</h2>
        <div class="btn-toolbar mb-4" role="toolbar">
          <div class="btn-group btn-group-sm me-2" role="group">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#foodEdit">
              <font-awesome-icon :icon="['fas', 'pen']" class="me-2"/>Редактировать
            </button>
            <button type="button" class="btn btn-dark" v-on:click="toggleRemovedFood(this.number)">
              <font-awesome-icon :icon="['fas', 'box-archive']" class="me-2"/>
              <span v-if="this.active">В архив</span>
              <span v-if="!this.active">Вернуть из архива</span>
            </button>
          </div>
          <div class="btn-group btn-group-sm me-2" role="group">
            <button type="button" class="btn btn-danger" v-on:click="deleteFood(this.number)">
              <font-awesome-icon :icon="['fas', 'trash']" class="me-2"/>Удалить
            </button>
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
                        <p class="m-0 me-4 color-white">Номер товара:</p>
                    </div>
                    <div class="col-9">
                        <p class="m-0 me-4 color-white">{{ number }}</p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-3">
                        <p class="m-0 me-4 color-white">Наименование:</p>
                    </div>
                    <div class="col-9">
                        <p class="m-0 me-4 color-white">{{ name }}</p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-3">
                        <p class="m-0 me-4 color-white">Категория:</p>
                    </div>
                    <div class="col-9">
                        <p class="m-0 me-4 color-white">{{ categoryName }}</p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-3">
                        <p class="m-0 me-4 color-white">Стоимость:</p>
                    </div>
                    <div class="col-9">
                        <p class="m-0 me-4 color-white">{{ price }} ₽</p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-3">
                        <p class="m-0 me-4 color-white">Масса:</p>
                    </div>
                    <div class="col-9">
                        <p class="m-0 me-4 color-white">{{ weight }} г.</p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-3">
                        <p class="m-0 me-4 color-white">Описание:</p>
                    </div>
                    <div class="col-9">
                        <p class="m-0 me-4 color-white">
                          {{ description }}
                        </p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-3">
                        <p class="m-0 me-4 color-white">Сейчас в топе:</p>
                    </div>
                    <div class="col-9">
                        <p class="m-0 me-4 color-white">
                          <span v-if="popular">✅</span>
                          <span v-if="!popular">❌</span>
                        </p>
                    </div>
                  </div>
                  <div class="item d-flex">
                    <div class="col-3">
                        <p class="m-0 me-4 color-white">Активен:</p>
                    </div>
                    <div class="col-9">
                        <p class="m-0 me-4 color-white">
                          <span v-if="active">✅</span>
                          <span v-if="!active">❌</span>
                        </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6 col-12">
            <div class="card" v-if="this.photo">
              <div class="card-body">
                <h5 class="card-title fw-bold mb-3">Фото</h5>
                <div class="card-text text-center">
                  <img class="w-50" :src="this.photo">
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
  import { useCookies } from "vue3-cookies";

  export default {
        data() {
            return { 
                number: '............',
                name: '............',
                price: '............',
                photo: '............',
                categoryName: '',
                categoryCode: '',
                description: '',
                active: true,
                popular: true,
                cookies: null
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
            this.getData(this.$route.params.number).then((data) => {
              console.log(data)
              this.number = data.number
              this.name = data.name
              this.price = data.price
              this.photo = data.photo
              this.active = data.active
              this.popular = data.popular
              this.weight = data.weight

              document.getElementById('name').value = this.name
              document.getElementById('price').value = this.price
              document.getElementById('weight').value = this.weight
              document.getElementById('popular').checked = this.popular

              this.getAllCategory().then((allCategory) => {
                for(let index in allCategory) {
                  let opt = document.createElement('option')
                  opt.value = allCategory[index].code
                  opt.innerHTML = allCategory[index].name

                  let allowed = false
                  for (let kindex in document.getElementById('category').childNodes) {
                    if ( document.getElementById('category').childNodes[kindex].value == allCategory[index].code ) {
                      allowed = true
                    }
                  }
                  if (!allowed) {
                    document.getElementById('category').appendChild(opt)
                  }

                  if (data.category && allCategory[index].code == data.category) {
                    this.categoryName = allCategory[index].name
                    this.categoryCode = allCategory[index].code
                    document.getElementById('category').value = allCategory[index].code
                  }
                }
                if (this.categoryName == '') {
                  this.categoryName = 'Не указана'
                }
              })

              if (data.description != '' && data.description != null && data.description != 'null') {
                this.description = data.description
                document.getElementById('description').value = this.description
              } else {
                this.description = 'Отсутствует'
              }
                
            })
          },
          async foodEdit() {
            let bodies = {}
            let name = document.getElementById('name').value
            let price = document.getElementById('price').value
            let description = document.getElementById('description').value
            let category = document.getElementById('category').value
            let weight = document.getElementById('weight').value
            let elemPhoto = document.getElementsByClassName('drop-zone__thumb')[0]
            let photo = null
            if ( elemPhoto ) {
              photo = getComputedStyle( elemPhoto ).backgroundImage
              photo = photo.replace('url("', '').replaceAll('")', '')
            }

            if ( name && name != '') { bodies.name = name }
            if ( price && price != '') { bodies.price = price }
            if ( weight && weight != '') { bodies.weight = weight }
            if ( description && description != '') { bodies.description = description }
            if ( category && category != '') { bodies.category = category }
            if ( photo && photo != '') { bodies.photo = photo }
            bodies.popular = document.getElementById('popular').checked
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/food/${this.number}`, {
              method: "POST",
              mode: "cors",
              body: JSON.stringify(bodies),
              headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            // window.location.href = "/admin/food/" + this.number
            this.init()
            document.getElementById('foodEditClosed').click()
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
          async getData(number) {
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/food/${number}`, {
              method: "GET",
              mode: "cors",
              headers: {
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            return jsonData
          },
          async getAllCategory() {
            
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/category`, {
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
              return `${date.getDate()}.${date.getMonth()}.${date.getYear() + 1900} ${date.getHours()}:${date.getMinutes()}`
          },
          openFood(number) {
            window.location.href = `/admin/food/${number}`
          },
          async deleteFood(number) {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/food/${number}`, {
              method: "DELETE",
              mode: "cors",
              headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies.get("token")}`
              },
            });
            const jsonData = await response.json();
            window.location.href = "/admin/foods"
          },
          async toggleRemovedFood(number) {
            const { cookies } = useCookies();
            const response = await fetch(`${baseURL}/api/food/${number}`, {
              method: "POST",
              mode: "cors",
              body: JSON.stringify({
                "active" : !this.active
              }),
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