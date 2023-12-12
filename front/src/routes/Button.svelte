<script>
	export let text;
	export let link = undefined;
	export let action = undefined;
	export let type = "button";


</script>

{#if link}
	<a
		href={link}
		class="bg-blue text-white py-2 px-4 text-white font-bold"
	>
		{text}
	</a>
{:else}
	<button 
		class="bg-blue text-white py-2 px-4 text-white font-bold"
		type={type}
		on:click={action}
	>
		{text}
	</button>
{/if}