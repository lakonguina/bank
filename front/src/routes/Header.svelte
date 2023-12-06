<script>
	import { JWT, user } from './store.js';	
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';

	import logo from '$lib/images/svelte-logo.svg';

	async function disconnect() {
		$JWT = false;
		$user = false;
		goto('/login')
	}
</script>

<header>
	<nav>
		<ul>
			<a href="/">
				<img alt="The project logo" src={logo} />
			</a>

			{#if !$JWT || $JWT === false}
				<li aria-current={$page.url.pathname === '/login' ? 'page' : undefined}>
					<a href="/login">Login</a>
				</li>
				<li aria-current={$page.url.pathname === '/register' ? 'page' : undefined}>
					<a href="/register">Register</a>
				</li>
			{:else}
				<li aria-current={$page.url.pathname === '/dashboard' ? 'page' : undefined}>
					<a href="/dashboard">Dashboard</a>
				</li>
				<li aria-current={$page.url.pathname === '/information' ? 'page' : undefined}>
					<a href="/information">Information</a>
				</li>
				<li>
					<button on:click={disconnect}>Disconnect</button>
				</li>
			{/if}
		</ul>
	</nav>
</header>

<style>
</style>
