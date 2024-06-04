"use server";
import { SignJWT, jwtVerify } from "jose";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { NextRequest, NextResponse } from "next/server";
import { cache } from "react";

const secretKey = "django-insecure-r0j$ke9+a)-23yeq5ig^*zll&y%y+ko^og6(eh_v%*1sqrk7hg";
const key = new TextEncoder().encode(secretKey);

export async function encrypt(payload) {
    return await new SignJWT(payload)
        .setProtectedHeader({ alg: "HS256" })
        .setIssuedAt()
        .setExpirationTime("10 hour from now")
        .sign(key);
}

export async function decrypt(input) {
    try {
        const { payload } = await jwtVerify(input, key, {
            algorithms: ["HS256"],
        });
        return payload;
    } catch (e) {
        console.log(e)
        return null;
    }
}


export async function login(formData) {
    // Verify credentials && get the user

    const expires = new Date(Date.now() + 10 * 60 * 60 * 1000);
    const session = formData.access_token;
    // Save the session in a cookie
    await cookies().set("session", session, {
        expires,
        httpOnly: true,
        sameSite: "lax",
        path: "/",
        secure: true,
    });
}






export async function getSession() {

    const session = await cookies().get("session")?.value;
    console.log(typeof (session))
    if (!session) {
        console.log("SOY NULL")

        return null;
    }
    return await decrypt(session);
}
