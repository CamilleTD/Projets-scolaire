<script setup lang="ts">
definePageMeta({
  name: 'Accueil'
})

const searchedGames = ref({label: '', id: ''})

const gamesSearchResults = ref<{ label: string, categoriesString: string, mecaniqueString: string, id: number }[]>([])

async function searchGamesResults(term: string) {
  if (term.length < 2) {
    return
  }

  // complete to make request to server to search for games results
  const results = await searchGames(term)
  gamesSearchResults.value = results.map((game) => {
    return {
      label: game.nom,
      categoriesString: game.categories.join(', '),
      mecaniqueString: game.mecanique.join(', '),
      id: game.id_jeu
    }
  })
}

const recommendedGames = await getTopRatedGames()

const gameImages = ref<{ id: number, url: string }[]>([])

onMounted(() => {
  recommendedGames.forEach(async (game) => {
    gameImages.value.push({id: game.id_jeu, url: await getGameImage(game.nom) })
  })
})
</script>

<template>
  <UContainer>
    <div class="flex flex-col items-center">
      <UPageHero title="FindYourGame" />
      <UInputMenu
        v-model="searchedGames"
        type="search"
        placeholder="Rechercher un jeu... (nom, genre, mots-clés...)"
        icon="i-lucide-search"
        class="max-w-screen w-xs md:w-sm lg:w-md xl:w-lg"
        :items="gamesSearchResults"
        :filter-fields="['label', 'categoriesString', 'mecaniqueString']"
        @update:search-term="searchGamesResults"
        @change="() => searchedGames?.id ? navigateTo(`/games/${searchedGames.id}`) : null" />

      <UPageSection
          title="Jeux populaires">
        <div class="grid grid-cols-5 gap-8">
          <ULink
            v-for="(game, index) in recommendedGames"
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
            </div>
          </ULink>
        </div>
      </UPageSection>
    </div>
  </UContainer>
</template>

<style scoped>

</style>