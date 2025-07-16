<script setup lang="ts">
definePageMeta({
  name: 'Admin Panel',
  layout: 'admin',
})
</script>

<template>
  <UPageHero
    title="Panel d'administration"
    description="Gérez les utilisateurs et les jeux dans un seul endroit."
    :links="[
        {
          label: 'Utilisateurs',
          to: '/admin/users',
          color: 'info'
        },
        {
          label: 'Jeux',
          to: '/admin/games',
          color: 'info'
        }
    ]"
  />
</template>

<style scoped>

</style>