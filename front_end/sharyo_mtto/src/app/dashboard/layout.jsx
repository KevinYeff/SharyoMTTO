import SideNav from "@/componentes_propios/dashboard/dashboard";

export default function Layout({ children }) {
    return (
        <div className="flex h-screen flex-col md:flex-row">
            <div className="flex-none md:w-64">
                <SideNav />
            </div>
            <div className="flex-grow p-4 md:p-6">
                <div className="bg-gray-100 h-full w-full mx-auto rounded-lg p-5 shadow-md">
                    {children}
                </div>
            </div>
        </div>
    );
}
