<script>
	import { JWT } from '../store.js';	
	import { goto } from '$app/navigation';

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
		class="bg-white border border-inherit w-full md:w-4/12 py-6 px-6 md:mt-32  mt-8 mx-2"
		on:submit|preventDefault={login}
	>
		<div>
			<div class="text-base font-bold">Email</div>
			<input
				class="border border-inherit w-full my-2 py-1 px-1"
				type="email"
				name="email"
				required
			>
		</div>

		<div>
			<div class="text-base font-bold">Mot de passe</div>
			<input
				class="border border-inherit w-full my-2 py-1 px-1"
				type="password"
				name="password"
				required
			>
		</div>

		<button 
			class="bg-blue-500 hover:bg-blue-700 text-white py-2 mt-2 w-full"
			type="submit"
		>
			Se connecter
		</button>

		{#if detail}
			<div 
				class="bg-blue-100 mt-2 px-2 py-2 font-bold"
			>
				{detail}
			</div>
		{/if}
	</form>
</div>