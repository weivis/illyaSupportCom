import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/zh-CN' // lang i18n
import { Message } from 'element-ui'

import * as api from './api'
import * as auth from './utils/auth'
import '@/permission' // permission control
import '@/styles/common.scss' // global css
import '@/styles/layout.scss' // global css
import '@/styles/el-important.scss' // global css
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI, { locale })
Vue.config.productionTip = false
Vue.prototype.$http = api
Vue.prototype.$authUser = auth
Vue.prototype.$ServerHttpUrl = 'http://127.0.0.1:8888/'
Vue.prototype.$Message = Message

// // auth.removeUserToken()

// Vue.config.publicPath = './'
Vue.config.publicPath = '/front'

const whiteList = ['/login','/404'] // 不重定向白名单
router.beforeEach((to, from, next) => {
    let user = auth.getUserToken()
    console.log('Token',user)
    if (user) {
      if (!user) {
        if (to.path === '/login') {
          next({ path: '/' })
        } else {
          if (JSON.stringify(to.query || {}) == '{}') {
            next({path: to.path})
          } else {
            next({path: to.path,query: to.query})
          }
        }
      } else {
        if (to.path === '/login') {
          next({ path: '/' })
        } else {
          next()
        }
      }
  
    } else {
      if (whiteList.indexOf(to.path) !== -1) {
        next()
      } else {
        next(`/login`) // 否则全部重定向到登录页
      }
    }
  })

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
}).$mount('#app')
