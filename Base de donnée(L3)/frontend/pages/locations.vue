<script setup lang="ts">
definePageMeta({
  name: 'Mes locations'
})

const userStore = useUserStore()
const user = computed(() => userStore.user?.id_utilisateur)

const games = ref<Game[]>([])

if (!user.value) {
  navigateTo('/login')
}
else {
  games.value = await getRentedGames(user.value)
}

const gameImages = ref<{ id: number, url: string }[]>([])

onMounted(() => {
  games.value.forEach(async (game) => {
    gameImages.value.push({id: game.id_jeu, url: await getGameImage(game.nom) })
  })
})
</script>

<template>
  <UPageSection
    title="Locations en cours"
    description="Voici la liste de vos jeux en cours de location.">
  <div class="flex flex-col mt-6 items-center">
    <div class="grid grid-cols-5 gap-8">
      <ULink
        v-for="(game, index) in games"
        :key="index"
        :to="`/games/${game.id_jeu}`">
        <div class="flex flex-col items-center hover:opacity-80 transition-opacity duration-300">
          <img
            v-if="gameImages.find((img) => img.id === game.id_jeu)?.url"
            :src="gameImages.find((img) => img.id === game.id_jeu)?.url"
            :alt="game.nom"
            class="h-48 w-32 rounded-lg shadow-lg object-cover">
          <USkeleton
            v-else
            class="h-48 w-32" />
          <p class="text-xl font-bold text-center">{{ game.nom }}</p>
          <p class="text-sm text-center">Depuis le {{ new Date(game.date_location ?? "").toLocaleDateString() }}</p>
        </div>
      </ULink>
    </div>
  </div>
  </UPageSection>
</template>

<style scoped>

</style>