
import { getVehiculos } from '@/actions/vehiculos';
import CardVehiculo from '@/componentes_propios/vehiculos/CardVehiculo';
import AddVehicleModal from '@/componentes_propios/modals/AddVehicleModal';
import { getCookies } from '@/actions/getCookies';
export default async function Vehiculos() {
    const vehiculos = await getVehiculos();
    const { session, userId } = await getCookies();
    return (
        <div>
            <div className=" pb-4 flex mx-10 justify-between items-center ">
                <h2 className=" text-3xl font-semibold mb-4">Tus vehiculos</h2>
                <AddVehicleModal session={session} userId={userId} />



            </div>
            <div className=" grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-4">
                {vehiculos.map((vehiculo) => (
                    <CardVehiculo key={vehiculo.plate} vehiculo={vehiculo} />
                ))}
            </div>
        </div>
    );
}
