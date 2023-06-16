import React, { ReactElement } from 'react';
import Header from './Header';
import Sidebar from './Sidebar';

type PageShellProps = {
    children: ReactElement;
}

function PageShell({ children }: PageShellProps) {
    return (
        <div >

            <Header />
            <div className='row'>
                <div className='col-md-2'>
                    <Sidebar />
                </div>
                <div className='col-md-10'>
                    {children}
                </div>
            </div>
        </div>
    );
}

export default PageShell;
