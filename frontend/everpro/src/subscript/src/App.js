import React from 'react';
import GlobalStyle from './globalStyles';
import Services from './pages/Services/Services';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import ScrollToTop from './components/ScrollToTop';
import { Navbar } from './components';

function App() {
  return (
    <Router>
      <GlobalStyle />
      <ScrollToTop />
      <Navbar />
      <Switch>
      <Route path='/services' component={Services} />
      </Switch>
      </Router>
  );
}

export default App;
