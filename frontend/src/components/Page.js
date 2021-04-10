import { useState } from "react";
import Menu from "./Menu";

/**
 * @desc Renders template layout for all pages
 * @param Takes the children JSX elements and a boolean value thats true if the current page is the Landing page
 * @author Abraham Hernandez
 */

const Page = ({ children, onLanding }) => {
  const [open, setOpen] = useState(false);

  return (
    <div className="bg-koi-fish-pond bg-no-repeat bg-cover w-full h-screen flex flex-col items-center sm:items-start sm:grid sm:grid-cols-5 sm:grid-rows-1 sm:grid-flow-col sm:gap-0 overflow-y-auto">
      <div className="sm:col-span-1 w-full">
        <Menu open={open} setOpen={setOpen} />
      </div>

      <div
        className={
          "sm:col-span-3 text-white w-full-with-margins h-screen bg-landing-transparent rounded-2xl " +
          (open ? "filter blur-md" : "")
        }
      >
        {children}
      </div>

      <div className={"col-span-1 w-full " + (open ? "filter blur-md" : "")}>
        {/* onLanding ? render smaller logo on right : don't render smaller logo */}
      </div>
    </div>
  );
};

export default Page;
