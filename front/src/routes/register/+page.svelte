<script>
	let error;

	async function register(event) {
		error = "";

		const data = new FormData(event.target)

		const login = data.get('login');
		const firstname = data.get('firstname');
		const lastname = data.get('lastname');
		const email = data.get('email');
		const phone = data.get('phone');
		const password = data.get('password');
		const passwordConfirm = data.get('passwordConfirm');

		if (password !== passwordConfirm) {
			error = "Passwords are different";
		}

		var payload = {
    		login: login,
    		first_name: firstname,
			last_name: lastname,
			email: email,
			phone: phone,
			password: password,
			passwordConfirm: passwordConfirm
		};

		fetch("http://0.0.0.0:3000/customer/register", {
    		method: "POST",
			headers: {"content-type": "application/json"},
    		body: JSON.stringify(payload)
		})
		.then(function(res){
			return res.json();
		})
		.then(function(data){
			console.log(JSON.stringify(data))
		})
	}
</script>

<svelte:head>
	<title>Register</title>
	<meta name="description" content="Register" />
</svelte:head>

<form on:submit|preventDefault={register}>
	<div>
		<label for="login">Login<label>
    	<input type="text" name="login" required>
	</div>
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

	{#if error}
		<p>{error}</p>
	{/if}

</form>