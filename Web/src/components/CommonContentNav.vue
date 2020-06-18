<!--
    import CommonContentNav from "@/components/CommonContentNav.vue";
    <CommonContentNav :conttype.sync="contentType" @conttype="getList(contentType, currentPage)" button_style="0" :buttlist='buttlist'/>
    buttlist:[
      { title:'全部', conttype:0 },
      { title:'番剧', conttype:1 },
      { title:'OST', conttype:2 },
      { title:'MMD', conttype:3 },
      { title:'Live2D', conttype:4 },
    ],
    contentType:0, // 当前选中内容分类
-->

<template>
  <div class="Components-CommonContentNav">
      <div class="CommonContentNav AllWidth" :style=componentsstyle>
          <div class="CommonContentNav ContentWidth Common page-width" v-if="button_style === '0'">
            <el-button v-for="(item,index) in buttlist" :style=buttonstyle :key="index + item" v-bind:class="{'button-active':index === i}"  class="CommonContentNav button" @click="conttypeChange(item.conttype, index)" round>{{item.title}}</el-button>
          </div>
          <div class="CommonContentNav ContentWidth Common page-width" v-if="button_style === '1'">
            <el-button v-for="(item,index) in buttlist" :style=buttonstyle :key="index + item" v-bind:class="{'button-active':index === i}"  class="CommonContentNav button" @click="conttypeChange(item.conttype, index)">{{item.title}}</el-button>
          </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'CommonContentNav',
  data(){
    return{
      conttypes: 0,
      i: 0,
      componentsstyle: 'background-color: ' + this.background_color + ';',
      buttonstyle: 'background-color: ' + this.button_background_color + ';'
    }
  },
  props: {
    background_color: {
      type: String,
      default: '#f4f4f4'
    },
    button_background_color: {
      type: String,
      default: ''
    },
    button_style: {
      type: String,
      default: '0'
    },
    buttlist:{
      type: Array,
      default (){
        return [{ title:'按钮', conttype:0 }]
      }
    },
    conttype:{
      type: Number,
      default:0
    },
  },
  methods: {
    conttypeChange(conttype, index) {
      this.i = index
      this.$emit("update:conttype", conttype)
      this.$emit('conttype', conttype)
    }
  },
  created(){
      console.log(this.buttlist)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .button-active{background-color:#0084ff; color: #fff}
    .CommonContentNav.AllWidth{width: 100%;}
    .CommonContentNav.ContentWidth{padding-top: 28px;padding-bottom: 28px;margin: 0 auto !important;}
    .CommonContentNav.button{margin-left: 0;margin-right: 25px;font-weight: bold;}
@media screen and (max-width: 1600px) {
}

@media screen and (max-width: 1200px) {
}

@media screen and (max-width: 600px) {
  .CommonContentNav.button{margin-right: 10px;}
}
</style>