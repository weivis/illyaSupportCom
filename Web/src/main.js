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
import '@/styles/el-important.scss' // global css
import 'element-ui/lib/theme-chalk/index.css'
// import '@/styles/transition.scss'

Vue.use(ElementUI, { locale })
Vue.config.productionTip = false
Vue.prototype.$http = api
Vue.prototype.$authUser = auth
Vue.prototype.$ServerHttpUrl = 'https://illya-support.weivird.com'
Vue.prototype.$Message = Message

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
}).$mount('#app')

import Router from 'vue-router'
const routerPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return routerPush.call(this, location).catch(error=> error)
}