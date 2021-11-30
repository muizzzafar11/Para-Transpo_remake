<template>
    <div id="Home">
    <TabNav :tabs="['Home', 'Settings']" :selected="selected" @selected="setSelected" >
      <Tab :isSelected="selected === 'Home'" >
        <p style="font-size: 30px; margin-top: 25px; font-weight: bold;">Booking trip for <b style="color: red"> {{ today }}</b></p>
        <BookRide />
      </Tab>
      <Tab :isSelected="selected === 'Settings'" >
        <Login msg=""/>
      </Tab>
    </TabNav>
  </div>
</template>

<script>
import TabNav from './components/TabNav.vue';
import Tab from './components/Tab.vue';
import Login from './components/LoginForm.vue';
import BookRide from './components/BookRide.vue';

export default {
  name: 'Home',
  components: { TabNav, Tab, Login, BookRide},
  data() {
    return {
      selected: 'Home',
      today: new Date(new Date().getTime() + 24 * 60 * 60 * 1000).toLocaleDateString(),
    }
  },
  methods: {
    setSelected(tab) {
      this.selected = tab;
    },
  },
}
</script>

<style>
#Home {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 20px; */
}
</style>