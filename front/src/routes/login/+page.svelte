<svelte:head>
	<title>Login</title>
	<meta name="description" content="Login" />
</svelte:head>

<form method="POST" action="/login">
	<div>
		<label for="name">Username</label>
    	<input type="text" name="name" required>
	</div>

	<div>
    	<label for="password">Password</label>
    	<input type="password" name="password" required>
	</div>

	<button type="submit">Login</button>
</form>