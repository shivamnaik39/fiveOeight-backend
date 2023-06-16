import React from 'react';

type WizardProps = {
    setCurrentStep: Function;
    currentStep: number;
}

const renderStep = (setCurrentStep: Function, stepNo: number, isActive: boolean) => {
    return (
        <li role="presentation" className={isActive ? "active" : "disabled"} onClick={() => setCurrentStep(stepNo)}>
            <a href={`#step${stepNo}`} data-toggle="tab" aria-controls={`step${stepNo}`} role="tab" aria-expanded="true">
                <span className="round-tab">{stepNo} </span>
                <i>Step {stepNo}</i>
            </a>
        </li>
    )
}
function Wizard(props: WizardProps) {
    const { setCurrentStep, currentStep } = props;
    const stepsArr = Array.from(Array(3).keys())

    return (
        <div className="wizard-inner">
            <ul className="nav nav-tabs" role="tablist">
                {stepsArr.map(step => renderStep(setCurrentStep, step + 1, step < currentStep))}
            </ul>
        </div>
    );
}

export default Wizard;
