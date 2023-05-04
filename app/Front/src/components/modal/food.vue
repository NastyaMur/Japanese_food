<template>
    <div class="modal fade" :id="'food-'+ this.number" tabindex="-1">
      <div class="modal-dialog shadow">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row h-100">
              <div class="col-12 col-md-7 text-center h-100">
                <img :src="this.photo" class="h-100">
              </div>
              <div class="col-12 col-md-5">
                <div class="d-flex h-100 flex-column">
                  <div class="mt-4">
                    <h4 class="fw-bold">{{this.name}}</h4>
                    <p class="text-muted">{{this.description}}</p>
                  </div>
                  <div class="footer mt-auto">
                    <div class="row w-100">
                      <div class="col-6">
                        <h4 class="fw-bold">{{this.price}} ₽</h4>
                        <p class="fw-bold">{{this.weight}} гр.</p>
                      </div>
                      <div class="col-6 text-end">
                        <button type="button" :id="'buy-' + this.number" class="btn btn-outline-success" v-on:click="addCart(this.number)">В корзину</button>
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

<script>

  import baseURL from "@/config"
  import { useCookies } from "vue3-cookies"

  export default {
    props: ['name','price','description', 'number', 'photo', 'weight'],
    setup() {
      const { cookies } = useCookies();
      return { cookies };
    },
    mounted() {
      this.init()
    },
    methods: {
      async init() {
        
      },
      async addCart(foodNumber) {
        const { cookies } = useCookies();
        let cart = JSON.parse(cookies.get("cart"))
        if (cart == null || cart == '') {
          cart = []
        }
        cart.push(foodNumber)
        this.cookies.set("cart", JSON.stringify(cart))
        
        document.getElementById('buy-' + foodNumber).innerHTML = 'Готово!'
        setTimeout(function() {
          document.getElementById('buy-' + foodNumber).innerHTML = 'В корзину!'
        }, 700);
      },
      async getCartData() {
        const { cookies } = useCookies();
      }
    }
  }
</script>

<style>
.modal-dialog {
  margin-top: 300px;
  max-height: 100% !important;
  max-width: 70% !important;
}
.modal-content,
.modal-body {
  height: 400px;
}
.modal-header {
  position: relative;
  z-index: 1000;
}
.modal-content,
.modal-footer,
.modal-header {
  border: none !important;
}
.modal-body {
  margin-top: -50px;
}
.modal-body > div > div > div:nth-of-type(2){
  padding-top: 50px;
}
</style>