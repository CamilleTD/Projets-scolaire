<script setup lang="ts">
import {LazyEditReviewModal, LazyReviewModal} from "#components";
import {checkGameStatus} from "~/composables/api";

definePageMeta({
  name: 'Jeu'
})

const gameId = parseInt(useRoute().params.game.toString())

const overlay = useOverlay()
const modal = overlay.create(LazyReviewModal, {
  props: {
    gameId: gameId,
  }
})

const userStore = useUserStore()
const user = computed(() => userStore.user?.id_utilisateur)
const isAdmin = computed(() => userStore.user?.role === 'Administrateur')

const game = ref<Game>(await getGameById(gameId))
const avis = ref<Evaluation[]>(await getReviewsByGameId(gameId))
const imageUrl = ref<string>()
const rentStatus = ref(await checkGameStatus(user.value || 0, gameId))

const disableReviewCreation = computed(() => {
  if (!user.value) {
    return true
  }
  if (avis.value.find(avisItem => avisItem.id_utilisateur === user.value)) {
    return true
  }
  return false
})

async function createNewReview() {
  const instance = modal.open()

  const result = await instance.result

  if (result) {
    game.value = await getGameById(gameId)
    avis.value = await getReviewsByGameId(gameId)
  }
}

async function callDeleteReview(userId: number, gameId: number) {
  await deleteReview(userId, gameId)
  avis.value = await getReviewsByGameId(gameId)
}

async function callEditReview(gameId: number, note: number, commentaire: string) {
  const editModal = overlay.create(LazyEditReviewModal, {
    props: {
      gameId: gameId,
      rating: note,
      comment: commentaire
    }
  })
  const instance = editModal.open()

  const result = await instance.result

  if (result) {
    game.value = await getGameById(gameId)
    avis.value = await getReviewsByGameId(gameId)
  }
}

async function startRent() {
  const result = await rentGame(user.value || 0, gameId)

  if (result) {
    rentStatus.value.status = 'rented'
    rentStatus.value.byMe = true
  }
}

async function returnRent() {
  const result = await returnGame(user.value || 0, gameId)

  if (result) {
    rentStatus.value.status = 'available'
    rentStatus.value.byMe = false
  }
}

onMounted(() => {
  getGameImage(game.value.nom).then(result => {
    imageUrl.value = result
  })
})
</script>

<template>
  <UContainer>
    <UAlert v-if="rentStatus.status === 'rented' && !rentStatus.byMe" color="info" variant="soft" class="mt-6">
      <template #title>
        Ce jeu est déjà loué par quelqu'un d'autre !<br>
        Vous ne pouvez pas l'emprunter actuellement.
      </template>
    </UAlert>
    <UAlert v-if="!user" color="info" variant="soft" class="mt-6">
      <template #title>
        Vous devez être connecté pour pouvoir laisser des commentaires ou louer un jeu !
      </template>
    </UAlert>
    <div class="flex gap-8 mt-8">
      <div class="h-96 w-64">
        <img
          v-if="imageUrl"
          :src="imageUrl"
          alt="Image du jeu"
          class="h-96 w-64 min-w-64 object-cover rounded-lg shadow-lg"
          @error="imageUrl = undefined"
        >
        <USkeleton v-else class="h-96 w-64" />
      </div>
      <div class="flex-1">
        <div class="flex items-center gap-2">
          <h1 class="text-4xl font-bold">{{ game.nom }}</h1>
          <StarsContainer :value="game.note_moyenne" />
          <p>({{ Math.round(game.note_moyenne) }}/10)</p>
        </div>
        <div class="flex items-center gap-2 mt-2">
          <UBadge v-for="(categorie, index) in game.categories" :key="index" color="info" variant="soft" :label="categorie" />
          <UBadge v-for="(mecanique, index) in game.mecanique" :key="index" color="info" variant="soft" :label="mecanique" />
          <UBadge v-if="game.annee_sortie" color="info" variant="soft" :label="game.annee_sortie" />
          <UBadge v-if="game.age_minimum" color="info" variant="soft" :label="game.age_minimum + '+ ans'" />
          <UBadge v-if="game.nombre_joueurs_min && game.nombre_joueurs_max" color="info" variant="soft" :label="game.nombre_joueurs_min + ' - ' + game.nombre_joueurs_max + ' joueurs'" />
          <UBadge v-else-if="game.nombre_joueurs_min" color="info" variant="soft" :label="game.nombre_joueurs_min + ' joueurs'" />
          <UBadge v-else-if="game.nombre_joueurs_max" color="info" variant="soft" :label="game.nombre_joueurs_max + ' joueurs'" />
          <UBadge v-if="game.duree_moyenne" color="info" variant="soft" :label="game.duree_moyenne + ' min'" />
          <UBadge v-if="game.editeur" color="info" variant="soft" :label="game.editeur" />
        </div>
        <p class="text-gray-600 mt-2">{{ game.description }}</p>
      </div>
      <div>
        <UButton v-if="rentStatus.status === 'available' || (rentStatus.status === 'rented' && !rentStatus.byMe)" color="info" label="Louer" leading-icon="i-lucide-square-arrow-out-up-right" :disabled="(rentStatus.status === 'rented' && !rentStatus.byMe) || !user" @click="startRent" />
        <UButton v-else-if="rentStatus.status === 'rented' && rentStatus.byMe" color="error" label="Rendre" leading-icon="i-lucide-corner-down-left" @click="returnRent" />
      </div>
    </div>
    <div class="mt-8">
      <div class="flex items-center gap-3">
        <p class="text-2xl font-bold">Avis</p>
        <UButton color="info" class="rounded-full" icon="i-lucide-plus" :disabled="disableReviewCreation" @click="createNewReview" />
      </div>
      <div class="grid grid-cols-4 gap-8 mt-4">
        <div v-for="avisItem in avis.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())" :key="avisItem.id_utilisateur" class="flex flex-col gap-2 mt-4">
          <div class="flex items-center gap-2">
            <UAvatar :alt="avisItem.nom" size="2xl" />
            <div class="flex flex-col">
              <p class="text-lg font-bold" :class="{ italic: avisItem.id_utilisateur === user }">{{ avisItem.id_utilisateur === user ? "Moi" : avisItem.nom }}</p>
              <StarsContainer :value="avisItem.note" />
            </div>
          </div>
          <p>
            {{ avisItem.commentaire }}
          </p>
          <p class="text-gray-500 text-sm text-right italic">{{ new Date(avisItem.date).toLocaleDateString() }}</p>
          <div v-if="avisItem.id_utilisateur === user || isAdmin" class="flex justify-end">
            <UButtonGroup>
              <UButton color="error" icon="i-lucide-trash-2" @click="callDeleteReview(avisItem.id_utilisateur, gameId)" />
              <UButton v-if="avisItem.id_utilisateur === user" color="info" icon="i-lucide-edit" @click="callEditReview(gameId, avisItem.note, avisItem.commentaire)" />
            </UButtonGroup>
          </div>
        </div>
      </div>
    </div>
  </UContainer>
</template>

<style scoped>

</style>