<script setup lang="ts">
import type {FormSubmitEvent} from "#ui/types";

definePageMeta({
  layout: 'fullscreen',
  middleware: 'no-auth',
  name: 'Inscription',
})

const userStore = useUserStore()

const loading = ref(false)

const fields = [{
  name: 'name',
  type: 'text' as const,
  label: 'Name',
  placeholder: 'Entrez votre nom',
  required: true
}, {
  name: 'email',
  type: 'text' as const,
  label: 'Email',
  placeholder: 'Entrez votre email',
  required: true
}, {
  name: 'password',
  label: 'Password',
  type: 'password' as const,
  placeholder: 'Entrez votre mot de passe',
  required: true
}, {
  name: 'rePassword',
  label: 'Password repeat',
  type: 'password' as const,
  placeholder: 'Entrez à nouveau votre mot de passe',
  required: true
}]

async function onSubmit(payload: FormSubmitEvent<{ name: string, email: string, password: string, rePassword: string }>) {
  if (payload.data.password !== payload.data.rePassword) {
    alert("Les mots de passe ne correspondent pas")
    return
  }
  loading.value = true
  console.log("Login payload:", payload)
  await register(payload.data.name, payload.data.email, payload.data.password)
  await userStore.login(payload.data.email, payload.data.password)
  loading.value = false
  navigateTo('/')
}
</script>

<template>
  <div class="flex flex-col items-center justify-center gap-4 p-4 w-screen h-screen">
    <UPageCard class="w-full max-w-md">
      <UAuthForm
        title="FindYourGame"
        description="Inscrivez vous à FindYourGame pour profiter de toutes les fonctionnalités du site !"
        icon="i-lucide-user"
        :fields="fields"
        :submit="{ label: 'S\'inscrire' }"
        @submit="onSubmit"
      >
        <template #footer>
          <p class="text-sm text-center">
            Déjà inscrit ?
            <ULink
              to="/login"
              class="text-blue-500 hover:text-blue-700 font-semibold">
              Connectez-vous
            </ULink>
          </p>
        </template>
      </UAuthForm>
    </UPageCard>
  </div>
</template>

<style scoped>

</style>