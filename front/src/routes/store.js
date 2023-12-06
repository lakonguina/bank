import { writable, readable, get } from "svelte/store";
import { browser } from "$app/environment"
import { goto } from '$app/navigation';

let storedJWT;

// Get local storage JWT and set it in store
if (browser) {
    storedJWT = localStorage.getItem("JWT");
}

export const JWT = writable(storedJWT || "false");
export const user = writable(null);

// Tie store update to localStorage
JWT.subscribe(value => {
    if (browser) {
        localStorage.setItem("JWT", value);
    }
});

export async function getUserInformation() {
    if (JWT) {
        const JWTValue = get(JWT);

        if (JWTValue !== "false") {
            const bearer = `Bearer ${get(JWT)}`;

            fetch("http://0.0.0.0:3000/user/information", {
                method: "GET",
                headers: {
                    "content-type": "application/json",
                    "authorization": bearer,
                },
            })
            .then(function(result){
                console.log(result);
                if (result.status === 401) {
                    goto('/login')
                }

                return result.json();
            })
            .then(function(data){
                user.set(data);
            })

        } else {
            goto('/login')
        }

    } else {
        goto('/login')
    }
}