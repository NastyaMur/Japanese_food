<script setup>
</script>

<template>
    <div class="item-bloc col-6 col-md-4 col-lg-3">
        <div class="item">
            <div class="image">
                <img src="@/assets/image/roll1.png" class="w-100">
            </div>
            
            <h3 class="text-white fw-bold">Закажи свой любимый ролл со скидкой</h3>
            <p class="text-muted fw-light"></p>
            <h5 class="fw-bolder"></h5>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'menuTopItemSale'
  }
</script>

<style scoped>
.item-bloc {
    padding: 10px;
}
.item {
    overflow: hidden;
    padding: 35px;
    height: 100%;
    border-radius: 14px;
    transition: .3s;
    background-image: linear-gradient(218deg, rgba(255, 0, 252, 0.88), rgba(0, 198, 255, 0.91))
}
.image {
    width: 120%;
}
.item:hover {
    cursor: pointer;
    transform: scale(1.04);
    /* background-color: rgb(238, 238, 238); */
}
</style>