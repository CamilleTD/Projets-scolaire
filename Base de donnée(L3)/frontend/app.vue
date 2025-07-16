<script setup lang="ts">
const route = useRoute()

const routeName = computed(() => route.name)

useHead({
  title: computed(() => {
    return `${routeName.value ? `${routeName.value} • FindYourGame` : 'FindYourGame'}`
  })
})
</script>
<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>

    <UOverlayProvider />
  </div>
</template>
