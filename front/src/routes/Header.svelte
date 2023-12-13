<script>
	import logo from "$lib/images/logo.png"
	import { JWT } from './store.js';	
	import Button from './Button.svelte';


	async function show() {
		const sidebar = document.getElementById('sidebar');

		if (sidebar.style.display == "block") {
			sidebar.style.display = "none"
		} else {
			sidebar.style.display = "block"
		}
	}


</script>

<header>
	<div class="flex justify-between items-center mx-auto max-w-screen-xl py-4 px-2">
		<a href="/" class="flex">
			<img src={logo} class="mr-3 h-16" alt="Logo" />
			<!-- <span class="self-center text-xl font-semibold dark:text-white">Bank</span> -->
		</a>

		<div>
			<!-- Button -->
			<div class="flex items-center hidden md:block">
				<a class="mr-2 font-bold" href="/">Tarifications</a>
				<a class="mr-2 font-bold" href="/">Services</a>

				{#if !$JWT || $JWT === "false"}
					<Button link="/login" text="Se connecter"/>
					<Button link="/register" text="Ouvrir un compte"/>
				{:else}
					<Button link="/dashboard" text="Accéder à l'application"/>
					<Button link="/information" text="Mon compte"/>
				{/if}
			</div>	

			<!-- Hamburger -->
			<div class="block md:hidden">
				<button on:click={show}>
					<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#9b9b9b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
				</button>
			</div>
		</div>
	</div>
</header>

<div id="sidebar" class="fixed h-screen top-0 right-0 mt-14 bg-white md:invisible w-2/3" style="display:none;">
		<div class="px-4 mt-2">
			<a href="/">Tarifications</a>
		</div>
		<div class="px-4 mt-2">
			<a href="/">Services</a>
		</div>

		{#if !$JWT || $JWT === "false"}
			<div class="px-4 mt-2">
				<Button link="/login" text="Se connecter"/>
			</div>
			<div class="px-4 mt-4">
				<Button link="/register" text="Ouvrir un compte"/>
			</div>
		{:else}
			<div class="px-4 mt-2">
				<Button link="/dashboard" text="Accéder à l'application"/>
			</div>
			<div class="px-4 mt-2">
				<Button link="/information" text="Mon compte"/>
			</div>
		{/if}
</div>
<style>
	details > summary {
		list-style: none;
	}

	details > summary::-webkit-details-marker {
		display: none;
	}
</style>