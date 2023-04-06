<script setup>
    import navbar from '@/components/client/navbar.vue'
    import menuTopItem from '@/components/client/menuTopItem.vue'
    import downBar from '@/components/client/footer.vue'
</script>

<template>
    <navbar />

    <div class="view">
      <div class="container p-4">
        <h3 class="fw-bolder">{{this.categoryCode}}</h3>
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

<script>

    export default {
        data() {
            return { 
                data: {},
                category: null
            }
        },
        created() {
            let path = this.$route.path
            this.categoryCode = path.substring(path.lastIndexOf('/') + 1, path.length)
        },
        // mounted() {
        // },
        // methods: {
        //     async getData(age) {
        //         const response = await fetch(`${baseURL}/photoAlbum/${age}`)
        //         const data = await response.json()

        //         console.log(data)
        //         this.data = data
        //     }
        // }
    }
</script>