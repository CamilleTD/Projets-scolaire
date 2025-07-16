<script setup lang="ts">
import { h, resolveComponent } from 'vue'
import { deleteUser } from "~/composables/api";
import { EditUserModal, CreateUserModal } from "#components";

definePageMeta({
  name: 'Admin Panel - Utilisateurs',
  layout: 'admin',
})

const users = ref<UserInfo[]>([])
const loading = ref(true)


const overlay = useOverlay()

async function editUser(user: UserInfo) {
  const modal = overlay.create(EditUserModal, {
    props: {
      user: user,
    }
  })

  const instance = modal.open()

  const result = await instance.result

  if (result) {
    users.value = await getUsers()
  }
}

async function addUser() {
  const modal = overlay.create(CreateUserModal, {
    props: {}
  })

  const instance = modal.open()

  const result = await instance.result

  if (result) {
    users.value = await getUsers()
  }
}

const columns = [
  {
    accessorKey: 'id_utilisateur',
    header: '#',
    sortable: true,
  },
  {
    accessorKey: 'nom',
    header: 'Nom',
    sortable: true,
  },
  {
    accessorKey: 'email',
    header: 'Email',
    sortable: true,
  },
  {
    accessorKey: 'role',
    header: 'Rôle',
    sortable: true,
  },
  {
    accessorKey: 'nb_evaluations',
    header: 'Évaluations',
    sortable: true,
  },
  {
    accessorKey: 'nb_locations',
    header: 'Locations',
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
              const result = await deleteUser(row.original.id_utilisateur)
              if (result) {
                users.value = users.value.filter(user => user.id_utilisateur !== row.original.id_utilisateur)
              }
            },
          }),
          h(UButton, {
            color: 'info',
            icon: 'i-lucide-edit',
            onClick: () => {
              return editUser(row.original)
            }
          })
        ]
      })
    }
  }
]

onMounted(async () => {
  users.value = await getUsers()
  loading.value = false
})
</script>

<template>
  <UContainer>
    <div class="flex flex-row justify-between items-center my-4">
      <h1 class="text-3xl font-bold">Utilisateurs</h1>
      <UButton
        color="info"
        icon="i-lucide-plus"
        class="rounded-full"
        @click="addUser"
      />
    </div>
    <UTable :columns="columns" :data="users" :loading="loading" />
  </UContainer>
</template>

<style scoped>

</style>