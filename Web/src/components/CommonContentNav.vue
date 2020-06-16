<template>
  <div class="Components-CommonContentNav">
      
      <div class="CommonContentNav AllWidth">
          <div class="CommonContentNav ContentWidth Common page-width">
              111
          </div>
      </div>

  </div>
</template>

<script>
export default {
  name: 'CommonContentNav',
  props: {
    background_color: String,
    button_color: String,
    button_style: Intl,
    buttlist: Array
  },
  created(){
      console.log(this.buttlist)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .CommonContentNav.AllWidth{width: 100%;}
    .CommonContentNav.ContentWidth{}
</style>