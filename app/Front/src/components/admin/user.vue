<template>
    <a :href="'/admin/user/' + number" class="d-flex" id="user">
        <div class="img">
            <img v-if="this.photo" :src="this.photo">
            <img v-if="!this.photo" src="@/assets/image/user.jpg">
        </div>
        <div class="d-block">
            <p class="fw-bold">{{ name }}</p>
            <p class="fw-light">{{ mail }}</p>
        </div>
    </a>
</template>


<script>

  import baseURL from "@/config"
  import { useCookies } from "vue3-cookies";

  export default {
        data() {
            return { 
                name: '............',
                mail: '............',
                photo: null,
                number: null
            }
        },
        created() {
        },
        mounted() {
            this.getMe().then((data) => {
                this.name = data.name
                this.mail = data.email
                this.photo = data.photo
                this.number = data.number
            })
        },
        methods: {
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
    #user {
        text-decoration: none !important;
        color: black;
        background-color: transparent !important;
        border: 1px dashed gray;
        border-radius: 50px;
        padding: 0 20px 0 0;
        transition: .3s;
    }
    #user:hover {
        border: 1px solid gray;
    }
    #user > .img {
        position: relative;
        overflow:hidden;
        width:50px;
        height:50px;
        padding: 0;
    }
    #user > .img > img {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        border-radius: 50px;
        width: 40px;
        height: 40px;
        object-fit:cover;
    }
    #user > div {
        padding-top: 5px;
    }
    #user > div > p {
        margin-bottom: -10px;
    }
</style>