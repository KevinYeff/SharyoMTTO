import { getStores } from '@/actions/stores';
import CardStore from '@/componentes_propios/stores/CardStore';
import AddStoreModal from '@/componentes_propios/modals/AddStoreModal';
import { getCookies } from '@/actions/getCookies';

export default async function Stores() {
    const stores = await getStores();
    const { session } = await getCookies();

    return (
        <div>
            <div className="pb-4 flex mx-10 justify-between items-center">
                <h2 className="text-3xl font-semibold mb-4">Tus Tiendas</h2>
                <AddStoreModal session={session} />
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-4">
                {stores.map((store) => (
                    <CardStore key={store.id} store={store} />
                ))}
            </div>
        </div>
    );
}
