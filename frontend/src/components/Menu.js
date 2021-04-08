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
      <div className={"flex flex-row text-white space-x-8 mt-12 ml-20 w-min"}>
        <CgVolume className="text-5xl cursor-pointer" />
        <div>
          <CgMenu
            className="text-5xl cursor-pointer"
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
      </div>
    </div>
  );
};

export default Menu;
