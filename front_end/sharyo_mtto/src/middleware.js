import { NextResponse } from 'next/server';

import { getSession } from "@/lib/auth";
import { cookies } from "next/headers";

const SECRET_KEY = 'django-insecure-r0j$ke9+a)-23yeq5ig^*zll&y%y+ko^og6(eh_v%*1sqrk7hg'; // Asegúrate de usar la misma clave que en tu configuración Django

export async function middleware(req) {
    const session = await getSession();
    const { pathname } = req.nextUrl;
    //console.log(session)


    if (req.nextUrl.pathname.startsWith('/dashboard')) {

        if (!session) {

            return NextResponse.redirect(new URL('/login', req.url));
        }


    }

    return NextResponse.next();
}

export const config = {
    matcher: ['/dashboard/:path*'], // Asegúrate de que esto apunte a las rutas que quieres proteger
};
