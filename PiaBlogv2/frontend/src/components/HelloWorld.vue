
<template>
  <div class="hello">
    {{info[1].username}}
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      info :null
    }
  },
  mounted () {
    axios
      .get("http://192.168.1.20:8000/users/?format=json")
      .then(response => (this.info = response.data.results))
    // axios.get('http://192.168.1.20:8000/users/?format=json', {
    //     headers: {
    //     },
    //     auth: {
    //       username: 'tudor',
    //       password: 'test'
    //     },
    //   })
    //   .then(function (response) {
    //     this.info = response;
    //   })
    //   .catch(function (error) {
    //     console.log(error);
    //   });

  },
  filters: {

  }
}
</script>

<style scoped>
.select, select { /* 100% width for the select */
  width: 100%;
}

.card { /* Adding some air under the tasks */
  margin-bottom: 25px;
}

.done { /* Make the done tasks a little bit transparent */
  opacity: 0.3;
}
</style>