"use server"
import React from 'react'
import AddVehicleModal from '@/componentes_propios/modals/AddVehicleModal'
import AddTallerModal from '@/componentes_propios/modals/AddTallerModal'
import AddMecanicoModal from '@/componentes_propios/modals/AddMecanicoModal'
import AddTiendaModal from '@/componentes_propios/modals/AddTiendaModal'
import { getTalleres } from '@/actions/talleres'
const page = async () => {
    let talleres = await getTalleres();
    return (
        <div>
            <div className="flex mx-10 justify-between items-center">
                <h2 className="text-3xl font-semibold mb-4">Tus Talleres</h2>


                <AddTallerModal />

            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-4 mt-4 w-full">

                <h1>asd{talleres}</h1>
            </div>

        </div>


    )
}

export default page