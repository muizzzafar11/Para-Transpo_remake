<template>
  <div class="login-page">
    <div class="form">
      <form class="login-form" @submit.prevent="login">
        <input id="email" type="email" name="email" placeholder="Email" v-model="email" />
        <input type="text" placeholder="Para Transpo Registration Number" v-model="regNum" />
        <input type="text" placeholder="First Name" v-model="firstName" />
        <input type="text" placeholder="Last Name" v-model="lastName" />
        <input type="text" placeholder="Phone Number" v-model="phoneNum" />
        <button type="submit" @click="onSubmit">{{loginButton}}</button>
        <!-- <p class="message">Not registered? <a href="#">Create an account</a></p> -->
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  props: {
    msg: String
  },
  data() {
    return {
      email: localStorage.getItem('email') ? localStorage.getItem('email') : '',
      regNum: localStorage.getItem('regNum') ? localStorage.getItem('regNum') : '',
      firstName: localStorage.getItem('firstName') ? localStorage.getItem('firstName') : '',
      lastName: localStorage.getItem('lastName') ? localStorage.getItem('lastName') : '',
      phoneNum: localStorage.getItem('phoneNum') ? localStorage.getItem('phoneNum') : '',
      loginButton: localStorage.getItem('email') ? 'Update' : 'Login',
    }
  },
  methods: {
    onSubmit() {
      localStorage.setItem('email', this.email)
      localStorage.setItem('regNum', this.regNum)
      localStorage.setItem('firstName', this.firstName)
      localStorage.setItem('lastName', this.lastName)
      localStorage.setItem('phoneNum', this.phoneNum)
      window.location.reload()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login-page {
  width: 100%;
  padding: 8% 0 0;
  margin: auto;
  font-size: 25px;
}
.form {
  width: 100%;
  position: relative;
  z-index: 1;
  background: #FFFFFF;
  max-width: 60vw;
  margin: 0 auto 100px;
  padding: 45px;
  text-align: center;
  border-radius: 20px;
  border: 3px solid #f1f1f1;
}
.form input {
  border-radius: 30px;
  font-family: "Roboto", sans-serif;
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  font-size: 14px;
}
.form button {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #4b4b4b;
  width: 50%;
  border-radius: 30px;
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 14px;
  margin-top: 20px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
}
.form button:hover,.form button:active,.form button:focus {
  background: #000000;
}
.form .message {
  margin: 15px 0 0;
  color: #b3b3b3;
  font-size: 12px;
}
.form .message a {
  color: #4CAF50;
  text-decoration: none;
}
.form .register-form {
  display: none;
}
.container {
  position: relative;
  z-index: 1;
  max-width: 300px;
  margin: 0 auto;
}
.container:before, .container:after {
  content: "";
  display: block;
  clear: both;
}
.container .info {
  margin: 50px auto;
  text-align: center;
}
.container .info h1 {
  margin: 0 0 15px;
  padding: 0;
  font-size: 36px;
  font-weight: 300;
  color: #1a1a1a;
}
.container .info span {
  color: #4d4d4d;
  font-size: 12px;
}
.container .info span a {
  color: #000000;
  text-decoration: none;
}
.container .info span .fa {
  color: #EF3B3A;
}
body {
  background: #76b852; /* fallback for old browsers */
  background: -webkit-linear-gradient(right, #76b852, #8DC26F);
  background: -moz-linear-gradient(right, #76b852, #8DC26F);
  background: -o-linear-gradient(right, #76b852, #8DC26F);
  background: linear-gradient(to left, #76b852, #8DC26F);
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;      
}
a {
  color: #42b983;
}
</style>
