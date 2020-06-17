<template>
  <div>
    <div class="leftbox">
      <el-row>
        <el-col class="common rwoh">
          <el-upload
            class="content"
            drag
            action
            :http-request="upLoad"
            :show-file-list="false"
            multiple
          >
            <img :src="loadcover" style="width:100%" />
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">
              将文件拖到此处，或
              <em>点击上传</em>
            </div>
            <!-- <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div> -->
          </el-upload>
          {{cover}}
        </el-col>
        <el-row class="common rwoh">
          <el-button>番剧ID: {{id}}</el-button>
          <el-button>系统唯一ID: {{identification}}</el-button>
        </el-row>
        <el-col>
          <el-row class="common rwoh">
            <el-input placeholder="请输入内容" v-model="name">
              <template slot="prepend">番剧名</template>
            </el-input>
          </el-row>

          <el-row class="common rwoh" style="line-height: 2.5;">
            <el-col :span="5" class="common elmr">
              <el-input placeholder="请输入剧集数" v-model="setscount">
                <template slot="prepend">剧集数</template>
              </el-input>
            </el-col>

            <el-col :span="6" class="common elmr">
                开播时间
              <el-date-picker
                v-model="openplay_time"
                type="date"
                placeholder="开播时间"
                format="yyyy 年 MM 月 dd 日"
                value-format="yyyy-MM-dd"
              ></el-date-picker>
            </el-col>

            <el-col :span="10" class="common elmr">
              <span class>连载状态</span>
              <el-select v-model="upstatus" placeholder="请选择">
                <el-option label="连载中" :value="true"></el-option>
                <el-option label="已完结" :value="false"></el-option>
              </el-select>
            </el-col>
          </el-row>

        <el-row class="common rwoh">
        <el-col class="common elmr" style="float:left; width:300px">
        <el-radio-group v-model="classification">
            <el-radio-button label="1">番剧</el-radio-button>
            <el-radio-button label="2">剧场版</el-radio-button>
            <el-radio-button label="3">OVA</el-radio-button>
            <el-radio-button label="4">SP</el-radio-button>
        </el-radio-group>
        </el-col>

        <el-col class="common elmr"  style="float:left; width:500px">
            <span class>是否允许站内播放</span>
            <el-select v-model="station_play" placeholder="请选择">
            <el-option label="允许" :value="true"></el-option>
            <el-option label="不开放" :value="false"></el-option>
            </el-select>
        </el-col>

        </el-row>
        </el-col>
      </el-row>
      <div class="line"></div>
      <el-row class="common rwoh">
        番剧介绍
        <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="introduce"></el-input>
      </el-row>
      <el-row class="common rwoh">
        STAFF
        <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="staff"></el-input>
      </el-row>
      <div class="line"></div>
      <el-row class="common rwoh">
        <el-table :data="cv_list" style="width: 100%">
          <el-table-column prop label="CV头像" width="150">
            <template slot-scope="scope">
              <el-image style="width: 90%; height: auto" :src="scope.row.head"></el-image>
            </template>
          </el-table-column>
          <el-table-column prop="id" label="ID" width="180"></el-table-column>
          <el-table-column prop="role_name" label="角色名" width="180"></el-table-column>
          <el-table-column prop="cv_id" label="CVID" width="180"></el-table-column>
          <el-table-column prop="sort" label="权重" width="180"></el-table-column>
          <el-table-column prop="people_name" label="CV名" width="180"></el-table-column>
          <el-table-column prop="head" label="CV名" width="180"></el-table-column>
        </el-table>
      </el-row>
      <div class="line"></div>
      <el-row>
        <el-table :data="playurl_tablist" style="width: 100%">
          <el-table-column prop="date" label="日期" width="180"></el-table-column>
          <el-table-column prop="name" label="姓名" width="180"></el-table-column>
          <el-table-column prop="address" label="地址"></el-table-column>
        </el-table>
      </el-row>
    </div>
    <div class="reightbox">
      <el-row class="funcbuttonrow">
        <div v-if="status === 1">番剧状态: 正常</div>

        <div v-if="status === 2">番剧状态: 已下架</div>
      </el-row>

      <el-row class="funcbuttonrow">
        <el-button @click="save()">保存</el-button>
      </el-row>
      <el-row class="funcbuttonrow">
        <el-button>添加CV</el-button>
      </el-row>
      <el-row class="funcbuttonrow">
        <el-button>添加播放地址</el-button>
      </el-row>
      <el-row class="funcbuttonrow">
        <el-button>上架</el-button>
      </el-row>
      <el-row class="funcbuttonrow">
        <el-button>下架</el-button>
      </el-row>
    </div>
  </div>
</template>
<script>
export default {
  name: "editbangumi",
  data() {
    return {
      id: "",
      name: "",
      classification: "",
      identification: "",
      setscount: "",
      introduce: "",
      cover: "",
      loadcover: "",
      upstatus: "",
      staff: "",
      station_play: "",
      openplay_time: "",
      sort: "",
      status: "",
      playurl_tablist: [],
      cv_list: []
    };
  },
  created() {
    this.query(this.$route.query.id);
  },
  methods: {
    query(id) {
      this.$http
        .bangumiInfo(id)
        .then(response => {
          if (response.code == 200) {
            this.id = response.data.result.id;
            this.name = response.data.result.name;
            this.classification = response.data.result.classification;
            this.identification = response.data.result.identification;
            this.setscount = response.data.result.setscount;
            this.introduce = response.data.result.introduce;
            this.loadcover = response.data.result.cover;
            this.upstatus = response.data.result.upstatus;
            this.staff = response.data.result.staff;
            this.station_play = response.data.result.station_play;
            this.openplay_time = response.data.result.openplay_time;
            this.sort = response.data.result.sort;
            this.status = response.data.result.status;
            this.cover = response.data.result.sourcecover;
            this.playurl_tablist = response.data.playsource;
            this.cv_list = response.data.cv;
            console.log();
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    upLoad(file) {
      const formData = new FormData();
      formData.append("file", file.file);
      formData.append("uploadKey", "bangumicover");

      console.log(file);
      this.$http.upload(formData).then(res => {
        console.log(res);
        console.log("上传成功");
        if (res.code === 200) {
          // console.log('res.data:',res.data)
          this.cover = res.data.filename;
          this.loadcover = res.data.lodpath;
        }
      });
    },
    change(id, types) {
      this.$http
        .bangumiChange(id, types, 0)
        .then(response => {
          if (response.code == 200) {
            this.getList(this.types, this.currentPage);
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    save() {
      let data = {
          id: this.id,
          classification: this.classification,
          openplay_time: this.openplay_time,
          name: this.name,
          setscount: this.setscount,
          introduce: this.introduce,
          cover: this.cover,
          upstatus: this.upstatus,
          staff: this.staff,
          station_play: this.station_play,
          status: this.status,
          sort: this.sort
      };
      this.$http
        .bangumiAddOrEdit(data)
        .then(response => {
          if (response.code == 200) {
            this.query(this.id);
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.leftbox {
  width: calc(100% - 230px);
  position: relative;
}
.reightbox {
  width: 180px;
  border-left: 1px solid #409eff;
  height: 100%;
  position: fixed;
  right: 20px;
  top: 90px;
  padding-left: 20px;
}
.funcbuttonrow {
  margin-bottom: 15px;
}
</style>