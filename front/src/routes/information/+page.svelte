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
<div class="flex px-96 pt-16">
	<div class="flex-none w-56 border-r-2 border-grey">
		<ul class="pl-16">
			<li class="text-xl font-bold">Portefeuille</li>
			<li class="text-xl font-bold">Marché</li>
			<li class="text-xl font-bold">Transactions</li>
		</ul>
	</div>
	<div class="flex-1 px-16">
		<div class="text-xl font-bold">Informations personelles</div>

		<div class="bg-grey p-4">
			<div>
				<span class="font-bold">Prénom:</span>
				{$user.first_name}
			</div>
			<div class="mt-1">
				<span class="font-bold">Nom:</span>
				{$user.last_name}
			</div>
			<div class="mt-1">
				<span class="font-bold">Email:</span>
				{$user.email.email}
				{#if $user.email.is_valid }
					<span class="bg-green p-1 text-white font-bold">Validé</span>
				{:else}
					<span class="bg-orange p-1 text-white font-bold">Email non validé</span>
				{/if}
			</div>
			<div class="mt-1">
				<span class="font-bold">Téléphone:</span>
				{$user.phone.phone}
				{#if $user.phone.is_valid }
					<span class="bg-green p-1 text-white font-bold">Validé</span>
				{:else}
					<span class="bg-orange p-1 text-white font-bold">Téléphone non validé</span>
				{/if}
			</div>
		</div>
	</div>
</div>
{/if}