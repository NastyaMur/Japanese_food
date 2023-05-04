import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { library } from "@fortawesome/fontawesome-svg-core";
import { 
    faBars, 
    faPhone, 
    faCog, 
    faCartShopping, 
    faPen, 
    faTrash, 
    faUser,
    faCartArrowDown,
    faUtensils,
    faLayerGroup,
    faHandSparkles,
    faPlus,
    faLock,
    faBoxArchive,
    faRightFromBracket,
    faPlay,
    faDolly,
    faSquare,
    faCheck,
    faHouse
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(
    faBars,
    faCog,
    faCartShopping,
    faTrash,
    faPen,
    faUser,
    faCartArrowDown,
    faUtensils,
    faLayerGroup,
    faHandSparkles,
    faPlus,
    faLock,
    faBoxArchive,
    faRightFromBracket,
    faPlay,
    faDolly,
    faSquare,
    faCheck,
    faHouse
);

import './assets/main.css'
import 'popper.js/dist/popper.min.js';
import 'bootstrap/dist/js/bootstrap.min.js'
import 'bootstrap/dist/css/bootstrap.min.css'
  
const app = createApp(App)

app.use(router)
app.component("font-awesome-icon", FontAwesomeIcon)
app.mount('#app')
