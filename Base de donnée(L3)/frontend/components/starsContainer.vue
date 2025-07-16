<script setup lang="ts">
const props = defineProps<{
  value: number
}>()

const { value } = toRefs(props)

const stars = computed(() => {
  const starsArray = []
  for (let i = 0; i < 5; i++) {
    if (i < value.value / 2) {
      starsArray.push('filled')
    } else {
      starsArray.push('empty')
    }
  }
  return starsArray
})

const filledStarPath = 'M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z'
const emptyStarPath = 'M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z'
const filledStarColor = '#FFD700'
const emptyStarColor = '#D3D3D3'
const filledStarSize = '24'
const emptyStarSize = '24'
const filledStarClass = 'h-6 w-6 text-yellow-500'
const emptyStarClass = 'h-6 w-6 text-gray-400'
</script>

<template>
  <div class="flex items-center">
    <svg
      v-for="(star, index) in stars"
      :key="index"
      :class="star === 'filled' ? filledStarClass : emptyStarClass"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
      :width="star === 'filled' ? filledStarSize : emptyStarSize"
      :height="star === 'filled' ? filledStarSize : emptyStarSize"
    >
      <path
        v-if="star === 'filled'"
        :d="filledStarPath"
        :fill="filledStarColor"
      />
      <path
        v-else
        :d="emptyStarPath"
        :fill="emptyStarColor"
      />
    </svg>
  </div>
</template>

<style scoped>

</style>