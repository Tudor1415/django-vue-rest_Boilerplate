<template>
  <div>
    <DrawLogo></DrawLogo>
  </div>
</template>

<script>
  import DrawLogo from '../components/home/DrawLogo'
  import Parallax from '../components/home/Parallax'
  import Timeline from '../components/home/Timeline'
  // import Parallax from '../components/home/Parallax'

  export default {
    name: 'Home',
    components: {
      DrawLogo,
      Parallax,
      Timeline,

    },
    data () {
      return {
        // info
      }
    }
  }
</script>

