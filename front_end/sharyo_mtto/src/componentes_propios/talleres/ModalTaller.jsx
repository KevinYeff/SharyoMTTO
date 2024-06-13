'use client';
import React from 'react';

export default function ModalTaller({ taller, isOpen, onClose }) {
    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50" onClick={onClose}>
            <div className="bg-white p-6 rounded-lg max-w-lg w-full relative" onClick={(e) => e.stopPropagation()}>
                <button className="absolute top-2 right-2 text-gray-500 hover:text-gray-700" onClick={onClose}>
                    &times;
                </button>
                <h2 className="text-2xl font-semibold mb-4">{taller.name}</h2>
                <p className="text-gray-700 mb-2">Teléfono: {taller.phone}</p>
                <p className="text-gray-700 mb-2">Móvil: {taller.mobil}</p>
                <p className="text-gray-700 mb-2">Email: {taller.email}</p>
                <p className="text-gray-700 mb-2">Dirección: {taller.address}</p>
                <p className="text-gray-700 mb-2">País: {taller.country}</p>
                <p className="text-gray-700 mb-2">Estado: {taller.state}</p>
                <p className="text-gray-700 mb-2">Ciudad: {taller.city}</p>
                <p className="text-gray-700 mb-2">Libreta de contactos: {taller.contact_book}</p>
                <h3 className="text-xl font-semibold mt-4 mb-2">Especializaciones:</h3>
                <ul className="list-disc list-inside">
                    {taller.specializations.map(spec => (
                        <li key={spec.id} className="text-gray-700">{spec.specialization}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
}
