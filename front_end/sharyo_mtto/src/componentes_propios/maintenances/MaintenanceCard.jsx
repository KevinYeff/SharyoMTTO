'use client';
import { useState } from 'react';
import MaintenanceDetailModal from './MaintenanceDetailModal';
import { format } from 'date-fns';

const MaintenanceCard = ({ maintenance }) => {
    const [isDetailOpen, setIsDetailOpen] = useState(false);

    const openDetailModal = () => setIsDetailOpen(true);
    const closeDetailModal = () => setIsDetailOpen(false);

    const currentDate = new Date();
    const endDate = new Date(maintenance.finish_date);
    const startDate = new Date(maintenance.start_date);

    const dateFormat = 'dd/MM/yyyy HH:mm';
    const formattedStartDate = format(startDate, dateFormat);
    const formattedEndDate = format(endDate, dateFormat);

    let cardColor = 'bg-green-200';
    if (endDate < currentDate) {
        cardColor = 'bg-red-200';
    } else if ((endDate - currentDate) / (1000 * 60 * 60 * 24) <= 7) {
        cardColor = 'bg-yellow-200';
    }

    return (
        <div className={`border rounded-lg p-4 shadow-md ${cardColor}`}>
            <h2 className="text-xl font-bold">{maintenance.name}</h2>
            <p><strong>Fecha de Inicio:</strong> {formattedStartDate}</p>
            <p><strong>Fecha de Fin:</strong> {formattedEndDate}</p>
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
