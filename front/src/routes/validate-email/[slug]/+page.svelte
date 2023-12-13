<script>
	import { page } from '$app/stores';
    import { onMount } from 'svelte';
	
	let slug = $page.params.slug;
	let response = undefined;

	onMount(() => {
		fetch(`http://0.0.0.0:3000/user/email/verify/${slug}`)
		.then(function(result){
			if (result.ok) {
				response = "Email validé";
			} else if (result.status == 401) {
				response = "Le lien de validation a expiré";
			} else if (result.status == 400) {
				response = "Email déjà validé";
			} else {
				response = "Une erreur a eu lieu lors de la validation";
			}
		})
	});

</script>


<div class="text-center my-16">
	{#if response}
		<p>{response}</p>
	{/if}
</div>
