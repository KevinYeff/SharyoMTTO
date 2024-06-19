'use client';
const MaintenanceDetailModal = ({ maintenance, onClose }) => {
    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
            <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-2xl relative">
                <button
                    onClick={onClose}
                    className="absolute top-2 right-2 bg-gray-200 hover:bg-gray-300 rounded-full p-2"
                >
                    X
                </button>
                <h2 className="text-2xl font-bold mb-4">{maintenance.name}</h2>
                <div className="mb-4">
                    <p><strong>Fecha de Inicio:</strong> {maintenance.start_date}</p>
                    <p><strong>Fecha de Fin:</strong> {maintenance.finish_date}</p>
                    <p><strong>Responsable:</strong> {maintenance.responsable}</p>
                    <p><strong>Falla Detectada:</strong> {maintenance.fail_detected}</p>
                    <p><strong>Vehículo:</strong> {maintenance.vehicle}</p>
                    <p><strong>Tipo de Mantenimiento:</strong> {maintenance.mtto_type}</p>
                </div>
                <button
                    onClick={onClose}
                    className="mt-4 bg-gray-500 text-white px-4 py-2 rounded"
                >
                    Cerrar
                </button>
            </div>
        </div>
    );
};

export default MaintenanceDetailModal;
