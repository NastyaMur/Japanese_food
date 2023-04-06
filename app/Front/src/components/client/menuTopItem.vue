<script setup>
</script>

<template>
    <div class="item-bloc col-6 col-md-4 col-lg-3">
        <div class="item">
            <div class="image">
                <img src="https://cdn.farfor.ru/media/cache/94/02/9402a24e73f71e4fc784a4567d09ca28.jpg" class="w-100">
            </div>
            
            <h5 class="fw-bold">Филадельфия</h5>
            <p class="text-muted fw-light">Лосось, огурец, сыр сливочный.</p>
            <h5 class="fw-bolder">130 ₽</h5>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'menuTopItem'
  }
</script>

<style scoped>
.item-bloc {
    padding: 10px;
}
.item {
    padding: 20px;
    border-radius: 14px;
    transition: .3s;
    background-color: white;
}
.image {
    padding: 20px;
}
.item:hover {
    cursor: pointer;
    transform: scale(1.04);
    /* background-color: rgb(238, 238, 238); */
}
</style>