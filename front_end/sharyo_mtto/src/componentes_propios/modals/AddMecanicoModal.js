"use client";
import { useState } from 'react';

const AddMecanicoModal = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [mechanic, setMechanic] = useState({
        name: '',
        last_name: '',
        phone: '',
        mobil: '',
        email: '',
        workshop: '',
        country: '',
        state: '',
        city: '',
        specialization: [],
    });

    const openModal = () => setIsOpen(true);
    const closeModal = () => setIsOpen(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setMechanic({ ...mechanic, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(mechanic);
        closeModal();
    };

    return (
        <>
            <button
                onClick={openModal}
                className="bg-green-500 text-white p-2 rounded"
            >
                Añadir Mecánico
            </button>
            {isOpen && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                    <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md relative">
                        <h2 className="text-2xl font-semibold mb-4">Añadir Mecánico</h2>
                        <form onSubmit={handleSubmit}>
                            <div className="grid gap-4">
                                <div className="flex flex-col">
                                    <label htmlFor="name" className="mb-1">Nombre</label>
                                    <input id="name" name="name" type="text" value={mechanic.name} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="last_name" className="mb-1">Apellido</label>
                                    <input id="last_name" name="last_name" type="text" value={mechanic.last_name} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="phone" className="mb-1">Teléfono</label>
                                    <input id="phone" name="phone" type="text" value={mechanic.phone} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="mobil" className="mb-1">Móvil</label>
                                    <input id="mobil" name="mobil" type="text" value={mechanic.mobil} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="email" className="mb-1">Correo Electrónico</label>
                                    <input id="email" name="email" type="email" value={mechanic.email} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="workshop" className="mb-1">Taller</label>
                                    <select id="workshop" name="workshop" value={mechanic.workshop} onChange={handleChange} className="border rounded px-3 py-2">
                                        <option value="">Seleccione un taller</option>
                                        <option value="taller1">Taller 1</option>
                                        <option value="taller2">Taller 2</option>
                                    </select>
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="country" className="mb-1">País</label>
                                    <input id="country" name="country" type="text" value={mechanic.country} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="state" className="mb-1">Estado</label>
                                    <input id="state" name="state" type="text" value={mechanic.state} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="city" className="mb-1">Ciudad</label>
                                    <input id="city" name="city" type="text" value={mechanic.city} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="specialization" className="mb-1">Especialización</label>
                                    <select id="specialization" name="specialization" multiple value={mechanic.specialization} onChange={handleChange} className="border rounded px-3 py-2">
                                        <option value="especializacion1">Especialización 1</option>
                                        <option value="especializacion2">Especialización 2</option>
                                    </select>
                                </div>
                                <button type="submit" className="bg-green-500 text-white rounded px-4 py-2 mt-4">
                                    Guardar
                                </button>
                            </div>
                        </form>
                        <button onClick={closeModal} className="absolute top-4 right-4 text-gray-500 hover:text-gray-800">
                            &times;
                        </button>
                    </div>
                </div>
            )}
        </>
    );
};

export default AddMecanicoModal;
