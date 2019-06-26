<template>
  <div class="main" @load='showPosts'>
    <!-- <v-container grid-list-md text-xs-center>
      <v-layout row wrap>

        <v-flex xs6 v-bind:id="i + '1'">
          <v-card dark color="primary" height="300">
          </v-card>
        </v-flex>

        <v-flex xs6 v-bind:id="i + '2'">
          <v-card dark color="dark" height="300">
          </v-card>
        </v-flex>

        <v-flex xs4 v-bind:id="i + '3'">
          <v-card dark color="deep-purple darken-4" height="300">
          </v-card>
          <v-flex d-flex v-bind:id="i + '4'">
            <v-card color="orange" dark height="600">
            </v-card>
          </v-flex>
        </v-flex>

        <v-flex d-flex xs12 sm6 md4 v-bind:id="i + '5'">

          <v-layout column>
            <v-card color="purple" dark height="600">
            </v-card>
            <v-flex xs4 v-bind:id="i + '6'">
              <v-card dark color="deep-purple darken-4" height="300">
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>

        <v-flex xs4 v-bind:id="i + '7'">
          <v-card dark color="deep-purple darken-4" height="300">
          </v-card>
          <v-flex d-flex v-bind:id="i + '8'">
            <v-card color="orange" dark height="600">
            </v-card>
          </v-flex>
        </v-flex>

      </v-layout>
    </v-container> -->
    <v-container>
      <v-layout row wrap>
        <v-flex {{size}} v-for="(card, size) in cards">
          <v-card v-if="card === 1" dark color="primary" height="300">
          </v-card>

          <v-card v-if="card === 2" dark color="dark" height="300">
          </v-card>

          <v-card v-if="card === 3" dark color="deep-purple darken-4" height="300">
          </v-card>
          <v-flex v-if="card === 34" d-flex v-bind:id="i + '4'">
            <v-card color="orange" dark height="600">
            </v-card>
          </v-flex>

        </v-flex>
      </v-layout>
      {{cards}}
    </v-container>

  </div>
</template>

<script>
  // import axios from 'axios'

  export default {
    data() {
      return {
        cards: this.getCards(20),
      }
    },
    methods: {
      getCards: function (posts) {
        var cards = new ActiveXObject("Scripting.Dictionary");
        for (var i = 0; i < posts; i++) {
          // if (i % 8 == 0) {
          //   cards.push(0);
          // }
          if (i % 8 === 1) {
            cards.add(1, "xs6");
          } else if (i % 8 === 2) {
            cards.add(2, "xs6");
          } else if (i % 8 === 3) {
            if (i + 1 % 8 === 4) {
              cards.add(34, "xs4");
            } else {
              cards.add(3, "xs4");
            }
          } else if (i % 8 === 5) {
            if (i + 1 % 8 === 6) {
              cards.add(56, "xs12");
            } else {
              cards.add(5, "xs12");
            }
          } else if (i % 8 === 7) {
            if (i + 1 % 8 === 8) {
              cards.add(78, "xs4");
            } else {
              cards.add(7, "xs4");
            }
          }
        }
        return cards
      },
    },
  }
</script>