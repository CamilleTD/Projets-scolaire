<script setup lang="ts">
const props = defineProps<{
  gameId: number,
  rating: number,
  comment: string,
}>()

const { gameId, rating, comment } = toRefs(props)

const newRating = ref(rating.value)
const newComment = ref(comment.value)

const emit = defineEmits<{ close: [boolean] }>()

const userStore = useUserStore()
const userId = userStore.user?.id_utilisateur

async function submitReview() {
  if (newRating.value < 0 || newRating.value > 10) {
    return
  }
  if (newComment.value.length === 0) {
    return
  }
  // Call the API to submit the review
  if (userId !== undefined) {
    await updateReview(userId, gameId.value, newRating.value, newComment.value)
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
          v-model="newRating"
          :min="0"
          :max="10"
          :icon="['i-lucide-star', 'i-lucide-star-2']"
          class="mb-4"
        />
        <UInput
          v-model="newComment"
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