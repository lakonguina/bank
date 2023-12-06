<script>
	import { JWT, user, getUserInformation } from '../store.js';	
    import { onMount } from 'svelte';

	onMount(() => {
		getUserInformation();
	});
	
	console.log($user);
</script>

<svelte:head>
	<title>Dashboard</title>
	<meta name="description" content="Dashboard" />
</svelte:head>

<hr>
{#if $user}
	{#if $user.status.slug == "waiting-for-validation" || $user.email.is_email_active == false}
		{#if $user.status.slug == "waiting-for-validation" }
			<p>Votre compte est en cours de validation.</p>
		{/if}

		{#if $user.email.is_email_active == false }
			<p>Veuillez valider votre email.</p>
		{/if}
	{/if}
{/if}