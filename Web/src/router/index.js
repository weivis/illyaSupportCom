import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

/* Layout */
import Layout from '../layout/Layout'

const routes = [
  { path: '/404', component: () => import('@/views/404'), hidden: true },
  {
    path: '/',
    name: 'Home',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
        meta: {title:'首页'}
      }
    ]
  },
  {
    path: '/bangumi',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'listbangumi',
        component: () => import('@/views/bangumi/index.vue'),
        meta: {title:'番剧'}
      },
      {
        path: 'info',
        name: 'listbangumi',
        component: () => import('@/views/bangumi/info.vue'),
        meta: {title:'番剧详细信息'}
      },
    ]
  },
  {
    path: '/album',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'listalbum',
        component: () => import('@/views/album/index.vue'),
        meta: {title:'资源'}
      },
      {
        path: 'info',
        name: 'infoalbum',
        component: () => import('@/views/album/info.vue'),
        meta: {title:'资源详细信息'}
      }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
