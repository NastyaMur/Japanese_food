import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { library } from "@fortawesome/fontawesome-svg-core";
import { faBars, faPhone } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { globalCookiesConfig } from "vue3-cookies";

library.add(faBars);

import './assets/main.css'
// import jQuery from 'jQuery'
import 'popper.js/dist/popper.min.js';
import 'bootstrap/dist/js/bootstrap.min.js'
import 'bootstrap/dist/css/bootstrap.min.css'

globalCookiesConfig({
    expireTimes: "1d",
    path: "/",
    domain: "",
    secure: true,
    sameSite: "None",
});
  
const app = createApp(App)

app.use(router)
app.component("font-awesome-icon", FontAwesomeIcon)
app.mount('#app')
