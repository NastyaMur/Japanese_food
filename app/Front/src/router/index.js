import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Главная',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/bonus',
      name: 'Акции',
      component: () => import('../views/client/category.vue')
    },
    {
      path: '/category/:category',
      name: 'Роллы',
      component: () => import('@/views/client/category.vue')
    },  
    {
      path: '/hot',
      name: 'Горячие роллы',
      component: () => import('../views/client/category.vue')
    },
    {
      path: '/cold',
      name: 'Холодные роллы',
      component: () => import('../views/client/category.vue')
    },
    {
      path: '/premium',
      name: 'Премиум роллы',
      component: () => import('../views/client/category.vue')
    },
    {
      path: '/sets',
      name: 'Сеты',
      component: () => import('../views/client/category.vue')
    },

    {
      path: '/login',
      name: 'Авторизация',
      component: () => import('../views/client/login.vue')
    },


    {
      path: '/admin',
      name: 'Панель администратора',
      component: () => import('../views/admin/dashboard.vue')
    }
  ]
})

export default router
