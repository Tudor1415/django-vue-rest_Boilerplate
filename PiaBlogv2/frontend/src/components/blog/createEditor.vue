<template>
  <Editor v-model="text" />
</template>

<script>
import { Editor, Renderer, Toolbar } from 'vuetify-markdown-editor';

// CSS for Editor
import 'vuetify-markdown-editor/dist/vuetify-markdown-editor.css';

/* Editor is a Vue component
 * Renderer is the internal rendering function
 * Toolbar is a Vue component used for some WYSIWYG functions
 */

export default {
  components: {
    Editor
  },
  data() {
    return {
      text: ''
    };
  }
};
</script>