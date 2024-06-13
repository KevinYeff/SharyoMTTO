import {
    UserGroupIcon,
    HomeIcon,
    DocumentDuplicateIcon,
    CalendarIcon,
    TruckIcon,
    Squares2X2Icon,
    BuildingStorefrontIcon,
    HomeModernIcon,
    UserIcon
} from '@heroicons/react/24/outline';
import Link from 'next/link';
import { cilCarAlt } from '@coreui/icons';
// Map of links to display in the side navigation.
// Depending on the size of the application, this would be stored in a database.
const links = [
    { name: 'Dashboard', href: '/dashboard', icon: Squares2X2Icon },
    { name: 'Calendario', href: '/dashboard/calendario', icon: CalendarIcon },
    { name: 'Tus Autos', href: '/dashboard/autos', icon: TruckIcon },
    { name: 'Tus Talleres', href: '/dashboard/talleres', icon: HomeModernIcon },
    { name: 'Tus Tiendas', href: '/dashboard/tiendas', icon: BuildingStorefrontIcon },
    { name: 'Tus Mecanicos', href: '/dashboard/mecanicos', icon: UserIcon },
];

export default function NavLinks() {
    return (
        <>
            {links.map((link) => {
                const LinkIcon = link.icon;
                return (
                    <Link
                        key={link.name}
                        href={link.href}
                        className="flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none md:justify-start md:p-2 md:px-3"
                    >
                        <LinkIcon className="w-6" />
                        <p className="hidden md:block">{link.name}</p>
                    </Link>
                );
            })}
        </>
    );
}
