import { Inter } from "next/font/google";
import "./globals.css";
import navbar from "@/componentes_propios/navbar";
const inter = Inter({ subsets: ["latin"] });
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,


} from "@/components/ui/navigation-menu"
import { navigationMenuTriggerStyle } from "@/components/ui/navigation-menu"

import Link from "next/link";
export const metadata = {

  title: "Mtto Sharyo",
  description: "Una app de mantenimiento de tus autos",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">

      <body className={inter.className}>


        {children}
      </body>
    </html>
  );
}
