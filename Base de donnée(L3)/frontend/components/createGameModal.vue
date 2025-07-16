<script setup lang="ts">
const emit = defineEmits<{ close: [boolean] }>()

</script>

<template>
  <UModal
    title="Créer jeu"
    :close="{ onClick: () => emit('close', false) }">
    <!-- Modal content -->
    <template #body>
      <p>Non fonctionnel</p>
    </template>
  </UModal>
</template>

<style scoped>

</style>