import { NextResponse } from 'next/server';
import jwt from 'jsonwebtoken';

const SECRET_KEY = 'django-insecure-r0j$ke9+a)-23yeq5ig^*zll&y%y+ko^og6(eh_v%*1sqrk7hg'; // Asegúrate de usar la misma clave que en tu configuración Django

export async function middleware(req) {
    const { pathname } = req.nextUrl;
    const token = req.cookies.get('access_token').value;
    console.log(token)
    if (pathname.startsWith('/dashboard')) {

        if (!token) {

            return NextResponse.redirect(new URL('/login', req.url));
        }

        try {
            jwt.verify(token, SECRET_KEY);
            return NextResponse.next();
        } catch (err) {
            console.log(err)
            console.log(typeof (token))
            return NextResponse.redirect(new URL('/login', req.url));
        }
    }

    return NextResponse.next();
}

export const config = {
    matcher: ['/dashboard/:path*'], // Asegúrate de que esto apunte a las rutas que quieres proteger
};
