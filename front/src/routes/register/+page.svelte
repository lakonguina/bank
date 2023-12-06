<script>
	let detail;

	async function register(event) {
		detail = null;

		const data = new FormData(event.target)

		const firstname = data.get('firstname');
		const lastname = data.get('lastname');
		const email = data.get('email');
		const phone = data.get('phone');
		const password = data.get('password');
		const passwordConfirm = data.get('passwordConfirm');

		if (password !== passwordConfirm) {
			detail = "Passwords are different";
		}

		var payload = {
			first_name: firstname,
			last_name: lastname,
			email: email,
			phone: phone,
			password: password,
		};

		fetch("http://0.0.0.0:3000/user/register", {
			method: "POST",
			headers: {"content-type": "application/json"},
			body: JSON.stringify(payload)
		})
		.then(function(result){
			return result.json();
		})
		.then(function(data){
			detail = data["detail"];
		})
	}
</script>

<svelte:head>
	<title>Register</title>
	<meta name="description" content="Register" />
</svelte:head>

<form on:submit|preventDefault={register}>
	<div>
		<label for="firstname">First name<label>
    	<input type="text" name="firstname" required>
	</div>
	<div>
		<label for="lastname">Last name<label>
    	<input type="text" name="lastname" required>
	</div>
	<div>
    	<label for="email">Email</label>
    	<input type="email" name="email" required>
	</div>
	<div>
    	<label for="phone">Phone</label>
    	<input type="text" name="phone" required>
	</div>
	<div>
    	<label for="password">Password</label>
    	<input type="password" name="password" required>
	</div>
	<div>
    	<label for="password">Confirm password</label>
    	<input type="password" name="passwordConfirm" required>
	</div>

	<button type="submit">Register</button>

	{#if detail}
		<p>{detail}</p>
	{/if}
</form>