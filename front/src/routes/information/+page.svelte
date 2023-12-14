<script>
    import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { JWT, user, getUserInformation } from '../store.js';	

	import Button from '../Button.svelte';

	onMount(() => {
		getUserInformation();
	});

	async function disconnect() {
		$JWT = "false";
		$user = null;
		goto('/login')
	}
</script>

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
		<div class="mt-2">
			<Button text="Se déconnecter" action={disconnect}/>
		</div>
	</div>
</div>
{/if}