export function getUrl() {
    let url = ""
    if (process.env.API_URL) {
        url = process.env.API_URL
    } else {
        url = "http://localhost:8000"
    }
    return url
}

export async function getGlobalUrl() {
    let url = ""
    if (process.env.GLOBAL_URL) {
        url = process.env.GLOBAL_URL
    } else {
        url = "http://localhost:8000"
    }
    return url
}