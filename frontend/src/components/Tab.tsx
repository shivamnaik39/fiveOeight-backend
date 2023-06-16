import React, { ReactElement } from 'react';

type TabProps = {
    children: ReactElement;
    heading: string;
    id: string;
}

function Tab({ children, heading, id }: TabProps) {
    return (
        <div className="tab-pane active" role="tabpanel" id={id}>
            {children}
        </div>
    );
}

export default Tab;
