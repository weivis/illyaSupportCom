import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/zh-CN' // lang i18n

import * as api from './api'
import * as auth from './utils/auth'
import '@/permission' // permission control
import '@/styles/common.scss' // global css

Vue.use(ElementUI, { locale })
Vue.config.productionTip = false
Vue.prototype.$http = api
Vue.prototype.$authUser = auth

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
}).$mount('#app')
