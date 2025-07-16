<script setup lang="ts">
const props = defineProps<{
  user: UserInfo
}>()

const { user } = toRefs(props)

const nom = ref(user.value.nom)
const email = ref(user.value.email)
const password = ref('')
const role = ref(user.value.role)

const emit = defineEmits<{ close: [boolean] }>()

async function submitUserUpdate() {
  updateUser(user.value.id_utilisateur, nom.value.length ? nom.value : undefined, email.value.length ? email.value : undefined, password.value.length ? password.value : undefined, role.value)
    .then(() => {
      emit('close', true)
    })
    .catch((error) => {
      console.error(error)
      emit('close', false)
      // Handle error
    })
}
</script>

<template>
  <UModal
    :title="`Modifier ${user.nom}`"
    :close="{ onClick: () => emit('close', false) }">
    <!-- Modal content -->
    <template #body>
      <div class="flex flex-col items-center gap-4">
        <UInput
          v-model="nom"
          label="Nom"
          placeholder="Nom"
          class="w-full" />
        <UInput
          v-model="email"
          label="Email"
          type="email"
          placeholder="Email"
          class="w-full" />
        <UInput
          v-model="password"
          label="Mot de passe"
          type="password"
          placeholder="Mot de passe"
          class="w-full" />
        <UInputMenu
          v-model="role"
          label="Rôle"
          placeholder="Sélectionner un rôle"
          :items="['Membre', 'Administrateur']"
          class="w-full" />
        <UButton
          label="Mettre à jour"
          class="mt-4"
          @click="submitUserUpdate"
        />
      </div>
    </template>
  </UModal>
</template>

<style scoped>

</style>