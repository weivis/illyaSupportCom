<template>
  <div>
    <CommonContentNav
      :conttype.sync="contentType"
      @conttype="getList()"
      button_style="0"
      :buttlist="buttlist"
    />
    {{currentPage}}
    <Pagination
      :total="totalItem"
      :page.sync="currentPage"
      @pagination="getList()"
      :limit.sync="pageSize"
    />
  </div>
</template>

<script>
import CommonContentNav from "@/components/CommonContentNav.vue";
import Pagination from "@/components/Pagination.vue";
export default {
  name: "index",
  data() {
    return {
      buttlist: [
        { title: "全部", conttype: 0 },
        { title: "番剧", conttype: 1 },
        { title: "剧场版", conttype: 2 },
        { title: "OVA", conttype: 3 },
        { title: "SP", conttype: 4 }
      ],
      contentType: 0, // 当前选中内容分类
      currentPage: 1, // 当前页码
      totalItem: 0, // 总条目
      totalPage: 0, // 总页数
      pageSize: 10, // 每页多少条
      list: []
    };
  },
  components: {
    CommonContentNav,
    Pagination
  },
  methods: {
    getList() {
      this.$http
        .bangumiList(this.contentType, this.currentPage, 0)
        .then(response => {
          if (response.code == 200) {
            this.list = response.data.result;
            this.currentPage = response.data.page;
            this.totalPage = response.data.pages;
            this.totalItem = response.data.count;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  },
  created(){
      this.getList()
  }
};
</script>