<template>
  <div>
    <CommonContentNav
      :conttype.sync="contentType"
      @conttype="getList()"
      button_style="0"
      :buttlist="buttlist"
      :rnav="rnav"
      background_color="#ffffff"
    />
    <div class="Common page-width content">
      <div v-for="(item, index) in list" :key="index" class="item">
        <div class="cover">
          <el-link :href="'/doujin/info?id=' + item.id" target="_blank">
          <el-image style="width:100%;height:100%;display:block;" :src="item.cover" fit="cover"></el-image>
          </el-link>
        </div>
        <div class="info">
          <div class="content">
            <div class="buttonli">
              <el-link :href="'/user/more-contribute?id=' + item.id" target="_blank" style="margin-right: 15px"><el-button>编辑</el-button></el-link>
              <el-button @click="delvideo(item.id)">删除稿件</el-button>
            </div>
            <div class="title">
              <span class="span"><el-link :href="'/doujin/info?id=' + item.id" target="_blank" class="span" :underline="false" style="font-size: 18px;">{{item.title}}</el-link></span>
              <div class="tag">
                <span v-if="item.verify_type === 1">审核通过</span>
                <span v-if="item.verify_type === 2">等待审核中</span>
                <span v-if="item.verify_type === 3">审核不合格退回</span>
                <span v-if="item.verify_type === 4">被管理员删除</span>
              </div>
            </div>
            <div class="more">

              <span class="span">
                VID: 
                {{item.id}}
              </span>

              <span class="span">
                <span v-if="item.classification === 1">MAD·AMV</span>
                <span v-if="item.classification === 2">MMD</span>
                <span v-if="item.classification === 3">技术宅</span>
                <span v-if="item.classification === 4">其他</span>
              </span>

              <span class="span">
                作品类型:
                <span v-if="item.original_type === 1">原创</span>
                <span v-if="item.original_type === 2">转载</span>
              </span>

              <span class="span">
                投稿时间: 
                {{item.create_time}}
              </span>

            </div>
          </div>
        </div>
      </div>
    </div>
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
  name: "contribute",
  data() {
    return {
      buttlist: [
        { title: "全部", conttype: 0 },
        { title: "已审核通过", conttype: 1 },
        { title: "等待审核", conttype: 2 },
        { title: "审核不合格退回", conttype: 3 }
      ],
      rnav: [{ title: "+ 投稿新作品", routername: "morecontribute" }],
      contentType: 0, // 当前选中内容分类
      currentPage: 1, // 当前页码
      totalItem: 0, // 总条目
      totalPage: 0, // 总页数
      pageSize: 10, // 每页多少条
      list: [],
      user: {}
    };
  },
  components: {
    CommonContentNav,
    Pagination
  },
  methods: {
    delvideo(id){
      this.$http
        .VideoDel({
          id:id
        })
        .then(response => {
          if (response.code == 200) {
            this.$Message({
              message: '删除成功',
              duration: 5 * 1000
            })
            this.getList();
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    getList() {
      this.$http
        .VideoList({
          types: 0,
          pages: this.currentPage,
          sfilter: this.contentType,
          userid: this.user.userID
        })
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
  created() {
    this.user = this.$authUser.getUser();
    this.getList();
  }
};
</script>
<style lang="scss" scoped>
.item {
  display: flow-root;
  width: 100%;
  border: 1px solid #cecece;
  margin-bottom: 25px;
  border-radius: 5px;
  .cover {
    float: left;
    width: 250px;
  }
  .info {
    float: right;
    width: calc(100% - 250px);
    .content {
      position: relative;
      padding: 20px;
      .buttonli{
        height: 30px;position: absolute;right: 50px;top: 0;bottom: 0;margin: auto;
      }
    }
    .title {
      margin-top: 20px;
      display: flow-root;
      width: 100%;
      font-size: 18px;
      .span {
        float: left;
      }
      .tag {
        margin-left: 15px;
        font-size: 14px;
        border: 1px solid #dadada;
        border-radius: 20px;
        line-height: 23px;
        height: 23px;
        padding-left: 10px;
        padding-right: 10px;
        float: left;
      }
    }
    .more {
      font-size: 14px;
      margin-top: 30px;
      display: flow-root;
      width: 100%;
      height: 20px;
      line-height: 20px;
      .span {
        float: left;
        margin-right: 25px;
      }
    }
  }
}
</style>