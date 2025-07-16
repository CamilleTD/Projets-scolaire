<script setup lang="ts">
import { h, resolveComponent } from 'vue'
import { EditGameModal, CreateGameModal } from "#components";

definePageMeta({
  name: 'Admin Panel - Jeux',
  layout: 'admin',
})

const games = ref<Game[]>([])
const loading = ref(true)


const overlay = useOverlay()

async function editGame(game: Game) {
  const modal = overlay.create(EditGameModal, {
    props: {
      game: game,
    }
  })

  const instance = modal.open()

  const result = await instance.result

  if (result) {
    games.value = await getAllGames()
  }
}

async function addGame() {
  const modal = overlay.create(CreateGameModal, {
    props: {}
  })

  const instance = modal.open()

  const result = await instance.result

  if (result) {
    games.value = await getAllGames()
  }
}

const columns = [
  {
    accessorKey: 'id_jeu',
    header: '#',
    sortable: true,
  },
  {
    accessorKey: 'nom',
    header: 'Nom',
    sortable: true,
  },
  {
    accessorKey: 'description',
    header: 'Description',
    sortable: true,
  },
  {
    accessorKey: 'annee_sortie',
    header: 'Année de sortie',
    sortable: true,
  },
  {
    accessorKey: 'Éditeur',
    header: 'editeur',
    sortable: true,
  },
  {
    accessorKey: 'note_moyenne',
    header: 'Note moyenne',
    sortable: true,
  },
  {
    accessorKey: 'actions',
    header: 'Actions',
    cell: ({ row }) => {
      const UButtonGroup = resolveComponent('UButtonGroup')
      const UButton = resolveComponent('UButton')
      return h(UButtonGroup, {}, () => {
        return [
          h(UButton, {
            color: 'error',
            icon: 'i-lucide-trash',
            onClick: async () => {
              const result = await deleteGame(row.original.id_jeu)
              if (result) {
                games.value = games.value.filter(game => game.id_jeu !== row.original.id_jeu)
              }
            },
          }),
          h(UButton, {
            color: 'info',
            icon: 'i-lucide-edit',
            onClick: () => {
              return editGame(row.original)
            }
          })
        ]
      })
    }
  }
]

onMounted(async () => {
  games.value = await getAllGames()
  loading.value = false
})
</script>

<template>
  <UContainer>
    <div class="flex flex-row justify-between items-center my-4">
      <h1 class="text-3xl font-bold">Jeux</h1>
      <UButton
        color="info"
        icon="i-lucide-plus"
        class="rounded-full"
        @click="addGame"
      />
    </div>
    <UTable :columns="columns" :data="games" :loading="loading" />
  </UContainer>
</template>

<style scoped>

</style>