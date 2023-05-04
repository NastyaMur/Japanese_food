<template>
    <div class="footer">
        <div class="container">
            <div class="row">
                <div class="col-12 col-md-4">
                    <p class="p-0 mb-0">© Japanese Food, 2023</p>
                    <a href="/admin" class="text-decoration-none"><font-awesome-icon :icon="['fas', 'cog']" class="me-2" />Администрирование</a>
                </div>
                <div class="col-12 col-md-4">
                </div>
                <div class="col-12 col-md-4">
                    <div class="sign">
                        <h4 class="d-inline-block"><span class="fw-bolder">Developed by</span><br><span class="fw-lighter">Muravieva Anastasiya</span></h4>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.footer {
    margin-top: 80px;
}
.sign {
    text-align: right;
}
</style>

<script>
  export default {
    name: 'downBar'
  }
</script>