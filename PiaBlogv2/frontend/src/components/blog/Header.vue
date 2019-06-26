<template>
  <v-layout row wrap>
    <v-toolbar :color="white" :dark="false" flat>
      <v-flex xs12 >
        <v-text-field label="Search" single-line></v-text-field>
      </v-flex>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>search</v-icon>
      </v-btn>
    </v-toolbar>
  </v-layout>
</template>

<script>
  export default {
    data: () => ({

    })
  }
</script>