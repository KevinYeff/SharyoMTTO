'use client';
import { useState } from 'react';

const MileageModal = ({ vehiculo, isOpen, onClose, session }) => {
    const [mileage, setMileage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('mileage', mileage);
        formData.append('date', new Date().toISOString().split('T')[0]);
        formData.append('vehicle', vehiculo.id);

        const res = await fetch('http://localhost:8000/vehicles/mileage_register/', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${session}`,
            },
            body: formData,
        });

        const data = await res.json();
        if (res.ok) {
            alert('Mileage registered successfully');
            window.location.reload();
        } else {
            console.error('Error:', data);
            alert('Failed to register mileage');
        }

        onClose();
    };

    if (!isOpen) return null;

    return (
        <div
            className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
            onClick={onClose}
        >
            <div
                className="bg-white p-4 rounded-lg shadow-lg"
                onClick={(e) => e.stopPropagation()}
            >
                <h2 className="text-xl font-semibold mb-4">Register Mileage for {vehiculo.description}</h2>
                <form onSubmit={handleSubmit}>
                    <div className="mb-4">
                        <label className="block text-gray-700 mb-2" htmlFor="mileage">Mileage</label>
                        <input
                            type="number"
                            id="mileage"
                            value={mileage}
                            onChange={(e) => setMileage(e.target.value)}
                            className="w-full p-2 border border-gray-300 rounded-lg"
                            required
                        />
                    </div>
                    <div className="flex justify-end">
                        <button
                            type="button"
                            onClick={onClose}
                            className="mr-2 px-4 py-2 bg-gray-300 text-gray-700 rounded-lg"
                        >
                            Cancel
                        </button>
                        <button
                            type="submit"
                            className="px-4 py-2 bg-blue-500 text-white rounded-lg"
                        >
                            Register
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default MileageModal;
