<script>
	import { onMount } from 'svelte';

	import Input from '../Input.svelte';
	import Button from '../Button.svelte';
	import Select from '../Select.svelte';

	let detail;
	let countries = [];


	async function getCountries() {
		fetch("http://0.0.0.0:3000/countries", {
			method: "GET",
			headers: {"content-type": "application/json"},
		})
		.then(function(result){
			return result.json();
		})
		.then(function(data){
			countries = data;
		})
	};

	onMount(() => {
		getCountries();
	});

	async function register(event) {
		detail = null;

		const data = new FormData(event.target)

		const firstname = data.get('firstname');
		const lastname = data.get('lastname');
		const nationality = data.get('nationality');
		const residence = data.get('residence');
		const street = data.get('street');
		const city = data.get('city');
		const zipCode = data.get('zipCode');
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
			country: {
				alpha3: nationality,
			},
			address: {
				alpha3: residence,
				street: street,
				city: city,
				zip_code: zipCode,
			}
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
		class="bg-white border border-inherit w-full md:w-4/12 py-6 px-6 md:mt-32  mt-8 mx-2"
		on:submit|preventDefault={register}
	>
		<Input text="Prénom" type="text" name="firstname" required={true}/>
		<Input text="Nom" type="text" name="lastname" required={true}/>
		<Select text="Nationalité" name="nationality" data={countries} value="alpha3" valueName="name" required={true}/>
		<Select text="Pays d'habitation" name="residence" data={countries} value="alpha3" valueName="name" required={true}/>
		<Input text="Rue" type="text" name="street" required={true}/>
		<Input text="Ville" type="text" name="city" required={true}/>
		<Input text="Code postal" type="text" name="zipCode" required={true}/>
		<Input text="Email" type="email" name="email" required={true}/>
		<Input text="Téléphone" type="text" name="phone" required={true}/>
		<Input text="Mot de passe" type="password" name="password" required={true}/>
		<Input text="Confirmé Mot de passe" type="password" name="passwordConfirm" required={true}/>
		<Button text="S'enregistrer" type="submit"/>

		{#if detail}
			<div 
				class="bg-blue-100 mt-2 px-2 py-2 font-bold"
			>
				{detail}
			</div>
		{/if}
	</form>
</div>