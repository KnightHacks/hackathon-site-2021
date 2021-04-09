import { useState } from "react";
import Menu from "./Menu";

const Page = ({ children, onLanding }) => {
  const [open, setOpen] = useState(false);

  return (
    <div className="bg-koi-fish-pond bg-no-repeat bg-cover w-full h-screen grid grid-cols-5 grid-rows-1 grid-flow-col gap-0">
      <div className="col-span-1 w-full">
        <Menu open={open} setOpen={setOpen} />
      </div>

      <div
        className={
          "col-span-3 text-white w-full bg-landing-transparent " +
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
