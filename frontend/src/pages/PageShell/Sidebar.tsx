//@ts-nocheck
import React, { useState } from 'react';
import {
  CDBSidebar,
  CDBSidebarContent,
  CDBSidebarFooter,
  CDBSidebarHeader,
  CDBSidebarMenu,
  CDBSidebarMenuItem,
} from 'cdbreact';
import { NavLink } from 'react-router-dom';
import './Sidebar.css';
import log from '../../assets/persistentLogo.svg';

const Sidebar = () => {
  const [selected, setSelected] = useState(null);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  const handleSelect = (index) => {
    setSelected(index);
  };

  return (
    <div style={{ position: 'fixed', top: -40, left: 0, bottom: 0, zIndex: 3 ,paddingBottom:0}}>
      <CDBSidebar className='sidebar-wrapper' textColor="#323130" backgroundColor="#fff" isOpen={isSidebarOpen}>
        <CDBSidebarHeader className="sidebar-header">
       <div></div>
        <a href="/" className="text-decoration-none" style={{ color: 'inherit' }}><div><img src={log} alt="Logo" width="fit-content" height="fit-content"  /></div>
        
  
</a>
        </CDBSidebarHeader>

        <CDBSidebarContent className="sidebar-content">
          <CDBSidebarMenu>
            <NavLink exact to="/" activeClassName="activeClicked">
              <CDBSidebarMenuItem className="sidebar-menu-item" icon="home" selected={selected === 0} onClick={() => handleSelect(0)} >Home</CDBSidebarMenuItem>
            </NavLink>
            <NavLink exact to="/tables" activeClassName="activeClicked">
              <CDBSidebarMenuItem className="sidebar-menu-item" icon="table" selected={selected === 1} onClick={() => handleSelect(1)}>My Previous Runs</CDBSidebarMenuItem>
            </NavLink>
            <NavLink exact to="/profile" activeClassName="activeClicked">
              <CDBSidebarMenuItem className="sidebar-menu-item" icon="user" selected={selected === 2} onClick={() => handleSelect(2)}>Profile</CDBSidebarMenuItem>
            </NavLink>
            <NavLink exact to="/analytics" activeClassName="activeClicked">
              <CDBSidebarMenuItem className="sidebar-menu-item" icon="chart-line" selected={selected === 3} onClick={() => handleSelect(3)}>Analytics</CDBSidebarMenuItem>
            </NavLink>
            <NavLink exact to="/help" activeClassName="activeClicked">
              <CDBSidebarMenuItem className="sidebar-menu-item" icon="question-circle" selected={selected === 4} onClick={() => handleSelect(4)}>Accessibility Help</CDBSidebarMenuItem>
            </NavLink>
            <NavLink exact to="/hero404" target="_blank" activeClassName="activeClicked">
              <CDBSidebarMenuItem className="sidebar-menu-item" n icon="envelope" selected={selected === 5} onClick={() => handleSelect(5)}>Contact Us</CDBSidebarMenuItem>
            </NavLink>
          </CDBSidebarMenu>
        </CDBSidebarContent>
        <div className="borderOne" ></div>
        <CDBSidebarFooter style={{ textAlign: 'center', fontSize: '1.0rem',paddingTop:25,paddingBottom:20 }}>
          <div style={{ padding: '4px 4px' }}>
            <em style={selected === 4 ? { borderBottom: '1px solid #fff' } : null}>"Accessibility is not a feature,<br/>it is a human right."</em>
          </div>
          <div style={{ marginTop: '5px' ,fontSize: '1.0rem' }}>
            <strong>Equal Access</strong>
          </div>
          <div style={{ marginBottom: '0px' }}></div>

        </CDBSidebarFooter>
      </CDBSidebar>

    </div>
  );
};

export default Sidebar;
