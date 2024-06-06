
import React from 'react'
import AddVehicleModal from '@/componentes_propios/modals/AddVehicleModal'
import AddTallerModal from '@/componentes_propios/modals/AddTallerModal'
import AddMecanicoModal from '@/componentes_propios/modals/AddMecanicoModal'
import AddTiendaModal from '@/componentes_propios/modals/AddTiendaModal'

function page() {
    return (
        <div className="flex mx-10 justify-between items-center">
            <h2 className="text-3xl font-semibold mb-4">Tus vehiculos</h2>
            <AddVehicleModal />

            <AddTallerModal />
            <AddMecanicoModal />
            <AddTiendaModal />
        </div>
    )
}

export default page