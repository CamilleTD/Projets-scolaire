<script setup lang="ts">
const props = defineProps<{
  game: Game
}>()

const { game } = toRefs(props)

const emit = defineEmits<{ close: [boolean] }>()
</script>

<template>
  <UModal
    :title="`Modifier ${game.nom}`"
    :close="{ onClick: () => emit('close', false) }">
    <!-- Modal content -->
    <template #body>
      <p>Non fonctionnel</p>
    </template>
  </UModal>
</template>

<style scoped>

</style>