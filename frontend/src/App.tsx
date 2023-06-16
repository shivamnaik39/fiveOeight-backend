import React from 'react';
import Home from './pages/Home/Home';
import { Routes, Route } from "react-router-dom";
import PageShell from './pages/PageShell/PageShell';

function App() {
  return (
    <div className="App">
      <PageShell>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </PageShell>
    </div>
  );
}

export default App;
