import React, { useState } from 'react';
import { ClipLoader } from 'react-spinners';
import './styles/FetchingErrorsLoader.scss'

function FetchingErrorsLoader() {

    const [progressCounter, setProgressCounter] = useState(0)
    const [progress, setProgress ]= useState(1)
    const stepProgressArr = ['Parsing HTML...', 'Fetching image errors...', 'Analysing color contrast issues... ', 'Creating image description suggestions...', 'Generating color suggestions... ']

    setTimeout(() => {
        if (progressCounter < stepProgressArr.length - 1) {
            setProgressCounter(progressCounter + 1)
        }
        if(progress < 9){
            setProgress(progress +1)
        }
    }, 4000)

    return (
        <div className="loader-container">
            <div className="fetching-loader-container">
                <ClipLoader color="#0d6efd" size={85} speedMultiplier={0.5} className={"loader-circle"} />
                <div className="error-loader-percentage"> {10 * progress + '%'}</div> 
                <div className="error-status">
                    <div className='loader-text'>{stepProgressArr[progressCounter]}</div>
                </div>
            </div>
        </div>
    )
}

export default FetchingErrorsLoader;