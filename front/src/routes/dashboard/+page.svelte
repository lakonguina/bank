<script>
	import { JWT, user, getUserInformation } from '../store.js';	
	import { goto } from '$app/navigation';
    import { onMount } from 'svelte';

	onMount(async () => {
		getUserInformation();
	});
</script>

<svelte:head>
	<title>Dashboard</title>
	<meta name="description" content="Dashboard" />
</svelte:head>

<div>This is the dashboard</div>
<div>This is the token {$JWT}</div>

<hr>
{#if $user}
	<div>login: {$user.login}</div>
	<div>firstname: {$user.first_name}</div>
	<div>lastname: {$user.last_name}</div>
	<div>email: {$user.email.email}</div>
	<div>phone: {$user.phone.phone}</div>
	<div>status: {$user.user_status.slug}</div>
{/if}