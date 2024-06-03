import Link from 'next/link';
import NavLinks from './nav-links';
import Image from 'next/image';
import { PowerIcon } from '@heroicons/react/24/outline';

import { Separator } from '@/components/ui/separator';
export default function SideNav() {
    return (
        <div className="flex h-full flex-col px-3 py-4 md:px-2">
            <Link
                className="mb-2 flex h-20 items-end justify-center rounded-md bg-gray-300 p-4 md:h-40"
                href="/"
            >
                <div className="relative w-full h-full text-white md:w-40">
                    <div className="hidden md:block h-full w-full flex items-center justify-center">
                        <Image
                            src="/sharyommto-logo-audi-2-draft-red.png"
                            layout="fill"
                            objectFit="contain"
                            alt="logo"
                        />
                    </div>
                    <div className="block md:hidden h-full w-full flex items-center justify-center">
                        <Image
                            src="/sharyomtto-logo-audi-horizontal.png"
                            layout="fill"
                            objectFit="contain"
                            alt="logo"
                        />
                    </div>
                </div>
            </Link>
            <div className="flex grow flex-row justify-between space-x-2 md:flex-col md:space-x-0 md:space-y-2">
                <NavLinks />
                <div className="hidden h-auto w-full grow rounded-md bg-white md:block"></div>
                <Separator className='hidden md:block'></Separator>
                <form>

                    <Link href="/login" className="flex h-[48px] w-full grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none md:justify-start md:p-2 md:px-3">
                        <PowerIcon className="w-6" />
                        <div className="hidden md:block">Cerrar Sesion</div>
                    </Link>

                </form>
            </div>
        </div>
    );
}
