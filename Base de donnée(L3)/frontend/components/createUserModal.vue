<script setup lang="ts">
const nom = ref('')
const email = ref('')
const password = ref('')
const role = ref<'Membre' | 'Administrateur'>('Membre')

const emit = defineEmits<{ close: [boolean] }>()

async function submitUserCreation() {
  createUser(nom.value, email.value, password.value, role.value)
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
    title="Créer utilisateur"
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
          label="Créer"
          class="mt-4"
          @click="submitUserCreation"
        />
      </div>
    </template>
  </UModal>
</template>

<style scoped>

</style>