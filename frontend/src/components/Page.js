import { useState } from "react";
import Menu from "./Menu";
import { Link } from "react-router-dom";
/**
 * @desc Renders template layout for all pages
 * @param Takes the children JSX elements and a boolean value thats true if the current page is the Landing page
 * @author Abraham Hernandez
 */

const Page = ({ children, onLanding }) => {
  const [open, setOpen] = useState(false);

  return (
    <div
      className={
        "bg-koi-fish-pond bg-no-repeat bg-cover w-full h-screen flex flex-col items-center sm:items-start sm:grid sm:grid-cols-5 sm:grid-rows-1 sm:grid-flow-col sm:gap-0 " +
        (open ? "filter blur-md" : "")
      }
    >
      <div className="sm:col-span-1 w-full">
        <Menu open={open} setOpen={setOpen} />
      </div>

      <div className="sm:col-span-3 text-white w-full-with-margins h-full bg-landing-transparent rounded-2xl overflow-y-auto">
        {children}
      </div>

        <Link to="/" className="col-span-1 w-full">
          {!onLanding ? (
              <div className="bg-knight-hacks-logo bg-no-repeat bg-center w-11/12 h-16 sm:h-32 mt-12 hidden sm:block" />
          ) : null}
        </Link>
    </div>
  );
};

export default Page;
