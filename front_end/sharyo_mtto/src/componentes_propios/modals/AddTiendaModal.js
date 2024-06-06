"use client";
import { useState } from 'react';

const AddTiendaModal = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [store, setStore] = useState({
        name: '',
        phone: '',
        mobil: '',
        email: '',
        country: '',
        state: '',
        city: '',
        address: '',
    });

    const openModal = () => setIsOpen(true);
    const closeModal = () => setIsOpen(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setStore({ ...store, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(store);
        closeModal();
    };

    return (
        <>
            <button
                onClick={openModal}
                className="bg-purple-500 text-white p-2 rounded"
            >
                Añadir Tienda
            </button>
            {isOpen && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                    <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md relative">
                        <h2 className="text-2xl font-semibold mb-4">Añadir Tienda</h2>
                        <form onSubmit={handleSubmit}>
                            <div className="grid gap-4">
                                <div className="flex flex-col">
                                    <label htmlFor="name" className="mb-1">Nombre</label>
                                    <input id="name" name="name" type="text" value={store.name} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="phone" className="mb-1">Teléfono</label>
                                    <input id="phone" name="phone" type="text" value={store.phone} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="mobil" className="mb-1">Móvil</label>
                                    <input id="mobil" name="mobil" type="text" value={store.mobil} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="email" className="mb-1">Correo Electrónico</label>
                                    <input id="email" name="email" type="email" value={store.email} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="country" className="mb-1">País</label>
                                    <input id="country" name="country" type="text" value={store.country} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="state" className="mb-1">Estado</label>
                                    <input id="state" name="state" type="text" value={store.state} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="city" className="mb-1">Ciudad</label>
                                    <input id="city" name="city" type="text" value={store.city} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="address" className="mb-1">Dirección</label>
                                    <input id="address" name="address" type="text" value={store.address} onChange={handleChange} className="border rounded px-3 py-2" />
                                </div>
                                <button type="submit" className="bg-purple-500 text-white rounded px-4 py-2 mt-4">
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

export default AddTiendaModal;
