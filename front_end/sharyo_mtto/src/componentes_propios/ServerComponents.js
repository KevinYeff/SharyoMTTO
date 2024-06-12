// src/componentes_propios/ServerComponent.js
import { cookies } from "next/headers";
import React from "react";
export default async function ServerComponent({ children }) {
    const session = await cookies().get("session")?.value;
    const userId = await cookies().get("user_id")?.value;

    return (
        <>
            {React.cloneElement(children, { session, userId })}
        </>
    );
}
