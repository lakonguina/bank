<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/svelte-logo.svg';
	import github from '$lib/images/github.svg';
</script>

<header>
	<nav>
		<ul>
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">Home</a>
			</li>
			<li aria-current={$page.url.pathname === '/login' ? 'page' : undefined}>
				<a href="/login">Login</a>
			</li>
			<li aria-current={$page.url.pathname === '/register' ? 'page' : undefined}>
				<a href="/register">Register</a>
			</li>
		</ul>
	</nav>
</header>

<style>
</style>
