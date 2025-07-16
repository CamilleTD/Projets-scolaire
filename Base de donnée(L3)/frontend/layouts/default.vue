<script setup lang="ts">
const userStore = useUserStore()

const items = computed(() => {
  const L = [
    {
      label: 'Accueil',
      to: '/',
    },
    {
      label: 'Mes locations',
      to: '/locations',
    },
  ]
  if (userStore.user?.role === 'Administrateur') {
    L.push({
      label: 'Administration',
      to: '/admin',
    })
  }
  return L
})
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