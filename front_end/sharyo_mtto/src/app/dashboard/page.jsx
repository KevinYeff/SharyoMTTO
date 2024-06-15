import React from 'react'
import Image from 'next/image'

function Page() {
    return (
        <div className='flex flex-col items-center justify-center h-screen w-screen pr-64'>
            <div> <div className="pb-4 flex mx-10 justify-between items-center">
                <h2 className="text-3xl font-semibold mb-4">Dashboard (Diseño)</h2>

            </div></div>
            <div>            <img
                src="/dashboard.png"
                alt="dashboard"



            />
            </div>

        </div>
    )
}

export default Page
