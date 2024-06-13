
import React from 'react';
import { getCookies } from '@/actions/getCookies';
import { getTalleres } from '@/actions/talleres';
import AddTallerModal from '@/componentes_propios/modals/AddTallerModal';
import CardTaller from '@/componentes_propios/talleres/CardTaller';
export default async function Talleres() {
    const talleres = await getTalleres();
    const { session, userId } = await getCookies();
    return (
        <div>
            <div className="pb-4 flex mx-10 justify-between items-center">
                <h2 className="text-3xl font-semibold mb-4">Tus Talleres</h2>
                <AddTallerModal session={session} userId={userId} />



            </div>
            <div className=" grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-4">
                {talleres.map((taller) => (
                    <CardTaller key={taller.name} taller={taller} />
                ))}
            </div>
        </div>
    );
}
