<template>
    <div>

      <el-row class="common rwoh">
        <el-radio-group v-model="types" class="common elmr">
          <el-radio-button label="0">全部</el-radio-button>
          <el-radio-button label="1">番剧</el-radio-button>
          <el-radio-button label="2">剧场版</el-radio-button>
          <el-radio-button label="3">OVA</el-radio-button>
          <el-radio-button label="4">SP</el-radio-button>
        </el-radio-group>
        <el-radio-group v-model="sfilter" class="common elmr">
          <el-radio-button label="0">正常</el-radio-button>
          <el-radio-button label="1">全部</el-radio-button>
        </el-radio-group>
        <el-button type="primary" class="common elmr" @click="getList(types, 1)">查询</el-button>
      </el-row>
      <el-row class="common rwoh">
        <template>
            <el-table
              :data="tableData"
              style="width: 100%">

              <el-table-column
                prop=""
                label="图片"
                width="150">
                <template slot-scope="scope">
                    <el-image style="width: 90%; height: auto" :src="scope.row.cover">
                    </el-image>
                </template>
              </el-table-column>

              <el-table-column
                prop="id"
                label="id"
                width="50">
              </el-table-column>

              <el-table-column label="类型" width="100">
                <template slot-scope="scope">
                  <span v-if="scope.row.classification == 1">番剧</span>
                  <span v-if="scope.row.classification == 2">剧场版</span>
                  <span v-if="scope.row.classification == 3">OVA</span>
                  <span v-if="scope.row.classification == 4">SP</span>
                </template>
              </el-table-column>

              <el-table-column
                prop="name"
                label="番剧名"
                width="400"
                >
              </el-table-column>

              <el-table-column
                prop="sort"
                label="权重"
                width="50">
              </el-table-column>

              <el-table-column label="上下架状态" width="100">
                <template slot-scope="scope">
                  <span v-if="scope.row.status == 1">正常</span>
                  <span v-if="scope.row.status == 2">下架</span>
                </template>
              </el-table-column>

              <el-table-column label="连载状态" width="100">
                <template slot-scope="scope">
                  <span v-if="scope.row.upstatus == 1">连载中</span>
                  <span v-if="scope.row.upstatus == 0">以完结</span>
                </template>
              </el-table-column>

              <el-table-column
                prop="setscount"
                label="集数"
                width="">
              </el-table-column>

              <el-table-column label="更多" width="200">
                <template slot-scope="scope">
                  <a :href="'edit?id=' + scope.row.id" target="_blank" style="margin-right: 15px;"><el-button size="mini">详情</el-button></a>
                  <el-button size="mini" @click="change(scope.row.id,2)" v-if="scope.row.status == 1" type="success">下架</el-button>
                  <el-button size="mini" @click="change(scope.row.id,1)" v-if="scope.row.status == 2" type="info">上架</el-button>
                </template>
              </el-table-column>

            </el-table>
          </template>
      </el-row>

      <el-row class="common rwoh">
        <Pagination :total="totalItem" :page.sync="currentPage" @pagination="getList(types, currentPage)" :limit.sync="pageSize"/>
      </el-row>

      </div>
</template>

<script>
import Pagination from '@/components/Pagination.vue'
export default {
  name: 'listbangumi',
  data() {
    return {
      types: 0,
      sfilter: 0,
      currentPage: 1, // 当前页码
      totalItem: 0, // 总条目
      totalPage: 0, // 总页数
      pageSize: 10, // 每页多少条
      tableData: []
    }
  },
  methods: {
    change(id,types){
      this.$http.bangumiChange(id, types, 0)
      .then(response => {
        if (response.code == 200){
          this.getList(this.types, this.currentPage)
        }
      })
      .catch(error => {
        console.log("error", error);
      });
    },
    getList(types, currentPage){
      this.$http.bangumiList(types, currentPage, this.sfilter)
      .then(response => {
        if (response.code == 200){
          this.tableData = response.data.result
          this.currentPage = response.data.page
          this.totalPage = response.data.pages
          this.totalItem = response.data.count
          this.types = types
        }
      })
      .catch(error => {
        console.log("error", error);
      });
    }
  },
  components: {
    Pagination
  },
  created(){
    this.getList(0,0)
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
