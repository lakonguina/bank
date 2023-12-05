import { writable } from "svelte/store";
import { browser } from "$app/environment"

const storedJWT = localStorage.getItem("JWT");

export const JWT = writable(storedJWT);

JWT.subscribe((value) => {
    console.log("TEST", value);
    if (browser) return (localStorage.JWT = value)
})