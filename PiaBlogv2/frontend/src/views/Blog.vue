<template>
  <div>
    <v-container>
      <Header></Header>
      <v-spacer></v-spacer>
      <PostGrid></PostGrid>
    </v-container>
  </div>
</template>

<script>

import Header from '../components/blog/Header'
import PostGrid from '../components/blog/PostGrid'

export default {

  components:{
    Header,
    PostGrid,
  }
}
</script>