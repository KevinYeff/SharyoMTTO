"use client";
import Image from "next/image";
import Link from "next/link";
import { CardTitle, CardDescription, CardHeader, CardContent, CardFooter, Card } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";

// Define form schema
const formSchema = z.object({
    email: z.string().email(),
    username: z.string().min(3),
    name: z.string().min(1),
    last_name: z.string().min(1),
    mobile: z.string().min(10),
    password: z.string().min(6),
    password2: z.string().min(6),
}).refine(data => data.password === data.password2, {
    message: "Passwords don't match",
    path: ["password2"],
});

function SignupPage() {
    const router = useRouter();

    const form = useForm({
        resolver: zodResolver(formSchema),
        defaultValues: {
            email: "",
            username: "",
            name: "",
            last_name: "",
            mobile: "",
            password: "",
            password2: "",
        },
    });

    const onSubmit = async (values) => {
        try {
            let res = await fetch("http://127.0.0.1:8000/user/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values),
            });

            if (res.status === 400) {
                const errorData = await res.json();
                form.setError("root", { message: errorData.message || "Error en el registro" });
                return;
            }

            // Redirige al usuario al login y pasa las credenciales
            router.push(`/login?email=${encodeURIComponent(values.email)}&password=${encodeURIComponent(values.password)}`);
        } catch (error) {
            console.error("Error en el registro:", error);
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
                    <CardTitle className="text-2xl justify-center">Registrate</CardTitle>
                    <CardDescription>Bienvenido! Por favor ingrese sus credenciales.</CardDescription>
                </CardHeader>

                <CardContent className="space-y-4">
                    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                        <div className="space-y-2">
                            <Label htmlFor="username">Nombre de usuario</Label>
                            <Input
                                {...form.register("username")}
                                id="username"
                                placeholder="Nombre de usuario"
                                required
                                type="text"
                            />
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="name">Nombre</Label>
                            <Input
                                {...form.register("name")}
                                id="name"
                                placeholder="Nombre"
                                required
                                type="text"
                            />
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="last_name">Apellido</Label>
                            <Input
                                {...form.register("last_name")}
                                id="last_name"
                                placeholder="Apellido"
                                required
                                type="text"
                            />
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="mobile">Teléfono móvil</Label>
                            <Input
                                {...form.register("mobile")}
                                id="mobile"
                                placeholder="Teléfono móvil"
                                required
                                type="text"
                            />
                        </div>
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
                        <div className="space-y-2">
                            <Label htmlFor="password2">Repetir contraseña</Label>
                            <Input
                                {...form.register("password2")}
                                id="password2"
                                required
                                type="password"
                            />
                        </div>
                        <Separator />
                        <p>¿Ya tienes cuenta? <span className="font-bold hover:italic"><Link href="/login">Inicia sesión</Link></span></p>
                        <p>¿Olvidaste tu contraseña? <span className="font-bold hover:italic"><Link href="/">Recuperar</Link></span></p>
                        <CardFooter>
                            <Button type="submit" className="w-full hover:bg-blue-500 transition-colors">Registrar</Button>
                        </CardFooter>
                    </form>
                </CardContent>
            </Card>
        </div>
    );
}

export default SignupPage;
