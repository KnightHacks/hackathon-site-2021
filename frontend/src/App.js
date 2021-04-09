import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Landing from "./pages/Landing";
import About from "./pages/About";
import Sponsors from "./pages/Sponsors";
import Schedule from "./pages/Schedule";
import FAQ from "./pages/FAQ";
import Register from "./pages/Register";

/**
 * @desc Handles routing to all pages
 * @author Abraham Hernandez
 */

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" component={Landing} exact />
        <Route path="/about" component={About} />
        <Route path="/sponsors" component={Sponsors} />
        <Route path="/schedule" component={Schedule} />
        <Route path="/faq" component={FAQ} />
        <Route path="/register" component={Register} />
      </Switch>
    </Router>
  );
};

export default App;
