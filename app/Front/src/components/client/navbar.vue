<script setup>
    
</script>

<template>
    <nav id="navbar" class="navbar navbar-expand-lg bg-white fixed-top">
        <div class="bg"></div>
        <div class="container">
            <a class="navbar-brand" href="/">
                <h2>🍱 Japanese Food</h2>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
                <font-awesome-icon icon='bars' />
            </button>
            <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                <div class="popup">
                    <div class="offcanvas-header">
                        <div class="container d-flex justify-content-between">
                            <h5 class="offcanvas-title" id="offcanvasNavbarLabel">
                                🍱 Japanese Food
                            </h5>
                            <button type="button" class="btn-close mt-0" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                        </div>
                    </div>
                    <div class="offcanvas-body">
                        <ul class="navbar-nav justify-content-end flex-grow-1 p-3 text-center">
                            <li class="nav-item" v-for="item in items">
                                <router-link class="nav-link" :to="'/category/' + item.code">{{item.name}}</router-link>
                            </li>
                            <!-- <li class="nav-item ms-2" >
                                <router-link class="nav-link" to="/user">
                                    <div class="d-flex" id="user">
                                        <div class="img me-2">
                                            <img v-if="this.user.photo" :src="this.user.photo">
                                            <img v-if="!this.user.photo" src="@/assets/image/user.jpg">
                                        </div>
                                        <p class="fw-bold"><span class="text-muted">Привет,</span> {{ this.user.name }} 👋</p>
                                    </div>
                                </router-link>
                            </li> -->
                            <li class="nav-item ms-1" v-if="isAdmin">
                                <a class="nav-link" href="/admin">
                                    <font-awesome-icon :icon="['fas', 'cog']" class="me-2 text-primary" />
                                </a>
                            </li>
                            
                            <li class="nav-item ms-1" >
                                <router-link class="nav-link" style="color: rgb(214, 0, 212)" to="/cart">
                                    <font-awesome-icon :icon="['fas', 'cart-shopping']" style="color: rgb(214, 0, 212); margin-right: 10px;" />
                                    Корзина
                                    <!-- <span class="badge bg-success">0</span> -->
                                </router-link>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    import baseURL from "@/config"
    import { useCookies } from "vue3-cookies";

    export default {
        data() {
            return { 
                items: [],
                isAdmin: false
            }
        },
        created() { 
            this.getData().then((data) => {
                this.items = data
            })
            this.getMe().then((data) => {
                if (data.roles && data.roles.includes('admin')) {
                    this.isAdmin = true
                }
            })
        },
        methods: {
          async getData() {
            const response = await fetch(`${baseURL}/api/category`, {
              method: "GET",
              mode: "cors"
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
          }
        }
    }
</script>

<style scoped>
.navbar::after {
    z-index: 0;
    position: absolute;
    content: '';
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    -webkit-backdrop-filter: saturate(180%) blur(20px);
    backdrop-filter: saturate(180%) blur(20px);
    background-color: rgba(255, 255, 255, 0.7);
}
.navbar, .navbar > .container {
    z-index: 10000;
    background-color: transparent !important;
}

a.navbar-brand {
    background-color: transparent !important;
}

@media screen and (max-width: 992px) {
    
    .offcanvas-body > ul {
        font-size: 28px;
    }
    .popup {
        margin: 14px;
        background-color: white;
        border-radius: 14px;
    }

    .offcanvas.offcanvas-start {
        width: 100%;
        background-color: rgba(0, 0, 0, 0.036);
        -webkit-backdrop-filter: saturate(180%) blur(20px);
        backdrop-filter: saturate(180%) blur(20px);
    }
  }

.offcanvas-body > ul > li > a{
    border-radius: 7px;
}
#user {
    text-decoration: none !important;
    color: black;
    transition: .3s;
}
#user > .img {
    position: relative;
    overflow:hidden;
    width: 20px;
    height: 20px;
    padding: 0;
}
#user > .img > img {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50px;
    width: 30px;
    height: 30px;
    object-fit:cover;
}
#user > div {
    padding-top: 5px;
}
#user > div > p {
    margin-bottom: -10px;
}
</style>