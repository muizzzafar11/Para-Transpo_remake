<template>
<div>
  <ul class="nav nav-tabs nav-fill">
       <li v-for="tab in tabs" :key="tab" class="nav-item">
  <a class="nav-link" :class="{ active: tab === selected }" @click="setTab(tab)"
    >{{ tab }}</a>
</li>   
  </ul>
  <slot></slot>
</div>
</template>
<script>
export default {
  props: {
    /* Holds all of the tabs data */
    tabs: {
      type: Array,
      required: true,
    },
    selected: {
      type: String,
      required: true,
    }
  },
  methods: {
    setTab(tab) {
      this.$emit('selected', tab);
    },
  },
};
</script>
<style>
/* Styling for tabs */
.nav-tabs {
  border-bottom: 1px solid #ddd;
  cursor: pointer;
  height: 50px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 4px 4px 0 0;
  height: 50px;
  font-size: 25px;
}
.nav-tabs > li > a:hover {
  border-color: #eee #eee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555;
  cursor: default;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  margin-bottom: 5px;
  text-align: center;
}
</style>
