"use client";
import { useState } from 'react';

const AddStoreModal = ({ session }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [store, setStore] = useState({
        specializations: [{ specialization: '' }],
        name: '',
        phone: '',
        mobil: '',
        email: '',
        address: '',
        country: 0,
        state: 0,
        city: 0
    });
    const [errors, setErrors] = useState({});

    const openModal = () => setIsOpen(true);
    const closeModal = () => setIsOpen(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setStore({ ...store, [name]: value });
    };

    const handleSpecializationChange = (index, e) => {
        const { value } = e.target;
        const updatedSpecializations = [...store.specializations];
        updatedSpecializations[index].specialization = value;
        setStore({ ...store, specializations: updatedSpecializations });
    };

    const addSpecialization = () => {
        setStore({
            ...store,
            specializations: [...store.specializations, { specialization: '' }]
        });
    };

    const removeSpecialization = (index) => {
        const updatedSpecializations = store.specializations.filter((_, i) => i !== index);
        setStore({ ...store, specializations: updatedSpecializations });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newErrors = {};

        // Validate specializations
        store.specializations.forEach((spec, index) => {
            if (!spec.specialization) {
                newErrors[`specialization_${index}`] = 'Este campo no puede estar vacío.';
            }
        });

        // Check if there are errors
        if (Object.keys(newErrors).length > 0) {
            setErrors(newErrors);
            return;
        }

        const payload = {
            ...store
        };
        const res = await fetch('http://localhost:8000/contact_book/add_store/', {
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
                Agrega una nueva tienda
            </button>
            {isOpen && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                    <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-4xl relative">
                        <h2 className="text-2xl font-semibold mb-4">Agrega una nueva tienda</h2>
                        <form onSubmit={handleSubmit}>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="flex flex-col">
                                    <label htmlFor="name" className="mb-1">Nombre</label>
                                    <input id="name" name="name" value={store.name} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Nombre de la tienda" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="phone" className="mb-1">Teléfono</label>
                                    <input id="phone" name="phone" value={store.phone} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Teléfono de la tienda" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="mobil" className="mb-1">Móvil</label>
                                    <input id="mobil" name="mobil" value={store.mobil} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Móvil de la tienda" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="email" className="mb-1">Email</label>
                                    <input id="email" name="email" value={store.email} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Email de la tienda" />
                                </div>
                                <div className="flex flex-col col-span-2">
                                    <label htmlFor="address" className="mb-1">Dirección</label>
                                    <input id="address" name="address" value={store.address} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Dirección de la tienda" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="country" className="mb-1">País</label>
                                    <input id="country" name="country" value={store.country} onChange={handleChange} className="border rounded px-3 py-2" placeholder="País de la tienda" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="state" className="mb-1">Estado</label>
                                    <input id="state" name="state" value={store.state} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Estado de la tienda" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="city" className="mb-1">Ciudad</label>
                                    <input id="city" name="city" value={store.city} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Ciudad de la tienda" />
                                </div>
                                <div className="flex flex-col col-span-2">
                                    <label className="mb-1">Especializaciones</label>
                                    {store.specializations.map((spec, index) => (
                                        <div key={index} className="flex items-center mb-2">
                                            <input
                                                name={`specialization_${index}`}
                                                value={spec.specialization}
                                                onChange={(e) => handleSpecializationChange(index, e)}
                                                className={`border rounded px-3 py-2 flex-grow ${errors[`specialization_${index}`] ? 'border-red-500' : ''}`}
                                                placeholder="Especialización"
                                            />
                                            <button
                                                type="button"
                                                onClick={() => removeSpecialization(index)}
                                                className="ml-2 bg-red-500 text-white rounded px-2 py-1"
                                            >
                                                -
                                            </button>
                                        </div>
                                    ))}
                                    <button
                                        type="button"
                                        onClick={addSpecialization}
                                        className="bg-green-500 text-white rounded px-2 py-1 mt-2"
                                    >
                                        + Agregar Especialización
                                    </button>
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

export default AddStoreModal;
