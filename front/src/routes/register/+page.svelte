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
			detail = "Mot de passe différent";
			return
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
			console.log(result);
			return result.json();
		})
		.then(function(data){
			console.log(data);
			detail = data["detail"];
		})
	}
</script>

<svelte:head>
	<title>Register</title>
	<meta name="description" content="Register" />
</svelte:head>

<div class="flex justify-center">
	<form 
		class="bg-white border border-inherit w-4/12 py-6 px-6 mt-32"
		on:submit|preventDefault={register}
	>
		<div>
			<div class="text-base font-bold">Prénom</div>
			<input
				class="border border-inherit w-full my-2 py-1 px-1"
				type="firstname"
				name="firstname"
				required
			>
		</div>

		<div>
			<div class="text-base font-bold">Nom</div>
			<input
				class="border border-inherit w-full my-2 py-1 px-1"
				type="lastname"
				name="lastname"
				required
			>
		</div>

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
			<div class="text-base font-bold">Téléphone</div>
			<input
				class="border border-inherit w-full my-2 py-1 px-1"
				type="text"
				name="phone"
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

		<div>
			<div class="text-base font-bold">Confirmé le mot de passe</div>
			<input
				class="border border-inherit w-full my-2 py-1 px-1"
				type="password"
				name="passwordConfirm"
				required
			>
		</div>

		<button 
			class="bg-blue-500 hover:bg-blue-700 text-white py-2 mt-2 w-full"
			type="submit"
		>
			S'enregistrer
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