import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

/* Layout */
import Layout from '../layout/Layout'

const routes = [
  { path: '/404', component: () => import('@/views/404'), hidden: true },
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
        meta: {title:'首页'}
      },
      {
        path: '/album',
        name: 'album',
        component: () => import('@/views/album/'),
        meta: {title:'资源'}
      },
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login/')
  }
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
