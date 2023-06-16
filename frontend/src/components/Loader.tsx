import React, { useState } from 'react';
//@ts-ignore
import { BounceLoader, ClipLoader } from 'react-spinners';
import './styles/Loader.scss'


function Loader() {
    const [progressCounter, setProgressCounter] = useState(0)
    const stepProgressArr = ['Fixing images...', 'Fixing constrast...', 'Fixing tags...']

    const [progress, setProgress ]= useState(1)

    setTimeout(() => {
        if (progressCounter < stepProgressArr.length - 1) {
            setProgressCounter(progressCounter + 1)
        }
        if(progress < 10){
            setProgress(progress +1)
        }
    }, 2000)

    return (
        <div className="loader-container">
            <div className="fetching-loader-container">
                <ClipLoader color="#0d6efd" size={75} speedMultiplier={0.5} className={"loader-circle"} />
                <div className="error-loader-percentage"> {10 * progress + '%'}</div>
                <div className="error-status">
                    <div className='loader-text'>{stepProgressArr[progressCounter]}</div>
                </div>
            </div>
        </div>
    )
}

export default Loader;