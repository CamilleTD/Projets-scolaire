import { defineStore } from 'pinia'
import type { UserInfo } from '~/composables/types'

export const useUserStore = defineStore('user', {
  state: () => {
    return {
      isLoggedIn: false,
      user: null,
    } as {
      isLoggedIn: boolean | null
      user: UserInfo | null
    }
  },
  persist: true,
  actions: {
    async login(email: string, password: string) {
      const user = await fetch(`${useRuntimeConfig().public.apiUrl}/auth/login`, {
        method: 'POST',
        body: JSON.stringify({
          email,
          password,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      }).then((res) => res.json())
      if (user.error) {
        this.setIsLoggedIn(false)
        this.setUser(null)
        return user
      }
      this.setIsLoggedIn(true)
      this.setUser(user)
      return user
    },
    logout() {
      this.setIsLoggedIn(false)
      this.setUser(null)
    },
    setIsLoggedIn(isLoggedIn: boolean) {
      this.isLoggedIn = isLoggedIn
    },
    setUser(user: UserInfo | null) {
      this.user = user
    },
  }
})
