import React from 'react';
import { API_URL } from '../constant';
import './styles/StepThree.scss';

import Tab from './Tab';

function StepThree() {

    const handleDownload = async () => {
        const response = await fetch(`${API_URL}/download_zip`);
        const blob = await response.blob();
        const url = window.URL.createObjectURL(new Blob([blob]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'fixed_folder.zip');
        document.body.appendChild(link);
        link.click();
        link.parentNode?.removeChild(link);
    }

    return (

        <Tab id="step4" heading="Step 3">
            <>
                <div className='DownloadPanel'>
                    <div className="row">
                        <div className='col'>
                            <div className='DoneIcon'><i className="bi bi-check-circle-fill"></i></div>
                            <div className='DonelargeTxt'>Congratulations!</div>
                            <div className='DonesmallTxt'>you have fixed maximum accessibility issues</div>
                        </div>
                    </div>
                    <div className="row">
                        <div className='col'>
                            <button type="button" className="btn" onClick={handleDownload}>
                                Download fixed folder
                            </button><div><button type="button" className="btn btn-sm" onClick={async() => {
                                const errorData = await fetch(`${API_URL}/suggest_changes`, {
                                    method: "GET"
                                  })
                                  const contrastImageErrorData = await errorData.json();
                                const jsn = JSON.stringify(contrastImageErrorData);
                                const blob = new Blob([jsn], { type: 'application/json' });

                                const url = window.URL.createObjectURL(blob);
                                const link = document.createElement('a');
                                link.href = url;
                                link.setAttribute('download', 'log.json');
                                document.body.appendChild(link);
                                link.click();
                                link.parentNode?.removeChild(link);
                            }}>
                                Download log file
                            </button></div>

                        </div>
                    </div>
                </div>
            </>
        </Tab>
    );

}

export default StepThree;