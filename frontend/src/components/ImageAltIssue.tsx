//@ts-nocheck
import React, { ReactElement } from 'react';

type ImageAltIssueProps = {
    imageData: any;
}

const renderFormInputColumn = (element: ReactElement) => {
    return (
        <div className="col-md-4">
            <div className="form-group">
                {element}
            </div>
        </div>
    )
}
function ImageAltIssue({ imageData }: ImageAltIssueProps) {
    if (!imageData) {
        return (<></>)
    }


    const formattedImageData = Object.entries(imageData)
        .flatMap(([key, val]) => {
            return val['img-alt']?.map(item => {
                return {
                    file: key,
                    ...item
                }
            })
        }
        )

    const handleDescriptionChange = (file: any, sourceLine: number, inputValue) => {
        const imageObj = imageData[file]['img-alt']?.find((item: { sourceline: number }) => item.sourceline === sourceLine)
        if (imageObj) {
            imageObj['new_value'] = inputValue
        }
    }

    return (
        <div className="img-alt-issue-div">
            {imageData ?
                formattedImageData?.map((imageDetails) => {
                    return (
                        <>
                            <div className='row image-alt-input'>
                                <img className="alt-image" src={imageDetails?.selector?.split('"')[1]} alt={imageDetails?.new_value} />

                                {renderFormInputColumn(
                                    <>
                                        <label className="form-label" htmlFor='suggestedDesc'>Current Description</label>
                                        <input className="form-control" type="text" name="name" id="suggestedDesc"
                                            value={imageDetails?.old_value || "No Alt Text"} readOnly />
                                    </>
                                )}
                                {renderFormInputColumn(
                                    <>
                                        <label className="form-label" htmlFor='userDesc'>Suggested Description</label>
                                        <input className="form-control" type="text" name="name" placeholder="Enter Description"                        
                                            defaultValue={imageDetails?.new_value}
                                            id="userDesc"
                                            onChange={(e) => handleDescriptionChange(imageDetails?.file, imageDetails?.sourceline, e?.target?.value)} />
                                    </>
                                )}
                            </div>
                        </>
                    )
                }) : null}
        </div>
    )
}

export default ImageAltIssue;