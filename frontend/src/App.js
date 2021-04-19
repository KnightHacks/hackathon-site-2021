import "./App.css";

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Landing from "./pages/Landing";
import About from "./pages/About";
import Sponsors from "./pages/Sponsors";
import Schedule from "./pages/Schedule";
import FAQ from "./pages/FAQ";
import Register from "./pages/Register";

import { TransitionGroup, CSSTransition } from "react-transition-group";
import { useLocation } from "react-router-dom";

/**
 * @desc See AppWithTransitions; don't make routing changes here
 * @author Abraham Hernandez, Rob
 */
const App = () => {
  return (
    <Router>
      <Switch>
        {/*
         * We forward to AppWithTransitions so we can animate the transitions.
         * Don't put more routes here, instead put them in the
         * AppWithTransitions component.
         */}
        <Route path="*">
          <AppWithTransitions />
        </Route>
      </Switch>
    </Router>
  );
};

/**
 * @desc AppWithTransitions is like App but it wraps every page transition to
 *       have a nice blur-up effect.
 * @author Rob
 */
const AppWithTransitions = () => {
  const location = useLocation();
  return (
    <TransitionGroup>
      <CSSTransition key={location.key} classNames="blur" timeout={1000}>
        {/* You can edit the routes here */}
        <Switch location={location}>
          <Route exact path="/" component={Landing} />
          <Route path="/about" component={About} />
          <Route path="/sponsors" component={Sponsors} />
          <Route path="/schedule" component={Schedule} />
          <Route path="/faq" component={FAQ} />
          <Route path="/register" component={Register} />
        </Switch>
      </CSSTransition>
    </TransitionGroup>
  );
};

export default App;
