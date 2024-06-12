'use client';
import { useState } from 'react';
import ModalVehiculo from './ModalVehiculo';

export default function CardVehiculo({ vehiculo }) {
    const [isOpen, setIsOpen] = useState(false);

    const handleOpenModal = () => {
        setIsOpen(true);
    };

    const handleCloseModal = () => {
        setIsOpen(false);
    };

    return (
        <div className="bg-white rounded-lg shadow-md p-4 cursor-pointer hover:shadow-lg transition-shadow duration-200" onClick={handleOpenModal}>

            <img src={vehiculo.image} alt={vehiculo.description} className="w-full h-48 object-cover rounded-lg mb-4" />
            <h3 className="text-lg font-semibold mb-2">{vehiculo.description}</h3>
            <p className="text-gray-600">Modelo: {vehiculo.model}</p>
            <p className="text-gray-600">Combustible: {vehiculo.fuel_type}</p>
            <ModalVehiculo vehiculo={vehiculo} isOpen={isOpen} onClose={handleCloseModal} />
        </div>
    );
}
