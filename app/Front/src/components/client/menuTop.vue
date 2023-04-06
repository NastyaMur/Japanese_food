<script setup>
    import menuTopItem from './menuTopItem.vue';
    import menuTopItemSale from './menuTopItemSale.vue'
</script>

<template>
    <div class="container p-4">
        <h2 class="fw-bolder">🔥 Горячо!</h2>
        <div class="row">
            <menuTopItemSale/>
            <menuTopItem/>
            <menuTopItem/>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'menuTop'
  }
</script>

<style scoped></style>