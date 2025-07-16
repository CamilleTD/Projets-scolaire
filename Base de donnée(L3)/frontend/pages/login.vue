<script setup lang="ts">
import type {FormSubmitEvent} from "#ui/types";

definePageMeta({
  layout: 'fullscreen',
  middleware: 'no-auth',
  name: 'Connexion',
})

const userStore = useUserStore()

const loading = ref(false)

const fields = [{
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
}]

async function onSubmit(payload: FormSubmitEvent<{ email: string, password: string }>) {
  loading.value = true
  console.log("Login payload:", payload)
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
        description="Connectez vous à FindYourGame pour accéder à votre compte !"
        icon="i-lucide-user"
        :fields="fields"
        :submit="{ label: 'Se connecter' }"
        @submit="onSubmit"
      >
        <template #footer>
          <p class="text-sm text-center">
            Pas encore de compte ?
            <ULink
              to="/signup"
              class="text-blue-500 hover:text-blue-700 font-semibold">
              Inscrivez-vous
            </ULink>
          </p>
        </template>
      </UAuthForm>
    </UPageCard>
  </div>
</template>

<style scoped>

</style>