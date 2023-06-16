import React from 'react';

type ProgressBarProps = {
    progress: number;
}
function ProgressBar({ progress }: ProgressBarProps) {
    const width = 25 * progress + '%'
    return (
        <div className="progress" role="progressbar" aria-label="Animated striped example" aria-valuenow={25 * progress} aria-valuemin={0} aria-valuemax={100}>
            <div className="progress-bar progress-bar-striped progress-bar-animated" style={{ width: width }}></div>
        </div>
    );
}

export default ProgressBar;