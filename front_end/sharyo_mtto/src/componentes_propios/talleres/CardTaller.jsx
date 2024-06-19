'use client';
import { useState } from 'react';
import ModalTaller from './ModalTaller';

export default function CardTaller({ taller }) {
    const [isOpen, setIsOpen] = useState(false);

    const handleOpenModal = () => {
        setIsOpen(true);
    };

    const handleCloseModal = () => {
        setIsOpen(false);
    };

    return (
        <div className="bg-white rounded-lg shadow-md p-4 cursor-pointer hover:shadow-lg transition-shadow duration-200" onClick={handleOpenModal}>
            <h3 className="text-lg font-semibold mb-2">{taller.name}</h3>
            <p className="text-gray-600">Teléfono: {taller.phone}</p>
            <p className="text-gray-600">Móvil: {taller.mobil}</p>
            <p className="text-gray-600">Email: {taller.email}</p>
            <p className="text-gray-600">Dirección: {taller.address}</p>
            <ModalTaller taller={taller} isOpen={isOpen} onClose={handleCloseModal} />
        </div>
    );
}
