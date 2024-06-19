"use client";
import Image from "next/image";
import Link from "next/link";
import { CardTitle, CardDescription, CardHeader, CardContent, CardFooter, Card } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { useRouter, useSearchParams } from "next/navigation";
import { useUser } from "@/methods/zustand/userZustand";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { login } from "@/lib/auth";

// Define form schema
const formSchema = z.object({
    email: z.string().email(),
    password: z.string().min(6),
});

function LoginPage() {
    const router = useRouter();
    const searchParams = useSearchParams();
    const setUser = useUser((state) => state.setUser);

    const form = useForm({
        resolver: zodResolver(formSchema),
        defaultValues: {

            email: searchParams.get("email") || "",
            password: searchParams.get("password") || "",
        },
    });

    const onSubmit = async (values) => {
        try {
            let res = await fetch("http://127.0.0.1:8000/user/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    email: values.email,
                    password: values.password,
                }),
            });

            if (res.status === 404) {
                form.setError("root", { message: "Credenciales invalidas" });
                return;
            }

            const data = await res.json();
            if (data.multiple) {
                console.log(data.account);
                return;
            }

            setUser(data);
            await login(data);
            console.log("Se esta guardando la cookie")
            document.cookie = `user_id=${data.id}; path=/; SameSite=Lax`; // Guarda el token en las cookies con SameSite

            router.push("/dashboard/calendario"); // Redirige al usuario a la página del dashboard
        } catch (error) {
            console.error("Error en el login:", error);
        }
    };

    return (
        <div className="flex flex-col justify-center items-center">
            <Image
                src="/sharyommto-logo-audi-2-draft-red.png"
                width={150}
                height={150}
                objectFit="contain"
                alt="logo"
            />

            <Card className="min-w-96 m-1">
                <CardHeader>
                    <CardTitle className="text-2xl justify-center">Inicio De Sesion</CardTitle>
                    <CardDescription>Por favor ingrese sus credenciales.</CardDescription>
                </CardHeader>

                <CardContent className="space-y-4">
                    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                        <div className="space-y-2">
                            <Label htmlFor="email">Email</Label>
                            <Input
                                {...form.register("email")}
                                id="email"
                                placeholder="Email"
                                required
                                type="email"
                            />
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="password">Contraseña</Label>
                            <Input
                                {...form.register("password")}
                                id="password"
                                required
                                type="password"
                            />
                        </div>
                        <Separator />
                        <p>No tienes cuenta? <span className="font-bold hover:italic"><Link href="/signup">Signup</Link></span></p>
                        <p>Te olvidaste tu contraseña? <span className="font-bold hover:italic"><Link href="/">Recuperar</Link></span></p>
                        <CardFooter>
                            <Button type="submit" className="w-full hover:bg-blue-500 transition-colors">Sign in</Button>
                        </CardFooter>
                    </form>
                </CardContent>
            </Card>
        </div>
    );
}

export default LoginPage;
