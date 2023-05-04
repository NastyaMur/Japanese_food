import { createRouter, createWebHistory } from 'vue-router'
import baseURL from '@/config.js';
import { useCookies } from "vue3-cookies";

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
      path: '/cart',
      name: 'Корзина',
      component: () => import('../views/client/cart.vue')
    },

    {
      path: '/login',
      name: 'Авторизация',
      component: () => import('../views/client/login.vue')
    },
    {
      path: '/registration',
      name: 'Регистрация',
      component: () => import('../views/client/reg.vue')
    },


    {
      path: '/admin',
      name: 'Панель администратора',
      component: () => import('../views/admin/dashboard.vue')
    },
    {
      path: '/admin/user/:number',
      name: 'Пользователь',
      component: () => import('../views/admin/userPage.vue')
    },
    {
      path: '/admin/users',
      name: 'Пользователи',
      component: () => import('../views/admin/users.vue')
    },
    {
      path: '/admin/foods',
      name: 'Товары',
      component: () => import('../views/admin/foods.vue')
    },
    {
      path: '/admin/food/:number',
      name: 'Товар',
      component: () => import('../views/admin/foodItem.vue')
    },
    {
      path: '/admin/orders',
      name: 'Заказы',
      component: () => import('../views/admin/orders.vue')
    },
    {
      path: '/admin/order/:number',
      name: 'Заказ',
      component: () => import('../views/admin/orderItem.vue')
    },
    {
      path: '/admin/categories',
      name: 'Категории',
      component: () => import('../views/admin/categories.vue')
    },
    {
      path: '/admin/roles',
      name: 'Роли',
      component: () => import('../views/admin/roles.vue')
    }
  ]
})

router.beforeEach(async (to) => {
  const { cookies } = useCookies();
  const adminPage = [
    'Роли', 'Категории', 'Заказ', 'Заказы', 'Товар', 'Товары', 'Пользователи', 'Пользователь', 'Панель администратора'
  ];
  const authRequired = adminPage.includes(to.name);

  if ( authRequired ) {
    if (cookies.get("token")) {
      const settings = {
          method: 'GET',
          headers: {
              'Authorization': 'Bearer ' + cookies.get("token"),
          }
      };
      const response = await fetch(`${baseURL}/api/user/me`, settings)
      const statusCode = await response.status
      const data = await response.json();

      if ( statusCode == 200 ) {
        if ( !data.roles.includes("admin") ) {
          return '/';
        }
      } else {
        return '/login';
      }
    } else {
      return '/login';
    }
  }
});

export default router
