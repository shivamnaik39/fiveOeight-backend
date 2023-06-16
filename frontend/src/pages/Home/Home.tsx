import React, { useState } from 'react';
import StepOne from '../../components/StepOne';
import StepThree from '../../components/StepThree';
import StepTwo from '../../components/StepTwo';
import './styles/Home.scss';

function Home() {
    const [currentStep, setCurrentStep] = useState(1)
    const stepArr = [
        { stepNo: 1, element: <StepOne setCurrentStep={setCurrentStep} /> },
        { stepNo: 2, element: <StepTwo setCurrentStep={setCurrentStep} /> },
        { stepNo: 3, element: <StepThree /> },
    ]

    return (
        <section className="checker-container">
            <div className="container">
                <div className="row d-flex justify-content-center">
                    <div >
                        <div className="wizard">
                                <div className="tab-content" id="main_form">
                                    <>
                                        {stepArr.find(step => step.stepNo === currentStep)?.element}
                                        
                                    </>
                                </div>

                        </div>
                    </div>
                </div>
            </div>
        </section>

    );
}

export default Home;
