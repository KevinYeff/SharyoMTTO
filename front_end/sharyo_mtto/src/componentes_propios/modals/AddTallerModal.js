"use client";
import { useState } from 'react';

const AddTallerModal = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [workshop, setWorkshop] = useState({
        name: '',
        phone: '',
        mobil: '',
        email: '',
        country: '',
        state: '',
        city: '',
        address: '',
        specialization: [],
    });

    const openModal = () => setIsOpen(true);
    const closeModal = () => setIsOpen(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setWorkshop({ ...workshop, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(workshop);
        closeModal();
    };

    return (
        <>
            <button
                onClick={openModal}
                className="bg-blue-500 text-white p-2 rounded"
            >
                Añadir Taller
            </button>
            {isOpen && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                    <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md relative">
                        <h2 className="text-2xl font-semibold mb-4">Añadir Taller</h2>
                        <form onSubmit={handleSubmit}>
                            <div className="grid gap-4">
                                <div className="flex flex-col">
                                    <label htmlFor="name" className="mb-1">Nombre</label>
                                    <input id="name" name="name" type="text" value={workshop.name} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="phone" className="mb-1">Teléfono</label>
                                    <input id="phone" name="phone" type="text" value={workshop.phone} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="mobil" className="mb-1">Móvil</label>
                                    <input id="mobil" name="mobil" type="text" value={workshop.mobil} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="email" className="mb-1">Correo Electrónico</label>
                                    <input id="email" name="email" type="email" value={workshop.email} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="country" className="mb-1">País</label>
                                    <input id="country" name="country" type="text" value={workshop.country} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="state" className="mb-1">Estado</label>
                                    <input id="state" name="state" type="text" value={workshop.state} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="city" className="mb-1">Ciudad</label>
                                    <input id="city" name="city" type="text" value={workshop.city} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="address" className="mb-1">Dirección</label>
                                    <input id="address" name="address" type="text" value={workshop.address} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="specialization" className="mb-1">Especialización</label>
                                    <select id="specialization" name="specialization" multiple value={workshop.specialization} onChange={handleChange} className="border rounded px-3 py-2">
                                        <option value="especializacion1">Especialización 1</option>
                                        <option value="especializacion2">Especialización 2</option>
                                    </select>
                                </div>
                                <button type="submit" className="bg-blue-500 text-white rounded px-4 py-2 mt-4">
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

export default AddTallerModal;
