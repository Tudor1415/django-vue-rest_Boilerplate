<template>
    <div>
        <createEditor></createEditor>
        <markdownHelp></markdownHelp>
        <!-- <fileUpload></fileUpload> -->
    </div>
</template>

<script>
import createEditor from '../components/blog/createEditor'
import markdownHelp from '../components/blog/markdownHelp'
// import fileUpload from '../components/blog/fileUpload'

export default {
    components:{
        createEditor,
        markdownHelp,
        // fileUpload,
    }
}
</script>