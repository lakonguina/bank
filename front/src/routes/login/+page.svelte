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

<form on:submit|preventDefault={login}>
	<div>
		<label for="email">Email</label>
    	<input type="email" name="email" required>
	</div>

	<div>
    	<label for="password">Password</label>
    	<input type="password" name="password" required>
	</div>

	<button type="submit">Login</button>

	{#if detail}
		<p>{detail}</p>
	{/if}
</form>