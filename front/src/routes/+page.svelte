<script>
	import Building from "$lib/images/building.jpg"
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Bank demo app" />
</svelte:head>

<div class="mb-16">
	<img
		src={Building}
		class=""
		id="building"
		alt="Banner of the website representing a corporate building"
	/>
	<div class="2xl:px-96 xl:px-48 px-2">
		<div class="mt-16 px-4 border-l-8 border-blue">
			<p class="text-2xl font-bold">A propos de nous</p>
			<p>Vanguard est une société d’investissement différente. Le groupe a été fondé aux États-Unis en 1975 sur une idée simple mais révolutionnaire : celle qu’une société d’investissement doit gérer ses fonds uniquement dans l’intérêt de ses clients.</p>
			<br>
			<p>Cette philosophie a permis à des millions de personnes dans le monde d’atteindre leurs objectifs grâce à des investissements simples et peu coûteux.</p>
			<br>
			<p>C’est ce que nous défendons, la création de valeur pour les investisseurs.</p>
		</div>

		<p class="text-2xl font-bold mt-16">Découvrez un univers de nouvelles opportunités</p>
		<div class="mt-4 md:flex justify-between gap-8">
			<div class="bg-blue text-white px-4 py-4 mt-4 md:mt-0">
				<p class="text-2xl font-bold">Prix transparents et coûts peu élevés</p>
				<p class="mt-4">Aucun frais de tenu de compte, faibles commissions et des intérêts élevés.</p>
			</div>
			<div class="bg-blue text-white px-4 py-4 mt-4 md:mt-0">
				<p class="text-2xl font-bold">Accès aux marchés Africains</p>
				<p class="mt-4">Investissez en Afrique en actions, indices et obligations à partir d'une seule plateforme.</p>
			</div>
			<div class="bg-blue text-white px-4 py-4 mt-4 md:mt-0">
				<p class="text-2xl font-bold">Accès aux marchés Africains</p>
				<p class="mt-4">Investissez en Afrique en actions, indices et obligations à partir d'une seule plateforme.</p>
			</div>
		</div>
	</div>
</div>