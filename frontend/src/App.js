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

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="*">
          <AppWithTransitions />
        </Route>
      </Switch>
    </Router>
  );
};

const AppWithTransitions = () => {
  const location = useLocation();
  return (
    <TransitionGroup>
      <CSSTransition key={location.key} classNames="fade" timeout={1000}>
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
