
import React, { useState } from 'react';
import './styles/StepOne.scss';
import angularIcon from '../assets/angular_icon.png';
import htmlIcon from '../assets/html5_icon.png';
import phpIcon from '../assets/php_icon.png';
import reactIcon from '../assets/react_icon.png';
import salesforceIcon from '../assets/salesforce_icon.png';
import vueIcon from '../assets/vue_icon.png';


type StepOneProps = {
  setCurrentStep: Function;
}

function StepOne({ setCurrentStep }: StepOneProps) {
  const [selected, setSelected] = useState<string[]>([]);

  const handleSelect = (techName: string) => {
    setSelected(prevSelected => {
      if (prevSelected.includes(techName)) {
        // If the technology is already selected, remove it from the array
        return prevSelected.filter(name => name !== techName);
      } else {
        // If the technology is not yet selected, add it to the array
        return [...prevSelected, techName];
      }
    });
  };

  const handleNext = () => {
    if (selected.length > 0) {
      setCurrentStep(2);
      // Do something when at least one technology is selected and Next button is clicked
    }
  };

  const isSelected = (techName: string) => selected.includes(techName);
  return (
    <div className="SectionDiv" >
      <div style={{padding:15}}>
        <h2>Let's get started with your project</h2>
      </div>
      <h4>Please select the Technology used</h4>
      <div style={{ padding: 3 }}></div>
      <form>
        <div className='row'>
          <div
            className={`cartPanel ${isSelected('Angular Js') ? 'selected' : ''}`}
            onClick={() => handleSelect('Angular Js')}
          >
            <div className="techLogo">
              <img src={angularIcon} alt="Angular Logo" />
            </div>
            <div className="techName">Angular Js</div>
          </div>
          <div
            className={`cartPanel ${isSelected('PHP') ? 'selected' : ''}`}
            onClick={() => handleSelect('PHP')}
          >
            <div className="techLogo">
              <img src={phpIcon} alt="PHP Logo" />
            </div>
            <div className="techName">PHP</div>
          </div>
          <div
            className={`cartPanel ${isSelected('HTML/CSS') ? 'selected' : ''}`}
            onClick={() => handleSelect('HTML/CSS')}
          >
            <div className="techLogo">
              <img src={htmlIcon} alt="HTML Logo" />
            </div>
            <div className="techName">HTML/CSS</div>
          </div>
        </div>
        <div className='row'>
        <div
          className={`cartPanel ${isSelected('React Js') ? 'selected' : ''}`}
          onClick={() => handleSelect('React Js')}
        >
          <div className="techLogo">
            <img src={reactIcon} alt="React Logo" />
          </div>
          <div className="techName">React Js</div>
        </div>
        <div
          className={`cartPanel ${isSelected('Salesforce') ? 'selected' : ''}`}
          onClick={() => handleSelect('Salesforce')}
        >
          <div className="techLogo">
            <img src={salesforceIcon} alt="Salesforce Logo" />
          </div>
          <div className="techName">Salesforce</div>
        </div>
        <div
          className={`cartPanel ${isSelected('Vue JS') ? 'selected' : ''}`}
          onClick={() => handleSelect('Vue JS')}
        >
          <div className="techLogo">
            <img src={vueIcon} alt="Vue Logo" />
          </div>
          <div className="techName">Vue JS</div>
        </div>
        </div>
      </form>
      <button onClick={handleNext} className="my-btn" >Next</button>
    </div>
  );
}

export default StepOne;
