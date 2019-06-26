<template>
    <div id="BlogPost">
        <v-parallax dark v-bind:src="post.image">
            <v-layout align-center column justify-center>
                <h1 class="display-2 font-weight-thin mb-3">{{post.title}}</h1>
                <h4 class="subheading">Build your application today!</h4>
            </v-layout>
        </v-parallax>
        <v-container>
            {{post.content}}
        </v-container>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                info: null,
                id: this.$route.params.id,
                post: {}
            }
        },
        mounted() {

        },
        created() {
            axios.get('http://192.168.1.20:8000/api/posts/' + this.id + '/?format=json')
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.post = response.data
                    console.log(post)
                    // console.log(blog)
                })
                .catch(e => {
                    this.errors.push(e)
                })
        },
    }
</script>