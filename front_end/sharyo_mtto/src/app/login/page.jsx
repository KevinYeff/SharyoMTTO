"use client"
/**
* This code was generated by v0 by Vercel.
* @see https://v0.dev/t/1ztOjIUO9hp
* Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
*/
import Link from "next/link"
import { CardTitle, CardDescription, CardHeader, CardContent, CardFooter, Card } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import GoogleButton from 'react-google-button'
function LoginPage() {
    return (
        <div className="flex flex-col justify-center items-center pt-10 ">
            <h2 className="mb-5 text-4xl">Sharyo Mtto</h2>
            <Card className="min-w-96">
                <CardHeader>
                    <CardTitle className="text-2xl justify-center ">Inicio De Sesion</CardTitle>
                    <CardDescription>Porfavor ingrese sus credenciales.</CardDescription>


                </CardHeader>


                <CardContent className="space-y-4">

                    <div className="space-y-2">
                        <Label htmlFor="username">Nombre de Usuario / Email</Label>
                        <Input id="username" placeholder="Nombre de Usuario / Email" required type="text" />
                    </div>
                    <div className="space-y-2">
                        <Label htmlFor="password">Contraseña</Label>
                        <Input id="password" required type="password" />
                    </div>
                </CardContent>
                <CardContent className="space-y-4">
                    <Separator></Separator>
                    <p>No tienes Cuenta? <span className="font-bold hover:italic"><Link className="" href={"/signup"}>Signup</Link></span></p>
                    <p>Te olvidaste tu contraseña? <span className="font-bold hover:italic"><Link className="" href={"/"}>Recuperar</Link></span></p>

                </CardContent>

                <CardFooter>
                    <Button className="w-full hover:bg-blue-500 transition-colors">Sign in</Button>
                </CardFooter>
            </Card>
        </div>
    );
}

export default LoginPage