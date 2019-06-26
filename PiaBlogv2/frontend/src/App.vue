<template>
  <v-app>

    <Header></Header>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Header from './components/Header'

export default {
  name: 'App',
  components: {
    Header
  },
  data () {
    return {
      // info
    }
  }
}
</script>

<style >
  body{
    background-color: #f3f3f3;
    font-family: 'Rockwell', serif;
  }
</style>
