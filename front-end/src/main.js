import 'bootstrap/dist/css/bootstrap.min.css'
import { createApp } from 'vue'
import App from './App.vue'
import Home from './HomePage.vue'
import "vue-gifplayer/src/gif.css"

// check if the localc storage contains email
const email = localStorage.getItem('email');
if(!email) {
    createApp(App).mount('#app')
} else {
    createApp(Home).mount('#app')
}
