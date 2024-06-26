import { getMaintenances } from '@/actions/mantenimientos';
import MaintenanceCard from '@/componentes_propios/maintenances/MaintenanceCard';
import AddMaintenanceModal from '@/componentes_propios/modals/AddMaintenanceModal';
import { getCookies } from '@/actions/getCookies';

export default async function Calendario() {
    const maintenances = await getMaintenances();
    const { session, userId } = await getCookies();

    // Sort maintenances from oldest to most recent
    const sortedMaintenances = maintenances.sort((a, b) => new Date(a.start_date) - new Date(b.start_date));

    return (
        <div>
            <div className="pb-4 flex mx-10 justify-between items-center">
                <h2 className="text-3xl font-semibold mb-4">Calendario de Mantenimientos</h2>
                <AddMaintenanceModal session={session} userId={userId} />
            </div>
            <div className="grid grid-cols-1 gap-6 p-4">
                {sortedMaintenances.map((maintenance) => (
                    <MaintenanceCard key={maintenance.id} maintenance={maintenance} />
                ))}
            </div>
        </div>
    );
}
