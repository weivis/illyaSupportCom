(function(t){function e(e){for(var o,r,u=e[0],c=e[1],s=e[2],l=0,d=[];l<u.length;l++)r=u[l],Object.prototype.hasOwnProperty.call(a,r)&&a[r]&&d.push(a[r][0]),a[r]=0;for(o in c)Object.prototype.hasOwnProperty.call(c,o)&&(t[o]=c[o]);h&&h(e);while(d.length)d.shift()();return i.push.apply(i,s||[]),n()}function n(){for(var t,e=0;e<i.length;e++){for(var n=i[e],o=!0,r=1;r<n.length;r++){var u=n[r];0!==a[u]&&(o=!1)}o&&(i.splice(e--,1),t=c(c.s=n[0]))}return t}var o={},r={app:0},a={app:0},i=[];function u(t){return c.p+"js/"+({}[t]||t)+"."+{"chunk-088abb0a":"a7552ab0","chunk-0c941996":"ebb9bd8d","chunk-1340336a":"7da7bcd3","chunk-1434b502":"7ee68014","chunk-16fe0070":"d2dd3446","chunk-179d3b34":"79a093cf","chunk-2d0e95df":"2e2df00c","chunk-3ea7c600":"e488b6ec","chunk-4cd28e7f":"bdcb58e4","chunk-4d48d843":"be1f0aa2","chunk-5ceed50d":"aa0779df","chunk-606ec7a6":"dc60a677","chunk-61f3a124":"8bbce84b","chunk-7d5300ce":"27d2ea06","chunk-8aa53f0a":"6889b7e4","chunk-8b521e18":"c87722f4","chunk-bedb1066":"c2b36202"}[t]+".js"}function c(e){if(o[e])return o[e].exports;var n=o[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,c),n.l=!0,n.exports}c.e=function(t){var e=[],n={"chunk-088abb0a":1,"chunk-0c941996":1,"chunk-1340336a":1,"chunk-1434b502":1,"chunk-16fe0070":1,"chunk-179d3b34":1,"chunk-3ea7c600":1,"chunk-4cd28e7f":1,"chunk-4d48d843":1,"chunk-5ceed50d":1,"chunk-606ec7a6":1,"chunk-61f3a124":1,"chunk-7d5300ce":1,"chunk-8aa53f0a":1,"chunk-8b521e18":1,"chunk-bedb1066":1};r[t]?e.push(r[t]):0!==r[t]&&n[t]&&e.push(r[t]=new Promise((function(e,n){for(var o="css/"+({}[t]||t)+"."+{"chunk-088abb0a":"6ce8845a","chunk-0c941996":"3fff44df","chunk-1340336a":"e78948cc","chunk-1434b502":"7e6faa38","chunk-16fe0070":"7ea55a77","chunk-179d3b34":"87b15b9c","chunk-2d0e95df":"31d6cfe0","chunk-3ea7c600":"bd233da6","chunk-4cd28e7f":"2f2f24bf","chunk-4d48d843":"ef897494","chunk-5ceed50d":"6269cc7a","chunk-606ec7a6":"df92fef2","chunk-61f3a124":"e1b9a7cc","chunk-7d5300ce":"65b3664d","chunk-8aa53f0a":"92a39597","chunk-8b521e18":"9031de7f","chunk-bedb1066":"8ef9a971"}[t]+".css",a=c.p+o,i=document.getElementsByTagName("link"),u=0;u<i.length;u++){var s=i[u],l=s.getAttribute("data-href")||s.getAttribute("href");if("stylesheet"===s.rel&&(l===o||l===a))return e()}var d=document.getElementsByTagName("style");for(u=0;u<d.length;u++){s=d[u],l=s.getAttribute("data-href");if(l===o||l===a)return e()}var h=document.createElement("link");h.rel="stylesheet",h.type="text/css",h.onload=e,h.onerror=function(e){var o=e&&e.target&&e.target.src||a,i=new Error("Loading CSS chunk "+t+" failed.\n("+o+")");i.code="CSS_CHUNK_LOAD_FAILED",i.request=o,delete r[t],h.parentNode.removeChild(h),n(i)},h.href=a;var f=document.getElementsByTagName("head")[0];f.appendChild(h)})).then((function(){r[t]=0})));var o=a[t];if(0!==o)if(o)e.push(o[2]);else{var i=new Promise((function(e,n){o=a[t]=[e,n]}));e.push(o[2]=i);var s,l=document.createElement("script");l.charset="utf-8",l.timeout=120,c.nc&&l.setAttribute("nonce",c.nc),l.src=u(t);var d=new Error;s=function(e){l.onerror=l.onload=null,clearTimeout(h);var n=a[t];if(0!==n){if(n){var o=e&&("load"===e.type?"missing":e.type),r=e&&e.target&&e.target.src;d.message="Loading chunk "+t+" failed.\n("+o+": "+r+")",d.name="ChunkLoadError",d.type=o,d.request=r,n[1](d)}a[t]=void 0}};var h=setTimeout((function(){s({type:"timeout",target:l})}),12e4);l.onerror=l.onload=s,document.head.appendChild(l)}return Promise.all(e)},c.m=t,c.c=o,c.d=function(t,e,n){c.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},c.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},c.t=function(t,e){if(1&e&&(t=c(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(c.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var o in t)c.d(n,o,function(e){return t[e]}.bind(null,o));return n},c.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return c.d(e,"a",e),e},c.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},c.p="/",c.oe=function(t){throw console.error(t),t};var s=window["webpackJsonp"]=window["webpackJsonp"]||[],l=s.push.bind(s);s.push=e,s=s.slice();for(var d=0;d<s.length;d++)e(s[d]);var h=l;i.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"034f":function(t,e,n){"use strict";var o=n("85ec"),r=n.n(o);r.a},"1be0":function(t,e,n){},"31d5":function(t,e,n){},4667:function(t,e,n){"use strict";var o=n("bf9b"),r=n.n(o);r.a},"56d7":function(t,e,n){"use strict";n.r(e);var o={};n.r(o),n.d(o,"getUserToken",(function(){return at})),n.d(o,"getUser",(function(){return it})),n.d(o,"setUser",(function(){return ut})),n.d(o,"removeUser",(function(){return ct}));var r={};n.r(r),n.d(r,"upload",(function(){return ht})),n.d(r,"AlbumList",(function(){return ft})),n.d(r,"AlbumInfo",(function(){return pt})),n.d(r,"AlbumDowurlList",(function(){return mt})),n.d(r,"AlbumDowurlFeedback",(function(){return bt})),n.d(r,"ArticleList",(function(){return vt})),n.d(r,"ArticleInfo",(function(){return gt})),n.d(r,"authLogin",(function(){return kt})),n.d(r,"authRegister",(function(){return wt})),n.d(r,"authRegisterAgainSendemail",(function(){return yt})),n.d(r,"authVerifyRegisterVcode",(function(){return Ct})),n.d(r,"authLogout",(function(){return _t})),n.d(r,"bangumiList",(function(){return jt})),n.d(r,"bangumiInfo",(function(){return St})),n.d(r,"getUserinfo",(function(){return Ot})),n.d(r,"userEditinfo",(function(){return It})),n.d(r,"userInfo",(function(){return $t})),n.d(r,"VideoList",(function(){return Ut})),n.d(r,"VideoQuery",(function(){return Lt})),n.d(r,"VideoUploadOrEdit",(function(){return Et})),n.d(r,"VideoDel",(function(){return At})),n.d(r,"PhotoList",(function(){return Pt})),n.d(r,"PhotoUp",(function(){return Tt})),n.d(r,"PhotoChange",(function(){return xt})),n.d(r,"getindex",(function(){return Wt}));n("e260"),n("e6cf"),n("cca6"),n("a79d");var a=n("2b0e"),i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("router-view",{key:t.$route.fullPath})],1)},u=[],c={name:"App",created:function(){var t=this.$authUser.getUserToken();t?console.log("用户已登录"):console.log("用户未登录")}},s=c,l=(n("034f"),n("2877")),d=Object(l["a"])(s,i,u,!1,null,null,null),h=d.exports,f=(n("d3b7"),n("8c4f")),p=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"main-container"},[n("layout-header"),n("layout-appmain"),n("layout-footer")],1)},m=[],b=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"layout-Header"},[n("div",{staticClass:"header"},[n("div",{staticClass:"Common page-width"},[n("div",{staticClass:"logo"},[n("router-link",{attrs:{to:"/"}},[n("div",{staticClass:"img"},[n("img",{staticStyle:{height:"100%"},attrs:{src:"https://illya-support.weivird.com/static/logo.png"}})]),n("div",{staticClass:"lines"}),n("div",{staticClass:"title"},[t._v(" China - Illya Aid com "),n("br"),t._v("中国地区応援サイト ")])])],1),t.navop?n("div",{staticClass:"nav"},t._l(t.list,(function(e,o){return n("div",{key:o,staticClass:"item"},[n("router-link",{staticClass:"title",attrs:{to:e.link}},[n("div",{staticClass:"jp"},[t._v(t._s(e.jptitle))]),n("span",{staticClass:"span"},[t._v("·")]),n("div",{staticClass:"cn"},[t._v(t._s(e.cntitle))]),n("i",{staticClass:"el-icon-arrow-down"})])],1)})),0):t._e(),t.navopbutton?n("div",{staticClass:"opennavbutton",on:{click:function(e){return t.oepnnav()}}},[n("i",{staticClass:"el-icon-s-fold"})]):t._e(),n("loginbar")],1)])])},v=[],g=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"Loginbar"},[t.user?n("div",{staticClass:"userbar"},[n("el-dropdown",[n("span",{staticClass:"el-dropdown-link"},[n("div",{staticClass:"head"},[n("el-image",{staticStyle:{width:"100%",height:"100%"},attrs:{src:t.user.userHead,fit:"cover"}})],1),n("div",{staticClass:"username"},[t._v(t._s(t.user.userName))]),n("i",{staticClass:"el-icon-arrow-down el-icon--right"})]),n("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[n("el-dropdown-item",{nativeOn:{click:function(e){return t.open_photos()}}},[t._v("我的相簿")]),n("el-dropdown-item",{nativeOn:{click:function(e){return t.open_contribute()}}},[t._v("我的投稿")]),n("el-dropdown-item",{nativeOn:{click:function(e){return t.Logout_users(e)}}},[t._v("退出登录")])],1)],1)],1):n("div",{staticClass:"login"},[n("router-link",{staticClass:"link",attrs:{to:t.loginurl}},[t._v("前往登录 | 注册")])],1)])},k=[],w={name:"Loginbar",data:function(){return{user:null,loginurl:"/auth/sgin-in"}},created:function(){var t=this.$authUser.getUser();console.log(t),this.user=t},methods:{open_photos:function(){this.$router.push({name:"userphotos"})},open_contribute:function(){this.$router.push({name:"usercontribute"})},Logout_users:function(){var t=this;this.$http.authLogout(this.user.userToken).then((function(e){console.log(e),200===e.code&&(t.$authUser.removeUser(),window.location.reload())})).catch((function(t){console.log("error",t)}))}}},y=w,C=(n("5974"),Object(l["a"])(y,g,k,!1,null,"2d18727b",null)),_=C.exports,j={name:"Header",components:{Loginbar:_},methods:{oepnnav:function(){0==this.navop?this.navop=!0:this.navop=!1}},data:function(){return{navop:!0,navopbutton:!1,screenWidth:document.body.clientWidth,list:[{jptitle:"どうじん",cntitle:"同人二次创作",link:"/doujin"},{jptitle:"公式情報",cntitle:"资讯",link:"/news"},{jptitle:"アニメ",cntitle:"动画",link:"/bangumi"},{jptitle:"アルバム",cntitle:"相簿",link:"/photo"},{jptitle:"",cntitle:"资源",link:"/album"}]}},created:function(){console.log("true"),document.body.clientWidth>850?(this.navop=!0,this.navopbutton=!1):(this.navop=!1,this.navopbutton=!0)},watch:{screenWidth:function(t){if(!this.timer){this.screenWidth=t,this.timer=!0;var e=this;setTimeout((function(){e.screenWidth<850?(e.navop=!1,e.navopbutton=!0):(e.navop=!0,e.navopbutton=!1),console.log(e.screenWidth),e.timer=!1}),400)}}},mounted:function(){var t=this;window.onresize=function(){return function(){window.screenWidth=document.body.clientWidth,t.screenWidth=window.screenWidth}()}}},S=j,O=(n("aa98"),Object(l["a"])(S,b,v,!1,null,"6972bede",null)),I=O.exports,$=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},U=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"layout-Footer footer"},[n("div",{staticClass:"Common page-width"},[n("div",[n("div",{staticClass:"li"},[n("span",{staticClass:"l"},[t._v("魔法少女☆伊莉雅同人应援网站")]),n("span",{staticClass:"l"},[t._v("本网站属于非盈利性质由伊莉雅爱好者建设 如有问题请联系442981412@qq.com")]),n("span",{staticClass:"r"},[t._v("© WeiVi(网站作者) 2014-2020")]),n("span",{staticClass:"r"},[t._v("粤ICP备20033641号-1")]),n("span",{staticClass:"r"},[t._v("开源地址https://github.com/weivis/illyaSupportCom")])])])])])}],L={name:"Footer",methods:{},components:{},created:function(){}},E=L,A=(n("634e"),Object(l["a"])(E,$,U,!1,null,"67777c1a",null)),P=A.exports,T=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("section",{staticClass:"app-main"},[n("transition",{attrs:{name:"fade-transform",mode:"out-in"}},[n("router-view",{key:t.key})],1)],1)},x=[],W=(n("b0c0"),{name:"AppMain",computed:{key:function(){return void 0!==this.$route.name?this.$route.name+ +new Date:this.$route+ +new Date}}}),M=W,D=(n("4667"),Object(l["a"])(M,T,x,!1,null,"fe7859f8",null)),H=D.exports,N={name:"Home",methods:{},components:{"layout-header":I,"layout-footer":P,"layout-appmain":H},created:function(){}},V=N,q=Object(l["a"])(V,p,m,!1,null,null,null),R=q.exports;a["default"].use(f["a"]);var F=[{path:"/404",component:function(){return n.e("chunk-2d0e95df").then(n.bind(null,"8cdb"))},hidden:!0},{path:"/",component:R,children:[{path:"/",name:"home",component:function(){return n.e("chunk-3ea7c600").then(n.bind(null,"bb51"))},meta:{title:"首页"}}]},{path:"/auth",component:R,children:[{path:"sgin-in",name:"login",component:function(){return n.e("chunk-5ceed50d").then(n.bind(null,"bd01"))},meta:{title:"登录"}},{path:"register",name:"register",component:function(){return n.e("chunk-16fe0070").then(n.bind(null,"6d75"))},meta:{title:"注册"}},{path:"verify",name:"verify",component:function(){return n.e("chunk-61f3a124").then(n.bind(null,"4793"))},meta:{title:"邮箱验证"}}]},{path:"/user",component:R,children:[{path:"contribute",name:"usercontribute",component:function(){return n.e("chunk-4cd28e7f").then(n.bind(null,"568b"))},meta:{title:"我的投稿"}},{path:"more-contribute",name:"morecontribute",component:function(){return n.e("chunk-1340336a").then(n.bind(null,"3a0e"))},meta:{title:"我的投稿"}},{path:"photos",name:"userphotos",component:function(){return n.e("chunk-1434b502").then(n.bind(null,"2c58"))},meta:{title:"我的相簿"}}]},{path:"/doujin",component:R,children:[{path:"/",name:"listdoujin",component:function(){return n.e("chunk-179d3b34").then(n.bind(null,"866e"))},meta:{title:"同人作品"}},{path:"info",name:"infodoujin",component:function(){return n.e("chunk-606ec7a6").then(n.bind(null,"5464"))},meta:{title:"详细信息"}}]},{path:"/bangumi",component:R,children:[{path:"/",name:"listbangumi",component:function(){return n.e("chunk-8aa53f0a").then(n.bind(null,"f839"))},meta:{title:"番剧"}},{path:"info",name:"infobangumi",component:function(){return n.e("chunk-4d48d843").then(n.bind(null,"b52a"))},meta:{title:"番剧详细信息"}}]},{path:"/album",component:R,children:[{path:"/",name:"listalbum",component:function(){return n.e("chunk-7d5300ce").then(n.bind(null,"dbea"))},meta:{title:"资源"}},{path:"info",name:"infoalbum",component:function(){return n.e("chunk-0c941996").then(n.bind(null,"6cb9"))},meta:{title:"资源详细信息"}}]},{path:"/news",component:R,children:[{path:"/",name:"listnews",component:function(){return n.e("chunk-bedb1066").then(n.bind(null,"7c64"))},meta:{title:"资源"}},{path:"item",name:"itemnews",component:function(){return n.e("chunk-088abb0a").then(n.bind(null,"224c"))},meta:{title:"资源详细信息"}}]},{path:"/photo",component:R,children:[{path:"/",name:"listphoto",component:function(){return n.e("chunk-8b521e18").then(n.bind(null,"4e4d"))},meta:{title:"相簿"}}]}],B=new f["a"]({mode:"history",routes:F}),z=B,J=n("2f62");a["default"].use(J["a"]);var K=new J["a"].Store({state:{},mutations:{},actions:{},modules:{}}),Q=n("5c96"),G=n.n(Q),X=n("f0d9"),Y=n.n(X),Z=n("bc3a"),tt=n.n(Z),et="illyaComUserToken",nt="illyaComUserName",ot="illyaComUserHead",rt="illyaComUserID";function at(){return window.localStorage.getItem(et)}function it(){return window.localStorage.getItem(et)?{userToken:window.localStorage.getItem(et),userID:window.localStorage.getItem(rt),userName:window.localStorage.getItem(nt),userHead:window.localStorage.getItem(ot)}:null}function ut(t,e,n,o){console.log("登录成功"),window.localStorage.setItem(et,t),window.localStorage.setItem(nt,n),window.localStorage.setItem(rt,e),window.localStorage.setItem(ot,o)}function ct(){console.log("退出登录"),window.localStorage.removeItem(et),window.localStorage.removeItem(nt),window.localStorage.removeItem(rt),window.localStorage.removeItem(ot),window.localStorage.clear()}var st="https://illya-support.weivird.com/api",lt=tt.a.create({baseURL:st,timeout:5e4});lt.interceptors.request.use((function(t){var e=at();return console.log("Authorization",e),e&&(t.headers["Token"]=e),t}),(function(t){console.log(t),Promise.reject(t)})),lt.interceptors.response.use((function(t){var e=t.data;return 200!==e.code&&Object(Q["Message"])({message:e.msg,type:"error",duration:5e3}),10086==e.code&&(Object(Q["Message"])({message:e.msg,type:"error",duration:5e3}),ct(),setTimeout((function(){z.go(0)}),1500)),e}),(function(t){return console.log("err"+t),Object(Q["Message"])({message:t.message,type:"error",duration:5e3}),Promise.reject(t)})),lt.httpRoot=st;var dt=lt;function ht(t){return dt({url:"/upload/",method:"post",data:t,headers:{"Content-Type":"multipart/form-data"}})}function ft(t,e,n){return dt({url:"/album/list",method:"post",data:{types:t,pages:e,sfilter:n}})}function pt(t){return dt({url:"/album/info",method:"post",data:{id:t}})}function mt(t){return dt({url:"/album/dowurl/list",method:"post",data:t||{}})}function bt(t){return dt({url:"/album/info",method:"post",data:{id:t}})}function vt(t){return dt({url:"/article/list",method:"post",data:t||{}})}function gt(t){return dt({url:"/article/info",method:"post",data:t||{}})}function kt(t,e){return dt({url:"/auth/sign-in",method:"post",data:{email:t,password:e}})}function wt(t,e,n,o){return dt({url:"/auth/register",method:"post",data:{email:t,password:e,repassword:n,username:o}})}function yt(t){return dt({url:"/auth/register/again-sendemail",method:"post",data:{email:t}})}function Ct(t){return dt({url:"/auth/verify/register-vcode",method:"post",data:{vcode:t}})}function _t(){return dt({url:"/auth/logout",method:"post",data:{}})}function jt(t,e,n){return dt({url:"/bangumi/list",method:"post",data:{types:t,pages:e,sfilter:n}})}function St(t){return dt({url:"/bangumi/info",method:"post",data:{id:t}})}function Ot(t){return dt({url:"/user/get/userinfo",method:"post",data:{id:t}})}function It(t,e,n){return dt({url:"/user/edit-myinfo",method:"post",data:{head:t,username:e,introduce:n}})}function $t(){return dt({url:"/user/myinfo",method:"post",data:{}})}function Ut(t){return dt({url:"/video/list",method:"post",data:t||{}})}function Lt(t){return dt({url:"/video/query",method:"post",data:t||{}})}function Et(t){return dt({url:"/video/uploadoredit",method:"post",data:t||{}})}function At(t){return dt({url:"/video/user/del",method:"post",data:t||{}})}function Pt(t){return dt({url:"/photo/list",method:"post",data:t||{}})}function Tt(t){return dt({url:"/photo/up",method:"post",data:t||{}})}function xt(t){return dt({url:"/photo/change",method:"post",data:t||{}})}function Wt(t){return dt({url:"/open/index",method:"post",data:t||{}})}z.beforeEach((function(t,e,n){t.meta.title&&(document.title=t.meta.title+" - 魔法少女☆伊莉雅同人爱好者网站 - 中国地区応援サイト"),n()}));n("1be0"),n("6db3"),n("0fae");a["default"].use(G.a,{locale:Y.a}),a["default"].config.productionTip=!1,a["default"].prototype.$http=r,a["default"].prototype.$authUser=o,a["default"].prototype.$ServerHttpUrl="https://illya-support.weivird.com",a["default"].prototype.$Message=Q["Message"],new a["default"]({el:"#app",router:z,store:K,render:function(t){return t(h)}}).$mount("#app");var Mt=f["a"].prototype.push;f["a"].prototype.push=function(t){return Mt.call(this,t).catch((function(t){return t}))}},5974:function(t,e,n){"use strict";var o=n("7c9b"),r=n.n(o);r.a},"634e":function(t,e,n){"use strict";var o=n("31d5"),r=n.n(o);r.a},"6db3":function(t,e,n){},"7c9b":function(t,e,n){},"85ec":function(t,e,n){},aa98:function(t,e,n){"use strict";var o=n("d14d"),r=n.n(o);r.a},bf9b:function(t,e,n){},d14d:function(t,e,n){}});
//# sourceMappingURL=app.14d83848.js.map