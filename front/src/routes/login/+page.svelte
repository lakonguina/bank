<script>
	import { JWT } from '../store.js';	
	import { goto } from '$app/navigation';

	let detail;

	async function login(event) {
		detail = null;

		const data = new FormData(event.target)

		const login = data.get('login');
		const password = data.get('password');

		var payload = {
			login: login,
			password: password,
		};

		fetch("http://0.0.0.0:3000/user/login", {
			method: "POST",
			headers: {"content-type": "application/json"},
			body: JSON.stringify(payload)
		})
		.then(function(result){
			console.log(result);
			return result.json();
		})
		.then(function(data){
			if ("detail" in data) {
				detail = data["detail"];
			} else {
				JWT.set(data['access_token']);
				
				goto('/')
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
		<label for="login">Login</label>
    	<input type="text" name="login" required>
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