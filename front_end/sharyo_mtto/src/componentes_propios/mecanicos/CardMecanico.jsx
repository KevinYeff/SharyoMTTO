'use client';
import { useState } from 'react';
import MechanicDetailModal from './MechanicDetailModal';

const CardMecanico = ({ mecanico }) => {
    const [isDetailOpen, setIsDetailOpen] = useState(false);

    const openDetailModal = () => setIsDetailOpen(true);
    const closeDetailModal = () => setIsDetailOpen(false);

    return (
        <div className="border rounded-lg p-4 shadow-md">
            <h2 className="text-xl font-bold">{mecanico.name} {mecanico.last_name}</h2>
            <p><strong>Email:</strong> {mecanico.email}</p>
            <p><strong>Teléfono:</strong> {mecanico.phone}</p>
            <p><strong>Móvil:</strong> {mecanico.mobil}</p>
            <button
                onClick={openDetailModal}
                className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
            >
                Ver detalles
            </button>
            {isDetailOpen && <MechanicDetailModal mecanico={mecanico} onClose={closeDetailModal} />}
        </div>
    );
};

export default CardMecanico;
