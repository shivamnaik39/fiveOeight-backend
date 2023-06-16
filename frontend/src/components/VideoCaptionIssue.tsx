import React, { ReactElement } from 'react';
import videoScreen from '../assets/video_screenshot.png';

function VideoCaptionIssue() {
    return (
        <>

            <div className='row image-alt-input'>
                <img src={videoScreen} alt="Video Screenshot" className='video-screenshot'/>
                No captions available
            </div>
        </>
    );
}

export default VideoCaptionIssue;
