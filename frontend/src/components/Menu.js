import { Fragment } from "react";
import { CgMenu, CgVolume } from "react-icons/cg";
import { Dialog, Transition } from "@headlessui/react";
import { Link } from "react-router-dom";

/**
 * @desc Renders menu component containing nav menu and volume
 * @param Takes a piece of state and its update function for when the menu is opened
 * @author Abraham Hernandez
 */

const Menu = ({ open, setOpen }) => {
  return (
    <div className="flex justify-center w-screen">
      <div
        className={
          "leading-6 text-white flex flex-row sm:space-x-8 w-full px-5 pt-6 mt-8 " +
          (open ? "hidden" : "visible")
        }
      >
        <CgMenu
          className="text-4xl md:text-5xl cursor-pointer"
          onClick={() => setOpen(!open)}
        />
        <div className="flex-1 sm:flex-none flex justify-end">
          <CgVolume className="text-4xl md:text-5xl cursor-pointer" />
        </div>
      </div>
      <Transition show={open} as={Fragment}>
        <Dialog
          as="div"
          id="modal"
          className="fixed inset-0 z-10 overflow-y-auto"
          static
          open={open}
          onClose={() => setOpen(false)}
        >
          <div className="min-h-screen">
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0"
              enterTo="opacity-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100"
              leaveTo="opacity-0"
            >
              <Dialog.Overlay className="fixed inset-0 bg-menu-transparent" />
            </Transition.Child>

            <div className="inline-block w-full px-5 pt-6 mt-8 text-left align-middle transition-all transform">
              <Dialog.Title
                as="div"
                className="leading-6 text-white flex flex-row sm:space-x-8"
              >
                <CgMenu
                  className="text-4xl md:text-5xl cursor-pointer"
                  onClick={() => setOpen(!open)}
                />
                <div
                  className={
                    "flex-1 sm:flex-none flex justify-end " +
                    (open ? "filter blur-md" : "cursor-pointer")
                  }
                >
                  <CgVolume className="text-4xl md:text-5xl" />
                </div>
              </Dialog.Title>
              <Transition.Child
                as={Fragment}
                enter="ease-out duration-300"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="ease-in duration-200"
                leaveFrom="opacity-100 scale-100"
                leaveTo="opacity-0 scale-95"
              >
                <div className="mt-2">
                  <ul className="text-4xl sm:text-5xl text-white">
                    <li className="mt-4 hover:underline">
                      <Link to="/" onClick={() => setOpen(false)}>
                        Home
                      </Link>
                    </li>
                    <li className="mt-4 hover:underline">
                      <Link to="/about" onClick={() => setOpen(false)}>
                        About
                      </Link>
                    </li>
                    <li className="mt-4 hover:underline">
                      <Link to="/sponsors" onClick={() => setOpen(false)}>
                        Sponsors
                      </Link>
                    </li>
                    <li className="mt-4 hover:underline">
                      <Link to="/schedule" onClick={() => setOpen(false)}>
                        Schedule
                      </Link>
                    </li>
                    <li className="mt-4 hover:underline">
                      <Link to="/faq" onClick={() => setOpen(false)}>
                        FAQ
                      </Link>
                    </li>
                    <li className="mt-4 hover:underline">
                      <Link to="/register" onClick={() => setOpen(false)}>
                        Register
                      </Link>
                    </li>
                  </ul>
                </div>
              </Transition.Child>
            </div>
          </div>
        </Dialog>
      </Transition>
    </div>
  );
};

export default Menu;
