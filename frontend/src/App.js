import { CgMenu, CgVolume } from "react-icons/cg";
import { FaTwitter, FaInstagram, FaFacebookF } from "react-icons/fa";

const App = () => {
  return (
    <div className="bg-koi-fish-pond w-screen h-screen grid grid-cols-5 grid-rows-1 grid-flow-col gap-0">
      <div className="col-span-1 w-full">
        <div className="flex flex-row text-white justify-end space-x-8 mr-12 mt-12">
          <CgVolume className="text-5xl" />
          <CgMenu className="text-5xl" />
        </div>
      </div>

      <div className="col-span-3 text-white w-full bg-landing-transparent">
        <div className="flex justify-center items-center flex-col w-full h-full">
          <div className="flex justify-center items-center flex-col w-full h-full">
            <h1 className="text-5xl">Welcome to</h1>
            <div className="bg-knight-hacks-logo w-full h-36 bg-no-repeat my-4 bg-center" />
            <p className="text-xl">October 9th - October 11th, 2021</p>
            <button className="px-12 py-2 border-white border-8 rounded-full text-4xl mt-8 hover:bg-blue-400 focus:outline-none">
              <p className="tracking-widest select-none" unselectable="on">
                REGISTER
              </p>
            </button>
          </div>
          <div className="flex flex-row mt-auto mb-8 space-x-8 text-6xl">
            <a href="https://twitter.com/KnightHacks?lang=en/">
              <FaTwitter className="border-4 border-white rounded-xl p-2 hover:bg-blue-400" />
            </a>
            <a href="https://www.instagram.com/knighthacks/">
              <FaInstagram className="border-4 border-white rounded-xl p-2 hover:bg-blue-400" />
            </a>
            <a href="https://www.facebook.com/KnightHacks/">
              <FaFacebookF className="border-4 border-white rounded-xl p-2 hover:bg-blue-400" />
            </a>
          </div>
        </div>
      </div>

      <div className="col-span-1 w-full" />
    </div>
  );
};

export default App;
