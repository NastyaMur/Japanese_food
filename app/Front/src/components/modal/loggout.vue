<template>
    <div class="modal fade" id="loggout" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Внимание!</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <p>Вы уверены что хотите выйти из аккаунта?</p>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Отменить</button>
            <button type="button" class="btn btn-danger" v-on:click="loggout()">Выйти</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script>

  import { useCookies } from "vue3-cookies";

  export default {
        mounted() {
        },
        methods: {
          async loggout() {
            const { cookies } = useCookies();
            cookies.remove("token", null)
            window.location.href = `/`
          }
        }
    }
</script>