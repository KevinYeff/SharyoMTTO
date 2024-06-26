'use client';
import React from 'react';
import Image from 'next/image';

export default function ModalVehiculo({ vehiculo, isOpen, onClose }) {
    if (!isOpen) return null;

    return (
        <div
            className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50"
            onClick={onClose}
        >
            <div
                className="bg-white p-6 rounded-lg max-w-lg w-full relative"
                onClick={(e) => e.stopPropagation()}
            >
                <button
                    className="absolute top-2 right-2 text-gray-500 hover:text-gray-700"
                    onClick={onClose}
                >
                    &times;
                </button>
                <h2 className="text-2xl font-semibold mb-4">{vehiculo.description}</h2>
                <div className="w-full h-64 mb-4 overflow-hidden rounded-lg">
                    <Image
                        src={`http://127.0.0.1:8000/${vehiculo.image}`}
                        alt={vehiculo.description}
                        layout="responsive"
                        width={300}
                        height={200}
                        className="object-contain w-full h-full"
                    />
                </div>
                <p className="text-gray-700 mb-2">Placa: {vehiculo.plate}</p>
                <p className="text-gray-700 mb-2">Modelo: {vehiculo.model}</p>
                <p className="text-gray-700 mb-2">Combustible: {vehiculo.fuel_type}</p>
                <p className="text-gray-700 mb-2">Marca: {vehiculo.brand}</p>
                <p className="text-gray-700 mb-2">Categoría: {vehiculo.vehicle_category}</p>
                <p className="text-gray-700 mb-2">Tipo: {vehiculo.vehicle_type}</p>
                <p className="text-gray-700 mb-2">Usuario: {vehiculo.user}</p>
            </div>
        </div>
    );
}
