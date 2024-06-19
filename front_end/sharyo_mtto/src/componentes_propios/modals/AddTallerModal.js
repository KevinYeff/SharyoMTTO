"use client";
import { useState } from 'react';

const AddTallerModal = ({ session, userId }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [taller, setTaller] = useState({
        specializations: [{ specialization: '' }],
        name: '',
        phone: '',
        mobil: '',
        email: '',
        workshop: 0,
        country: 0,
        state: 0,
        city: 0,
        contact_book: 0,
    });
    const [errors, setErrors] = useState({});

    const openModal = () => setIsOpen(true);
    const closeModal = () => setIsOpen(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setTaller({ ...taller, [name]: value });
    };

    const handleSpecializationChange = (index, e) => {
        const { value } = e.target;
        const updatedSpecializations = [...taller.specializations];
        updatedSpecializations[index].specialization = value;
        setTaller({ ...taller, specializations: updatedSpecializations });
    };

    const addSpecialization = () => {
        setTaller({
            ...taller,
            specializations: [...taller.specializations, { specialization: '' }]
        });
    };

    const removeSpecialization = (index) => {
        const updatedSpecializations = taller.specializations.filter((_, i) => i !== index);
        setTaller({ ...taller, specializations: updatedSpecializations });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newErrors = {};

        // Validate specializations
        taller.specializations.forEach((spec, index) => {
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
            user: userId,
            ...taller
        };
        const res = await fetch('http://localhost:8000/contact_book/add_workshop/', {
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
                Agrega un nuevo taller
            </button>
            {isOpen && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                    <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-4xl relative">
                        <h2 className="text-2xl font-semibold mb-4">Agrega un nuevo taller</h2>
                        <form onSubmit={handleSubmit}>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="flex flex-col">
                                    <label htmlFor="name" className="mb-1">Nombre</label>
                                    <input id="name" name="name" value={taller.name} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Nombre del taller" />
                                </div>

                                <div className="flex flex-col">
                                    <label htmlFor="phone" className="mb-1">Teléfono</label>
                                    <input id="phone" name="phone" value={taller.phone} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Teléfono del taller" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="mobil" className="mb-1">Móvil</label>
                                    <input id="mobil" name="mobil" value={taller.mobil} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Móvil del taller" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="email" className="mb-1">Email</label>
                                    <input id="email" name="email" value={taller.email} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Email del taller" />
                                </div>

                                <div className="flex flex-col">
                                    <label htmlFor="country" className="mb-1">País</label>
                                    <input id="country" name="country" value={taller.country} onChange={handleChange} className="border rounded px-3 py-2" placeholder="País del taller" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="state" className="mb-1">Estado</label>
                                    <input id="state" name="state" value={taller.state} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Estado del taller" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="city" className="mb-1">Ciudad</label>
                                    <input id="city" name="city" value={taller.city} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Ciudad del taller" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="contact_book" className="mb-1">Libreta de contactos</label>
                                    <input id="contact_book" name="contact_book" value={taller.contact_book} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Libreta de contactos" />
                                </div>
                                <div className="flex flex-col col-span-2">
                                    <label className="mb-1">Especializaciones</label>
                                    {taller.specializations.map((spec, index) => (
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
                                                className="bg-red-500 text-white rounded px-3 py-2 ml-2"
                                            >
                                                -
                                            </button>
                                            {errors[`specialization_${index}`] && (
                                                <span className="text-red-500 text-sm ml-2">{errors[`specialization_${index}`]}</span>
                                            )}
                                        </div>
                                    ))}
                                    <button
                                        type="button"
                                        onClick={addSpecialization}
                                        className="bg-blue-500 text-white rounded px-4 py-2 mt-2"
                                    >
                                        + Agregar Especialización
                                    </button>
                                </div>
                                <button type="submit" className="bg-red-500 text-white rounded px-4 py-2 mt-4 col-span-2">
                                    + Agregar Taller
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
