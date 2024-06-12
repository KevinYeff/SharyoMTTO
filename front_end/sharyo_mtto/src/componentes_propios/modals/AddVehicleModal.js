"use client";
import { useState } from 'react';

const AddVehicleModal = ({ session, userId }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [vehicle, setVehicle] = useState({
        brand: 0,
        model: '',
        description: '',
        fuel_type: 'ELECTRICO',
        vehicle_category: 0,
        vehicle_type: 0,
        plate: '',
        photo: null,
    });
    const [photoPreview, setPhotoPreview] = useState(null);

    const openModal = () => setIsOpen(true);
    const closeModal = () => setIsOpen(false);

    const handleChange = (e) => {
        const { name, value, files } = e.target;
        if (name === 'photo') {
            const file = files[0];
            setVehicle({ ...vehicle, photo: file });
            setPhotoPreview(URL.createObjectURL(file));
        } else {
            setVehicle({ ...vehicle, [name]: value });
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('user', userId);
        for (const key in vehicle) {
            formData.append(key, vehicle[key]);
        }
        const res = await fetch('http://localhost:8000/vehicles/add_vehicle/', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${session}`,
            },
            body: formData,
        });
        const data = await res.json();
        console.log(data);
        closeModal();
    };

    return (
        <>
            <button
                onClick={openModal}
                className="w-48 bg-[#0f172a] text-[#f8fafc] hover:bg-blue-500 transition-colors px-4 py-2 rounded"
            >
                Agrega un nuevo vehículo
            </button>
            {isOpen && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                    <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-4xl relative">
                        <h2 className="text-2xl font-semibold mb-4">Agrega un nuevo vehículo</h2>
                        <form onSubmit={handleSubmit} encType="multipart/form-data">
                            <div className="grid grid-cols-2 gap-4">
                                <div className="flex flex-col">
                                    <label htmlFor="brand" className="mb-1">Marca</label>
                                    <input id="brand" name="brand" value={vehicle.brand} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Marca del vehículo" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="model" className="mb-1">Modelo</label>
                                    <input id="model" name="model" type="number" value={vehicle.model} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Modelo del vehículo" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="description" className="mb-1">Descripción</label>
                                    <input id="description" name="description" value={vehicle.description} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Descripción del vehículo" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="fuel_type" className="mb-1">Tipo de combustible</label>
                                    <select id="fuel_type" name="fuel_type" value={vehicle.fuel_type} onChange={handleChange} className="border rounded px-3 py-2">
                                        <option value="ELECTRICO">Eléctrico</option>
                                        <option value="EXTRA">Extra</option>
                                        <option value="DIESEL">Diesel</option>
                                        <option value="GASOLINA">Gasolina</option>
                                        <option value="GAS">Gas</option>
                                        <option value="HIBRIDO">Híbrido</option>
                                    </select>
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="vehicle_category" className="mb-1">Categoría del vehículo</label>
                                    <input id="vehicle_category" name="vehicle_category" value={vehicle.vehicle_category} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Categoría del vehículo" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="vehicle_type" className="mb-1">Tipo de vehículo</label>
                                    <input id="vehicle_type" name="vehicle_type" value={vehicle.vehicle_type} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Tipo de vehículo" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="plate" className="mb-1">Número de placa</label>
                                    <input id="plate" name="plate" value={vehicle.plate} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Número de placa del vehículo" />
                                </div>
                                <div className="flex flex-col col-span-2">
                                    <label htmlFor="photo" className="mb-1">Foto del vehículo</label>
                                    <div className="border-dashed border-2 rounded px-3 py-2 text-center h-48 flex items-center justify-center relative">
                                        <input id="photo" name="photo" type="file" onChange={handleChange} className="hidden" />
                                        <label htmlFor="photo" className="cursor-pointer">Haz click aquí para subir o suelta el archivo</label>
                                        {photoPreview && (
                                            <img src={photoPreview} alt="Preview" className="absolute inset-0 w-full h-full object-cover rounded" />
                                        )}
                                    </div>
                                </div>
                                <button type="submit" className="bg-red-500 text-white rounded px-4 py-2 mt-4 col-span-2">
                                    + Agrega el nuevo vehículo
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

export default AddVehicleModal;
