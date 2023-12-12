<script>
	import Header from './Header.svelte';
	import Footer from './Footer.svelte';
	import "../app.css";
</script>

<div class="flex flex-col min-h-screen">
	<Header />

	<main>
		<slot />
	</main>

	<Footer/>
</div>

<style>
</style>
