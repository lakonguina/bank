<script>
	import { JWT, user, getUserInformation } from '../store.js';	
    import { onMount } from 'svelte';

	onMount(() => {
		getUserInformation();
	});
</script>

<svelte:head>
	<title>Dashboard</title>
	<meta name="description" content="Dashboard" />
</svelte:head>

{#if $user}
	{#if $user.status.slug == "waiting-for-validation" || $user.email.is_valid == false}
		<div
			class="mt-48 text-center font-bold"
		>
			<div class="flex items-center justify-center">
				{#if $user.status.slug == "waiting-for-validation" }
					<svg class="h-4 me-2 text-orange" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
						<circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line>
					</svg>
					Votre compte est en cours de validation.
				{:else}
					<svg class="h-4 me-2 text-green" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
						<path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z"/>
					</svg>
					Votre compte est validé.
				{/if}
			</div>
			<div class="flex items-center justify-center">
				{#if $user.email.is_valid == false }
					<svg class="h-4 me-2 text-orange" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" stroke="#ffffff" >
						<circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line>
					</svg>
					Veuillez valider votre adresse email.
				{:else}
					<svg class="h-4 me-2 text-green" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
						<path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z"/>
					</svg>
					Adresse email validé.
				{/if}
			</div>
		</div>
	{/if}
{/if}