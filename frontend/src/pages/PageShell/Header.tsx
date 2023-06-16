import React from 'react';
import './styles/Header.scss';
import logo from '../../assets/508.png';
import log from '../../assets/PSL_Logo.png';
function Header() {
  return (
     <nav className="navbar navbar-inverse">
       <div className="container-fluid">
        <div className="navbar-header">
          <a className="navbar-brand" href="#">
            <img src={log} alt="Logo" width='36' height='36' style={{marginRight:12,marginLeft:-12}}/>
            <span ></span>
            {/* <span ></span>
            <span ></span> */}
            {/* <span ></span> */}
            <span className='five' >FiveO8</span>
            <span ></span>
            {/* <span ></span>
            <span ></span> */}
          <span ></span>
          <span ></span>
            {/* <span >FiveO8</span> */}
            {/* <img src={logo} alt="Logo" width='80' height='36'/> */}
           
          </a>
        </div>
        <span style={{marginLeft:853}}><i className="fas fa-cog" ></i> Kevin Peter</span>
        <div className="circle">
  <p className="circle-inner">KP</p>
</div>
       </div>
     </nav>
   );
}

export default Header;
