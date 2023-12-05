<script>
	import { JWT } from '../store.js';	
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';
	import { get } from 'svelte/store';

	onMount(() => {
		console.log("OUI");

		if (browser) {
			const value = get(JWT);
			console.log(value);
		}
	});
	/*
	async function getUserInformation(event) {
		fetch("http://0.0.0.0:3000/user/information", {
			method: "GET",
			headers: {
				"content-type": "application/json",
				"authorization": 'Bearer {JWT}'
			},
		})
		.then(function(result){
			console.log(result);
			return result.json();
		})
		.then(function(data){
			console.log(data);
		})
	}
	*/
</script>

<svelte:head>
	<title>Dashboard</title>
	<meta name="description" content="Dashboard" />
</svelte:head>

<div>This is the dashboard</div>