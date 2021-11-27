import 'bootstrap/dist/css/bootstrap.min.css'
import { createApp } from 'vue'
import App from './App.vue'
import Home from './HomePage.vue'

// check if the localc storage contains email
const email = localStorage.getItem('email');
if(!email) {
    createApp(App).mount('#app')
} else {
    createApp(Home).mount('#app')
}
