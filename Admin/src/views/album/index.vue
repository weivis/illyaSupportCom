<template>
  <div class="album">
    <CommonContentNav :conttype.sync="contentType" @conttype="getList(contentType, currentPage)" button_style="0" :buttlist='buttlist'/>
    <Pagination :total="totalItem" :page.sync="currentPage" @pagination="getList(contentType, currentPage)" :limit.sync="pageSize"/>
  </div>
</template>

<script>
import CommonContentNav from '@/components/CommonContentNav.vue'
import Pagination from '@/components/Pagination.vue'
export default {
  name: 'album',
  data(){
    return{
      buttlist:[
        { title:'全部', conttype:0 },
        { title:'番剧', conttype:1 },
        { title:'OST', conttype:2 },
        { title:'MMD', conttype:3 },
        { title:'Live2D', conttype:4 },
      ],
      contentType:0, // 当前选中内容分类
      currentPage: 3, // 当前页码
      totalItem: 1000, // 总条目
      totalPage: 100, // 总页数
      pageSize: 15 // 每页多少条
    }
  },
  components: {
    CommonContentNav, Pagination
  },
  methods: {
    getList(content_type, pages){
      console.log(content_type)
      console.log(pages)
      this.contentType = content_type
      this.currentPage = pages
    }
  }
}
</script>
