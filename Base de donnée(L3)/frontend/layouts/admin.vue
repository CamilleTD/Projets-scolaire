<script setup lang="ts">
const items = [
  {
    label: 'Accueil',
    to: '/admin/',
  },
  {
    label: 'Utilisateurs',
    to: '/admin/users',
  },
  {
    label: 'Jeux',
    to: '/admin/games',
  }
]

const userStore = useUserStore()
</script>

<template>
  <div>
    <UHeader title="FindYourGame">
      <UNavigationMenu :items="items" />

      <template #right>
        <UButton
          v-if="userStore.isLoggedIn"
          color="neutral"
          variant="outline"
          icon="i-lucide-user"
          label="Mon compte"
          to="/account" />
        <UButton
          v-else
          color="neutral"
          variant="outline"
          icon="i-lucide-log-in"
          label="Se connecter"
          to="/login" />
      </template>
    </UHeader>
    <NuxtPage />
  </div>
</template>

<style scoped>

</style>