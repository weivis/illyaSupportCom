(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-4d48d843"],{"0bde":function(t,s,a){},b52a:function(t,s,a){"use strict";a.r(s);var i=function(){var t=this,s=t.$createElement,a=t._self._c||s;return a("div",[a("div",{staticClass:"top"},[a("div",{staticClass:"Common page-width content"},[a("div",{staticClass:"left"},[a("img",{staticStyle:{width:"100%"},attrs:{src:t.cover}})]),a("div",{staticClass:"right"},[a("div",{staticClass:"title"},[t._v(t._s(t.name))]),a("div",{staticClass:"info"},[a("span",{staticClass:"mr"},[t._v(t._s(t.openplay_time)+"开播")]),a("span",{staticClass:"mr"},[t._v("全"+t._s(t.setscount)+"话")]),!0===t.upstatus?a("span",{staticClass:"mr"},[t._v("连载中")]):t._e(),!1===t.upstatus?a("span",{staticClass:"mr"},[t._v("已完结")]):t._e()]),a("div",{staticClass:"introduce"},[t._v(t._s(t.introduce))])])]),a("div",{staticClass:"filterm"},[a("div",{staticClass:"filter",style:t.background})])]),a("div",{staticClass:"bottom Common page-width"},[a("div",{staticClass:"left-content"},[a("div",{staticClass:"page"},[a("div",{staticClass:"p-name"},[t._v("播放源")]),a("div",{staticClass:"p-content"},t._l(t.playsource_list,(function(s,i){return a("el-link",{key:i,attrs:{href:s.url,target:"_blank",underline:!1}},[a("div",{staticClass:"PlaySource-button"},[t._v(t._s(s.source_name))])])})),1)]),a("div",{staticClass:"line"}),a("div",{staticClass:"page"},[a("div",{staticClass:"p-name"},[t._v("CV")]),a("div",{staticClass:"p-content"},t._l(t.cv_list,(function(s,i){return a("div",{key:i,staticClass:"cv"},[a("div",{staticClass:"head"},[a("img",{staticStyle:{width:"100%"},attrs:{src:s.head}})]),a("div",{staticClass:"info"},[a("div",{staticClass:"name"},[t._v(t._s(s.people_name))]),a("div",{staticClass:"role"},[t._v(t._s(s.role_name))])])])})),0)]),a("div",{staticClass:"line"})]),a("div",{staticClass:"right-content"},[a("div",{staticClass:"page"},[a("div",{staticClass:"p-name"},[t._v("STAFF")]),a("div",{staticClass:"staff"},[t._v(t._s(t.staff))])])])])])},e=[],c=(a("b0c0"),{name:"info",data:function(){return{id:"",cover:"",classification:"",identification:"",introduce:"",name:"",openplay_time:"",setscount:"",sort:"",sourcecover:"",staff:"",station_play:"",upstatus:"",cv_list:[],playsource_list:[],background:""}},methods:{query:function(t){var s=this;this.$http.bangumiInfo(t).then((function(t){if(200==t.code){var a=t.data.result;s.id=a.id,s.cover=a.cover,s.classification=a.classification,s.identification=a.identification,s.introduce=a.introduce,s.name=a.name,s.openplay_time=a.openplay_time,s.setscount=a.setscount,s.sort=a.sort,s.sourcecover=a.sourcecover,s.staff=a.staff,s.station_play=a.station_play,s.upstatus=a.upstatus,s.cv_list=t.data.cv,s.playsource_list=t.data.playsource,s.background="background-image:url('"+a.cover+"')"}})).catch((function(t){console.log("error",t)}))}},components:{},created:function(){this.query(this.$route.query.id)}}),n=c,o=(a("b548"),a("2877")),l=Object(o["a"])(n,i,e,!1,null,"7a3613ce",null);s["default"]=l.exports},b548:function(t,s,a){"use strict";var i=a("0bde"),e=a.n(i);e.a}}]);
//# sourceMappingURL=chunk-4d48d843.be1f0aa2.js.map