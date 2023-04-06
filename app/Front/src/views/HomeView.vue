<script setup>
    import navbar from '@/components/client/navbar.vue'
    import menuTopItem from '@/components/client/menuTopItem.vue'
    import menuTopItemSale from '@/components/client/menuTopItemSale.vue'
    import downBar from '@/components/client/footer.vue'
</script>

<template>
    <navbar />

    <div class="view">
      <div class="container p-4">
        <h3 class="fw-bolder">🔥 Горячо!</h3>
        <p>Выгодная цена на любимые роллы, успей купить, пока акция еще не закончилась!</p>
        <div class="row">
            <menuTopItemSale/>
            <menuTopItem/>
            <menuTopItem/>
            <menuTopItem/>
            <menuTopItem/>
        </div>
      </div>

      <div class="container p-4">
        <h3 class="fw-bolder">Премиум роллы</h3>
        <div class="row">
            <menuTopItem/>
            <menuTopItem/>
            <menuTopItem/>
            <menuTopItem/>
        </div>
      </div>

      <div class="container p-4">
        <h3 class="fw-bolder">Сеты</h3>
        <div class="row">
            <menuTopItem/>
            <menuTopItem/>
            <menuTopItem/>
            <menuTopItem/>
        </div>
      </div>

    </div>

    <downBar />
</template>


<style scoped>
  .view {
    margin-top: 88px;
  }
</style>