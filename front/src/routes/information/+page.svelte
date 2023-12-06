<script>
	import { user, getUserInformation } from '../store.js';	
    import { onMount } from 'svelte';

	onMount(() => {
		getUserInformation();
	});
</script>

<svelte:head>
	<title>Information</title>
	<meta name="description" content="Information" />
</svelte:head>

{#if $user}
	<div>Firstname: {$user.first_name}</div>
	<div>Lastname: {$user.last_name}</div>
	<div>
		Email: {$user.email.email} -
		{#if $user.email.is_email_active }
			Validé
		{:else}
			Valider votre email
		{/if}
	</div>
	<div>
		Phone: {$user.phone.phone} - 
		{#if $user.phone.is_phone_active }
			Validé
		{:else}
			Valider votre téléphone
		{/if}
	</div>
{/if}