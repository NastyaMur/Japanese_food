<script setup>
    
</script>

<template>
    <nav id="navbar" class="navbar navbar-expand-lg fixed-top navbar-dark">
        <div class="container">
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
                        <ul class="navbar-nav justify-content-end flex-grow-1 text-center">
                            <li class="nav-item">
                                <router-link class="nav-link" to="/category/bonus">Акции</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/category/cold">Холодные роллы</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/category/premium">Премиум роллы</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/category/hot">Запеченные роллы</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/category/sets">Сеты</router-link>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="offcanvas offcanvas-end" tabindex="-1" >
                <h1>fvdf</h1>
            </div>
        </div>
    </nav>
</template>

<script>
  export default {
    name: 'navbar'
  }
</script>

<style scoped>

.offcanvas.offcanvas-start {
    /* -webkit-backdrop-filter: saturate(180%) blur(20px);
    backdrop-filter: saturate(180%) blur(20px); */
    right: auto !important;
    background-color: rgba(22, 22, 23, .7) !important;
    color: #fff !important;
    border-radius: 26px !important;
    margin: 15px;
}
.navbar::after {
    z-index: 0;
    position: absolute;
    content: '';
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    /* -webkit-backdrop-filter: saturate(180%) blur(20px);
    backdrop-filter: saturate(180%) blur(20px);
    background-color: rgba(255, 255, 255, 0.7); */
}
.navbar, .navbar > .container {
    z-index: 10000;
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
        background-color: rgba(22, 22, 23, .7) !important;
        color: #fff !important;
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

</style>