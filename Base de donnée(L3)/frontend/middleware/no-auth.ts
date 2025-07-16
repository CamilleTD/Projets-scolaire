import { useUserStore } from '~/stores/user'

export default defineNuxtRouteMiddleware((_to, _from) => {
  const userStore = useUserStore()

  if (userStore.isLoggedIn) {
    return navigateTo('/')
  }
})
