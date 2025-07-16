// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: false },

  modules: [
    '@nuxt/eslint',
    '@nuxt/ui-pro',
    '@nuxt/icon',
    '@nuxt/image',
    '@pinia/nuxt',
    'pinia-plugin-persistedstate/nuxt',
  ],

  css: ['~/assets/css/main.css'],

  runtimeConfig: {
    public: {
      apiUrl:
        process.env.NODE_ENV === 'production'
          ? 'https://findyourgame-api.docsystem.xyz'
          : 'http://localhost:8080',
    },
  }
})