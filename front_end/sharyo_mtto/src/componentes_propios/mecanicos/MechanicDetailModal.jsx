'use client';
const MechanicDetailModal = ({ mecanico, onClose }) => {
    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
            <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-2xl relative">
                <button
                    onClick={onClose}
                    className="absolute top-2 right-2 bg-gray-200 hover:bg-gray-300 rounded-full p-2"
                >
                    X
                </button>
                <h2 className="text-2xl font-bold mb-4">{mecanico.name} {mecanico.last_name}</h2>
                <div className="mb-4">
                    <p><strong>Email:</strong> {mecanico.email}</p>
                    <p><strong>Teléfono:</strong> {mecanico.phone}</p>
                    <p><strong>Móvil:</strong> {mecanico.mobil}</p>
                    <p><strong>Taller:</strong> {mecanico.workshop}</p>
                    <p><strong>País:</strong> {mecanico.country}</p>
                    <p><strong>Estado:</strong> {mecanico.state}</p>
                    <p><strong>Ciudad:</strong> {mecanico.city}</p>
                    <p><strong>Libreta de contactos:</strong> {mecanico.contact_book}</p>
                    <div>
                        <strong>Especializaciones:</strong>
                        <ul>
                            {mecanico.specializations.map((spec, index) => (
                                <li key={index}>{spec.specialization}</li>
                            ))}
                        </ul>
                    </div>
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

export default MechanicDetailModal;
