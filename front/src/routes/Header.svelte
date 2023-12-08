<script>
	import { JWT, user } from './store.js';	
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';

	import logo from '$lib/images/svelte-logo.svg';

	async function disconnect() {
		$JWT = "false";
		$user = null;
		goto('/login')
	}
</script>

<header>
	<div class="flex justify-between items-center mx-auto max-w-screen-xl py-4">
		<a href="/" class="flex">
			<img src={logo} class="mr-3 h-6 sm:h-9" alt="Logo" />
			<span class="self-center text-xl font-semibold dark:text-white">Bank</span>
		</a>
		<div class="flex items-center">
			<a href="/" class="mr-2">
				Marchés
			</a>
			{#if !$JWT || $JWT === "false"}
				<a href="/login" class="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 mr-2">
					Se connecter
				</a>
				<a href="/register" class="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4">
					Ouvrir un compte
				</a>
			{:else}
				<a href="/dashboard" class="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 mr-2">
					Accéder à l'application
				</a>
				<button class="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4">
					Mon compte
				</button>
			{/if}
		</div>	
	</div>
</header>