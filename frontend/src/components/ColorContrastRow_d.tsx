import React, { useState } from 'react';
//@ts-ignore
import { HuePicker } from 'react-color'
//@ts-ignore
import { ColorContrastCalc } from 'color-contrast-calc';

type ColorContrastRowProps = {
    handleColorChange: Function;
    handleBackgroundColorChange: Function;
    contrastDetails: any;
}

function ColorContrastRow(
    { handleColorChange, handleBackgroundColorChange, contrastDetails }
        : ColorContrastRowProps) {
    const [foreground, setForeground] = useState('#f4f4f4')
    const [background, setBackground] = useState('#f4f4f4')

    const yellow = ColorContrastCalc.colorFrom(foreground);
    const black = ColorContrastCalc.colorFrom(background);
    const contrast = yellow.contrastRatioAgainst(black)

    return (
        <>
            <div className='col-md-1'>
                {contrastDetails?.selector}
            </div>
            <div className='col-md-4'>
                Current Font Color
                <div
                    className='current-color-box'
                    style={{ backgroundColor: contrastDetails['current_colors']['color'] }} />
                Suggested Font Color
                <div
                    id={`${contrastDetails?.id}-foreground`}
                    className='current-color-box'
                    style={{ backgroundColor: contrastDetails['suggested_colors']['color'] }} />
                <HuePicker
                    color={contrastDetails['suggested_colors']['color']}
                    onChange={(color: any) => {
                        setForeground(color.hex)
                        handleColorChange(contrastDetails?.id, color.hex)
                    }
                    } />
            </div>
            <div className='col-md-4'>
                Current Background Color
                <div
                    className='current-color-box'
                    style={{ backgroundColor: contrastDetails['current_colors']['background-color'] }} />
                Suggested Background Color
                <div
                    id={`${contrastDetails?.id}-background`}
                    className='current-color-box'
                    style={{ backgroundColor: contrastDetails['suggested_colors']['background-color'] }} />
                <HuePicker
                    color={contrastDetails['suggested_colors']['background-color']}
                    onChange={(color: any) => {
                        setBackground(color.hex)
                        handleBackgroundColorChange(contrastDetails?.id, color.hex)
                    }} />
            </div>
            <div className='col-md-2'>
                Contrast ratio
                <br />
                {contrast?.toFixed(2)}
            </div>
        </>
    );
}

export default ColorContrastRow;
