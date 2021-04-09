import { CgMenu, CgVolume } from "react-icons/cg";
import { Link } from "react-router-dom";

const Menu = ({ open, setOpen }) => {
  return (
    <div
      className={
        "w-full " +
        (open
          ? "z-10 absolute w-full h-full bg-menu-transparent transition ease-in duration-300"
          : "")
      }
    >
      <div className={"text-white mt-12 ml-8 w-min"}>
        <div className="flex flex-col sm:flex-row-reverse space-y-4 sm:space-y-0 space-x-reverse space-x-8">
          <div>
            <CgMenu
              className="text-4xl md:text-5xl cursor-pointer"
              onClick={() => setOpen(!open)}
            />
            {open ? (
              <ul className="text-5xl text-white">
                <li className="mt-4 hover:underline">
                  <Link to="/about">About</Link>
                </li>
                <li className="mt-4 hover:underline">
                  <Link to="/sponsors">Sponsors</Link>
                </li>
                <li className="mt-4 hover:underline">
                  <Link to="/schedule">Schedule</Link>
                </li>
                <li className="mt-4 hover:underline">
                  <Link to="/faq">FAQ</Link>
                </li>
                <li className="mt-4 hover:underline">
                  <Link to="/register">Register</Link>
                </li>
              </ul>
            ) : null}
          </div>
          <CgVolume
            className={
              "text-4xl md:text-5xl cursor-pointer " + (open ? "invisible" : "")
            }
          />
        </div>
      </div>
    </div>
  );
};

export default Menu;
