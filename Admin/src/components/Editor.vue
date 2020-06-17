<template>
  <div id="editor">
    <vue-editor ref="editor" v-model="strHtml" :disabled='!!disabled' useCustomImageHandler  @image-added="handleImageAdded"></vue-editor>
  </div>
</template>
<script>
import { VueEditor } from "vue2-editor";
export default {
  name: "Editor",
  props: ["content", "disabled"],
  data() {
    return {
      strHtml: ""
    };
  },
  components: { VueEditor },
  watch: {
    $attrs(val) {
      this.strHtml = val.value;
    },
    strHtml(newval) {
      this.$emit("input", newval);
    }
  },
  methods: {
    handleImageAdded: function(file, Editor, cursorLocation, resetUploader) {
      var formData = new FormData()
      formData.append('file', file)
      formData.append("uploadKey", "articleimg");
      this.$http.upload(formData)
        .then(res => {
          let url = res.data.lodpath
          console.log(`${this.baseUrl}${url}`)
            Editor.insertEmbed(cursorLocation, 'image', `${url}`)
          resetUploader()
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
};
</script>