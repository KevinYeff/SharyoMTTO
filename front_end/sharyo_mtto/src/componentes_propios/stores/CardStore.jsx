'use client';
import { useState } from 'react';
import StoreDetailModal from './StoreDetailModal';

const CardStore = ({ store }) => {
    const [isDetailOpen, setIsDetailOpen] = useState(false);

    const openDetailModal = () => setIsDetailOpen(true);
    const closeDetailModal = () => setIsDetailOpen(false);

    return (
        <div className="border rounded-lg p-4 shadow-md">
            <h2 className="text-xl font-bold">{store.name}</h2>
            <p><strong>Email:</strong> {store.email}</p>
            <p><strong>Teléfono:</strong> {store.phone}</p>
            <p><strong>Móvil:</strong> {store.mobil}</p>
            <button
                onClick={openDetailModal}
                className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
            >
                Ver detalles
            </button>
            {isDetailOpen && <StoreDetailModal store={store} onClose={closeDetailModal} />}
        </div>
    );
};

export default CardStore;
