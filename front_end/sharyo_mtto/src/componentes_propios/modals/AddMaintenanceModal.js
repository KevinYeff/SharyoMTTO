'use client';
import { useState } from 'react';

const AddMaintenanceModal = ({ session, userId }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [maintenance, setMaintenance] = useState({
        name: '',
        start_date: '',
        finish_date: '',
        responsable: '',
        fail_detected: '',
        vehicle: '',
        mtto_type: 'CORRECTIVO'
    });
    const [errors, setErrors] = useState({});

    const openModal = () => setIsOpen(true);
    const closeModal = () => setIsOpen(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setMaintenance({ ...maintenance, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newErrors = {};

        // Validate fields
        if (!maintenance.name) newErrors.name = 'Este campo es requerido.';
        if (!maintenance.start_date) newErrors.start_date = 'Este campo es requerido.';
        if (!maintenance.finish_date) newErrors.finish_date = 'Este campo es requerido.';
        if (!maintenance.responsable) newErrors.responsable = 'Este campo es requerido.';
        if (!maintenance.fail_detected) newErrors.fail_detected = 'Este campo es requerido.';
        if (!maintenance.vehicle) newErrors.vehicle = 'Este campo es requerido.';

        // Check if there are errors
        if (Object.keys(newErrors).length > 0) {
            setErrors(newErrors);
            return;
        }

        const payload = {
            ...maintenance,
            vehicle: parseInt(maintenance.vehicle),
        };
        const res = await fetch('http://127.0.0.1:8000/work_order/add_mtto/', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${session}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        if (res.ok) {
            // If response is OK, refresh the page
            window.location.reload();
        } else {
            // Handle error
            const data = await res.json();
            console.error('Error:', data);
        }
        closeModal();
    };

    return (
        <>
            <button
                onClick={openModal}
                className="w-48 bg-[#0f172a] text-[#f8fafc] hover:bg-blue-500 transition-colors px-4 py-2 rounded"
            >
                Agregar Mantenimiento
            </button>
            {isOpen && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                    <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-4xl relative">
                        <h2 className="text-2xl font-semibold mb-4">Agregar Mantenimiento</h2>
                        <form onSubmit={handleSubmit}>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="flex flex-col">
                                    <label htmlFor="name" className="mb-1">Nombre</label>
                                    <input id="name" name="name" value={maintenance.name} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Nombre del mantenimiento" />
                                    {errors.name && <span className="text-red-500">{errors.name}</span>}
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="start_date" className="mb-1">Fecha de Inicio</label>
                                    <input id="start_date" name="start_date" value={maintenance.start_date} onChange={handleChange} type="datetime-local" className="border rounded px-3 py-2" placeholder="Fecha de Inicio" />
                                    {errors.start_date && <span className="text-red-500">{errors.start_date}</span>}
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="finish_date" className="mb-1">Fecha de Fin</label>
                                    <input id="finish_date" name="finish_date" value={maintenance.finish_date} onChange={handleChange} type="datetime-local" className="border rounded px-3 py-2" placeholder="Fecha de Fin" />
                                    {errors.finish_date && <span className="text-red-500">{errors.finish_date}</span>}
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="responsable" className="mb-1">Responsable</label>
                                    <input id="responsable" name="responsable" value={maintenance.responsable} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Responsable" />
                                    {errors.responsable && <span className="text-red-500">{errors.responsable}</span>}
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="fail_detected" className="mb-1">Falla Detectada</label>
                                    <input id="fail_detected" name="fail_detected" value={maintenance.fail_detected} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Falla Detectada" />
                                    {errors.fail_detected && <span className="text-red-500">{errors.fail_detected}</span>}
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="vehicle" className="mb-1">Vehículo</label>
                                    <input id="vehicle" name="vehicle" type="number" value={maintenance.vehicle} onChange={handleChange} className="border rounded px-3 py-2" placeholder="ID del Vehículo" />
                                    {errors.vehicle && <span className="text-red-500">{errors.vehicle}</span>}
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="mtto_type" className="mb-1">Tipo de Mantenimiento</label>
                                    <select id="mtto_type" name="mtto_type" value={maintenance.mtto_type} onChange={handleChange} className="border rounded px-3 py-2">
                                        <option value="CORRECTIVO">CORRECTIVO</option>
                                        <option value="PREVENTIVO">PREVENTIVO</option>
                                    </select>
                                </div>
                            </div>
                            <div className="flex justify-end mt-4">
                                <button type="button" onClick={closeModal} className="bg-gray-500 text-white rounded px-4 py-2 mr-2">
                                    Cancelar
                                </button>
                                <button type="submit" className="bg-blue-500 text-white rounded px-4 py-2">
                                    Agregar
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            )}
        </>
    );
};

export default AddMaintenanceModal;
