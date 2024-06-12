// src/utils/getCookies.js
import { cookies } from 'next/headers';

export async function getCookies() {
    const session = cookies().get("session")?.value;
    const userId = cookies().get("user_id")?.value;
    return { session, userId };
}