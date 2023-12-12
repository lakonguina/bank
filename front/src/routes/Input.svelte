<script>
	export let text;
	export let type;
	export let name;
    export let required = false;
</script>

<div>
    <div class="text-base font-bold">
        {text}

        {#if required}
            <span class="text-red">*</span>
        {/if}
    </div>
    <input
        class="border border-grey w-full my-2 py-1 px-1"
        type={type}
        name={name}
        required={required}
    />
</div>