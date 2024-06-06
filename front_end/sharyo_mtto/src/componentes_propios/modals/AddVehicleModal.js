"use client";
import { useState } from 'react';

const AddVehicleModal = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [vehicle, setVehicle] = useState({
        brand: '',
        model: '',
        mileage: '',
        plate: '',
        photo: null,
    });

    const openModal = () => setIsOpen(true);
    const closeModal = () => setIsOpen(false);

    const handleChange = (e) => {
        const { name, value, files } = e.target;
        if (name === 'photo') {
            setVehicle({ ...vehicle, photo: files[0] });
        } else {
            setVehicle({ ...vehicle, [name]: value });
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(vehicle);
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
                    <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md relative">
                        <h2 className="text-2xl font-semibold mb-4">Agrega un nuevo vehículo</h2>
                        <form onSubmit={handleSubmit}>
                            <div className="grid gap-4">
                                <div className="flex flex-col">
                                    <label htmlFor="brand" className="mb-1">Marca</label>
                                    <select id="brand" name="brand" value={vehicle.brand} onChange={handleChange} className="border rounded px-3 py-2">
                                        <option>Marca del vehiculo</option>
                                    </select>
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="model" className="mb-1">Modelo</label>
                                    <select id="model" name="model" value={vehicle.model} onChange={handleChange} className="border rounded px-3 py-2">
                                        <option>Modelo</option>
                                    </select>
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="mileage" className="mb-1">Kilometraje</label>
                                    <input id="mileage" name="mileage" type="number" value={vehicle.mileage} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Kilometraje del vehiculo" />
                                </div>
                                <div className="flex flex-col">
                                    <label htmlFor="plate" className="mb-1">Numero de placa</label>
                                    <input id="plate" name="plate" type="text" value={vehicle.plate} onChange={handleChange} className="border rounded px-3 py-2" placeholder="Numero de placa del vehiculo" />
                                </div>
                                <div className="flex flex-col ">
                                    <label htmlFor="photo" className="mb-1">Foto del vehiculo</label>
                                    <div className="border-dashed border-2 rounded px-3 py-2 text-center h-48">
                                        <input id="photo" name="photo" type="file" onChange={handleChange} className="hidden" />
                                        <p>haz click aquí para subir o suelta el archivo</p>
                                    </div>
                                </div>
                                <button type="submit" className="bg-red-500 text-white rounded px-4 py-2 mt-4">
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
