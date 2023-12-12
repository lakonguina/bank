<script>
	import { JWT } from '../store.js';	
	import { goto } from '$app/navigation';

	import Button from '../Button.svelte';
	import Input from '../Input.svelte';

	let detail;

	async function login(event) {
		detail = null;

		const data = new FormData(event.target)

		const email = data.get('email');
		const password = data.get('password');

		var payload = {
			email: email,
			password: password,
		};

		fetch("http://0.0.0.0:3000/user/login/email", {
			method: "POST",
			headers: {"content-type": "application/json"},
			body: JSON.stringify(payload)
		})
		.then(function(result){
			console.log(result);
			return result.json();
		})
		.then(function(data){
			console.log(data);
			if ("detail" in data) {
				detail = data["detail"];
			} else {
				$JWT = data['access_token'];

				goto('/dashboard')
			}
		})
	}
</script>

<svelte:head>
	<title>Login</title>
	<meta name="description" content="Login" />
</svelte:head>

<div class="flex justify-center">
	<form 
		class="bg-white border-2 border-grey border-t-8 border-t-blue w-full md:w-4/12 py-6 px-6 md:mt-32  mt-8 mx-2"
		on:submit|preventDefault={login}
	>
		<Input text="Email" type="email" name="email" required={true} />
		<Input text="Mot de passe" type="password" name="password" required={true} />
		<div class="mt-2">
			<Button text="Se connecter" type="submit" />
		</div>
		<p class="mt-2">Mot de passe oublié?</p>
		{#if detail}
			<div 
				class="bg-blue-100 mt-2 px-2 py-2 font-bold"
			>
				{detail}
			</div>
		{/if}
	</form>
</div>