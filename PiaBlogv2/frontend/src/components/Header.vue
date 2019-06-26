<template>
  <v-toolbar>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title><v-btn to="/" flat>Home</v-btn></v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat to="/blog">Blog</v-btn>
      <v-btn flat to="/about">About</v-btn>
      <v-btn flat to="/profile">Profile</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>


<script>
export default {

}
</script>

<style >

</style>