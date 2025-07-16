<script setup lang="ts">
const rating = ref(0)
const comment = ref('')

const props = defineProps<{
  gameId: number
}>()

const { gameId } = toRefs(props)

const emit = defineEmits<{ close: [boolean] }>()

const userStore = useUserStore()
const userId = userStore.user?.id_utilisateur

async function submitReview() {
  if (rating.value < 0 || rating.value > 10) {
    return
  }
  if (comment.value.length === 0) {
    return
  }
  // Call the API to submit the review
  if (userId !== undefined) {
    await addReview(userId, gameId.value, rating.value, comment.value)
  }
  emit('close', true)
}
</script>

<template>
  <UModal
    title="Évaluation"
    :close="{ onClick: () => emit('close', false) }">
    <!-- Modal content -->
    <template #body>
      <div class="flex flex-col items-center">
        <p class="text-sm text-gray-500 mb-4">Votre avis est important pour nous !</p>
        <UInputNumber
          v-model="rating"
          :min="0"
          :max="10"
          :icon="['i-lucide-star', 'i-lucide-star-2']"
          class="mb-4"
        />
        <UInput
          v-model="comment"
          type="textarea"
          placeholder="Laissez un commentaire..."
          class="w-full max-w-md"
        />
        <UButton
          label="Envoyer"
          class="mt-4"
          @click="submitReview"
        />
      </div>
    </template>
  </UModal>
</template>

<style scoped>

</style>