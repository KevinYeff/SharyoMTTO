'use client';
import { useState } from 'react';
import ModalVehiculo from './ModalVehiculo';
import Image from 'next/image';

export default function CardVehiculo({ vehiculo }) {
    const [isOpen, setIsOpen] = useState(false);

    const handleOpenModal = () => {
        setIsOpen(true);
    };

    const handleCloseModal = () => {
        setIsOpen(false);
    };

    return (
        <div
            className="bg-white rounded-lg shadow-md p-4 cursor-pointer hover:shadow-lg transition-shadow duration-200"
            onClick={handleOpenModal}
        >
            <div className="w-full h-48 mb-4 overflow-hidden rounded-lg">
                <Image
                    src={`http://127.0.0.1:8000/${vehiculo.image}`}
                    alt={vehiculo.description}
                    layout="responsive"
                    width={300}
                    height={200}
                    className="object-contain w-full h-full"
                />
            </div>
            <h3 className="text-lg font-semibold mb-2">{vehiculo.description}</h3>
            <p className="text-gray-600">Modelo: {vehiculo.model}</p>
            <p className="text-gray-600">Combustible: {vehiculo.fuel_type}</p>
            <ModalVehiculo vehiculo={vehiculo} isOpen={isOpen} onClose={handleCloseModal} />
        </div>
    );
}
