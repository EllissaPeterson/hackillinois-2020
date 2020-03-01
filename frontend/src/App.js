import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route} from "react-router-dom";
import ReactCSSTransitionGroup from 'react-addons-css-transition-group';
import TitlePage from './components/pages/TitlePage';
import OptionsPage from './components/pages/OptionsPage';
import OptionsPageCountries from './components/pages/OptionsPageCountries';
import MapPage from './components/pages/MapPage';

const Home = () => (
    <header className="App-header">
        <TitlePage/>
    </header>
)

function App() {
  return (
      <Router>
        <div className="App">
            <ReactCSSTransitionGroup transitionName="load"
                           transitionAppear={true}
                           transitionAppearTimeout={1000}
                           transitionEnter={false}
                           transitionLeave={false}>
                <Route exact path="/" component={TitlePage} />
                <Route exact path="/options" component={OptionsPage} />
                <Route exact path="/options/countries" component={OptionsPageCountries} />
                <Route exact path="/map" component={MapPage} />
            </ReactCSSTransitionGroup>
        </div>
      </Router>
  );
}

export default App;
