(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3ea7c600"],{5878:function(t,a,s){},b5db:function(t,a,s){"use strict";var i=s("5878"),e=s.n(i);e.a},bb51:function(t,a,s){"use strict";s.r(a);var i=function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",[s("div",{staticClass:"bill",style:t.bill},[s("a",{staticClass:"a",attrs:{href:"/bangumi/info?id=4",target:"_blank"}})]),s("div",{staticClass:"Common page-width content"},[s("div",{staticClass:"body-p"},[s("div",{staticClass:"body-l"},[s("div",{staticClass:"common-mp"},[t._m(0),s("div",{staticClass:"content"},t._l(t.moduledata_bangumi,(function(a,i){return s("div",{key:i},[s("el-link",{staticClass:"bangumiitem",attrs:{href:"/bangumi/info?id="+a.id,target:"_blank",underline:!1}},[s("div",{staticClass:"cover"},[s("img",{staticStyle:{width:"100%"},attrs:{src:a.cover}})]),s("div",{staticClass:"r"},[s("div",{staticClass:"title"},[t._v(" "+t._s(a.name)+" ")]),s("div",{staticClass:"info"},[s("div",{staticClass:"info"},[s("span",{staticClass:"mr"},[t._v(t._s(a.openplay_time)+"开播")]),s("span",{staticClass:"mr"},[t._v("全"+t._s(a.setscount)+"话")]),!0===a.upstatus?s("span",{staticClass:"mr"},[t._v("连载中")]):t._e(),!1===a.upstatus?s("span",{staticClass:"mr"},[t._v("已完结")]):t._e()])]),s("div",{staticClass:"button"},[t._v("立即观看")])])])],1)})),0)]),t._m(1),s("div",{staticClass:"common-mp"},[t._m(2),s("div",{staticClass:"content"},[s("el-row",{attrs:{gutter:20}},t._l(t.moduledata_madamv,(function(a,i){return s("el-col",{key:i+"madamv",staticClass:"madamvitem",attrs:{span:9,xs:12,lg:6}},[s("div",[s("el-link",{attrs:{href:"/doujin",target:"_blank",underline:!1}},[s("img",{staticStyle:{width:"100%"},attrs:{src:a.cover}}),s("div",{staticClass:"title"},[t._v(t._s(a.title))])])],1)])})),1)],1)])]),s("div",{staticClass:"body-r"},[s("div",{staticClass:"common-mp"},[t._m(3),s("div",{staticClass:"content"},t._l(t.moduledata_news,(function(a,i){return s("div",{key:i,staticClass:"newsitem"},[s("el-link",{attrs:{href:"/news/item?id="+a.id,target:"_blank",underline:!1}},[s("div",{staticClass:"l"},[s("div",{staticClass:"cover"},[s("el-image",{staticStyle:{width:"100%",height:"100%",display:"block"},attrs:{src:a.cover,fit:"cover"}})],1)]),s("div",{staticClass:"r"},[s("div",{staticClass:"title"},[t._v(t._s(a.title))])])])],1)})),0)]),s("div",{staticClass:"common-mp"},[t._m(4),s("div",{staticClass:"content"},[s("el-row",{attrs:{gutter:10}},t._l(t.moduledata_photo,(function(t,a){return s("el-col",{key:a+"photo",staticClass:"photoitem",attrs:{span:12}},[s("div",[s("el-link",{attrs:{href:"/photo",target:"_blank",underline:!1}},[s("img",{staticStyle:{width:"100%"},attrs:{src:t.cover}})])],1)])})),1)],1)])])])])])},e=[function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"li"},[s("span",{staticClass:"title"},[t._v("アニメ")]),s("div",{staticClass:"r-button"},[s("a",{attrs:{href:"/bangumi",target:"_blank"}},[t._v("更多")])])])},function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"common-mp"},[s("div",{staticClass:"li"},[s("span",{staticClass:"title"},[t._v("资源")]),s("div",{staticClass:"r-button"},[s("a",{attrs:{href:"/album",target:"_blank"}},[t._v("更多")])])]),s("div",{staticClass:"content"},[s("div",{staticClass:"album"},[s("a",{attrs:{href:"/album",target:"_blank"}},[s("div",{staticClass:"button"},[t._v("アニメ")])]),s("a",{attrs:{href:"/album",target:"_blank"}},[s("div",{staticClass:"button"},[t._v("OST")])]),s("a",{attrs:{href:"/album",target:"_blank"}},[s("div",{staticClass:"button"},[t._v("MMD Model")])]),s("a",{attrs:{href:"/album",target:"_blank"}},[s("div",{staticClass:"button"},[t._v("Live2D")])])])])])},function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"li"},[s("span",{staticClass:"title"},[t._v("MAD·AMV")]),s("div",{staticClass:"r-button"},[s("a",{attrs:{href:"/doujin",target:"_blank"}},[t._v("更多")])])])},function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"li"},[s("span",{staticClass:"title"},[t._v("公式情報")]),s("div",{staticClass:"r-button"},[s("a",{attrs:{href:"/news",target:"_blank"}},[t._v("更多")])])])},function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"li"},[s("span",{staticClass:"title"},[t._v("絵を描く")]),s("div",{staticClass:"r-button"},[s("a",{attrs:{href:"/photo",target:"_blank"}},[t._v("更多")])])])}],l={name:"Home",data:function(){return{bill:"background-image: url(https://illya-support.weivird.com/static/com/bill/1.jpg);",moduledata_madamv:[],moduledata_bangumi:[],moduledata_news:[],moduledata_photo:[]}},components:{},methods:{getindex:function(){var t=this;this.$http.getindex({}).then((function(a){200==a.code&&(console.log(a.data),t.moduledata_madamv=a.data.madamv,t.moduledata_bangumi=a.data.bangumi,t.moduledata_news=a.data.news,t.moduledata_photo=a.data.photo)})).catch((function(t){console.log("error",t)}))},getList:function(t){console.log(t)}},created:function(){this.getindex()}},n=l,c=(s("b5db"),s("2877")),r=Object(c["a"])(n,i,e,!1,null,"680f901e",null);a["default"]=r.exports}}]);
//# sourceMappingURL=chunk-3ea7c600.e488b6ec.js.map