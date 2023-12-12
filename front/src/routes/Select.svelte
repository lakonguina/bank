
<script>
	export let data;
	export let value;
	export let valueName;

	export let text;
	export let name;
    export let required = false;
</script>

<div>
    <div class="text-base font-bold">
        {text}
        {#if required}
            <span class="text-red-600">*</span>
        {/if}
    </div>
    <select name={name} class="border border-grey bg-white w-full my-2 py-1 px-1" required={required}>
        {#each data as d}
            <option value={d[value]}>{d[valueName]}</option>
        {/each}
    </select>
</div>