"use server"
import { cookies } from "next/headers";

import { getUrl } from "@/lib/url";

const APIURL = getUrl();

export async function getMaintenances() {
    //TODO ver como hacer el fetch

    const session = await cookies().get("session")?.value;
    const user_id = await cookies().get("user_id")?.value;
    if (!session) return [];
    const res = await fetch(`${APIURL}/work_order/mtto/list/${1}/`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${session}`,
        },
    });

    const data = await res.json();
    return data;

}

