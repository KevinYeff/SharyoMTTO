'use client';
import { useState } from 'react';
import MaintenanceDetailModal from './MaintenanceDetailModal';

const MaintenanceCard = ({ maintenance }) => {
    const [isDetailOpen, setIsDetailOpen] = useState(false);

    const openDetailModal = () => setIsDetailOpen(true);
    const closeDetailModal = () => setIsDetailOpen(false);

    return (
        <div className="border rounded-lg p-4 shadow-md">
            <h2 className="text-xl font-bold">{maintenance.name}</h2>
            <p><strong>Fecha de Inicio:</strong> {maintenance.start_date}</p>
            <p><strong>Fecha de Fin:</strong> {maintenance.finish_date}</p>
            <p><strong>Responsable:</strong> {maintenance.responsable}</p>
            <p><strong>Falla Detectada:</strong> {maintenance.fail_detected}</p>
            <button
                onClick={openDetailModal}
                className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
            >
                Ver detalles
            </button>
            {isDetailOpen && <MaintenanceDetailModal maintenance={maintenance} onClose={closeDetailModal} />}
        </div>
    );
};

export default MaintenanceCard;
