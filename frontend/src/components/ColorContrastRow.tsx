import React, { useState } from 'react';
//@ts-ignore
import { HuePicker } from 'react-color'
//@ts-ignore
import { ColorContrastCalc } from 'color-contrast-calc';
import contentSpanIcon from '../assets/content_span.png'
import liIcon from '../assets/ul_li_a.png'


type ColorContrastRowProps = {
    handleColorChange: Function;
    handleBackgroundColorChange: Function;
    contrastDetails: any;
}

function ColorContrastRow(
    { handleColorChange, handleBackgroundColorChange, contrastDetails }
        : ColorContrastRowProps) {
    const [foreground, setForeground] = useState(contrastDetails['suggested_colors']['color'])
    const [background, setBackground] = useState(contrastDetails['suggested_colors']['background-color'])

    const foregroundColor = ColorContrastCalc.colorFrom(foreground);
    const backgroundColor = ColorContrastCalc.colorFrom(background);
    const contrast = foregroundColor.contrastRatioAgainst(backgroundColor)


    const currentForegroundColor = ColorContrastCalc.colorFrom(contrastDetails['current_colors']['color']);
    const currentBackgroundColor = ColorContrastCalc.colorFrom(contrastDetails['current_colors']['background-color']);
    const currentContrast = currentForegroundColor.contrastRatioAgainst(currentBackgroundColor)


    const renderElementImage = (selector: string) => {
        switch (selector) {
            case '.content span':
                return (
                    <>
                        <img src={contentSpanIcon} alt={'content span icon element'}/>
                    </>
                )
            case 'ul li a':
                return (
                    <>
                        <img src={liIcon} alt={'li element'}/>
                    </>
                )
            default:
                return (
                    <>
                        {selector}
                    </>
                )
        }
    }
    return (
        <>
            <div className='col-md-1 color-image-selector'>
                {renderElementImage(
                    contrastDetails?.selector
                )}
            </div>
            <div className='col-md-4'>
                <div className='current-color-box'
                    style={{ backgroundColor: contrastDetails['current_colors']['color'] }} />

                <div className="colorText">Current Font Color</div>
                <br />

                <div
                    id={`${contrastDetails?.id}-foreground`}
                    className='current-color-box'
                    style={{ backgroundColor: contrastDetails['suggested_colors']['color'] }} />

                <div className="colorText">Suggested Font Color</div>
                <br />

                <HuePicker
                    width="200px"
                    color={contrastDetails['suggested_colors']['color']}
                    onChange={(color: any) => {
                        setForeground(color.hex)
                        handleColorChange(contrastDetails?.id, color.hex)
                    }
                    } />

            </div>
            <div className='col-md-4 noRight'>
                <div
                    className='current-color-box'
                    style={{ backgroundColor: contrastDetails['current_colors']['background-color'] }} />

                <div className="colorText">Current Background Color</div>
                <br />

                <div
                    id={`${contrastDetails?.id}-background`}
                    className='current-color-box'
                    style={{ backgroundColor: contrastDetails['suggested_colors']['background-color'] }} />
                <div className="colorText">Suggested Background Color</div>
                <br />

                <HuePicker
                    width="200px"
                    color={contrastDetails['suggested_colors']['background-color']}
                    onChange={(color: any) => {
                        setBackground(color.hex)
                        handleBackgroundColorChange(contrastDetails?.id, color.hex)
                    }} />
            </div>
            <div className='col-md-3 noPadding'>
                <div>
                    <span className="colorText">Current Contrast ratio: &nbsp;</span>
                    <span>{currentContrast?.toFixed(2)}</span>
                    {currentContrast > 4.5 ?
                        <span className="contrast-check">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-check-circle-fill " viewBox="0 0 16 16">
                                <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z" />
                            </svg>

                        </span>
                        : <span className="contrast-cross"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-x-circle" viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
                            <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />

                        </svg>
                        </span>}

                </div>



                <span className="colorText">Contrast ratio: &nbsp;</span>
                {contrast?.toFixed(2)}
                {contrast > 4.5 ?
                    <span className="contrast-check">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-check-circle-fill " viewBox="0 0 16 16">
                            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z" />
                        </svg>

                    </span>
                    : <span className="contrast-cross"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-x-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
                        <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />

                    </svg>
                    </span>}
            </div>
        </>
    );
}

export default ColorContrastRow;
