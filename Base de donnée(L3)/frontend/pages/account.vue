<script setup lang="ts">
definePageMeta({
  name: 'Mon compte'
})

const userStore = useUserStore()

function logout() {
  userStore.logout()
  navigateTo('/')
}
</script>

<template>
  <UContainer>
    <div class="flex flex-col items-center gap-2 mt-8">
      <p class="text-4xl font-bold mb-4">Mon compte</p>
      <UAvatar :alt="userStore.user?.nom" size="3xl" />
      <p class="text-2xl font-bold">{{ userStore.user?.nom }}</p>
      <UBadge v-if="userStore.user?.role === 'Administrateur'" label="Administrateur" color="error" />
      <UBadge v-else-if="userStore.user?.role === 'Membre'" label="Membre" color="info" />
      <p class="text-lg text-(--ui-mute) flex items-center gap-2"><UIcon name="i-lucide-mail" /><span>{{ userStore.user?.email }}</span></p>
      <USeparator class="my-4" />
      <UButton label="Se déconnecter" icon="i-lucide-log-out" color="error" @click="logout()" />
    </div>
  </UContainer>
</template>

<style scoped>

</style>