import { FaTwitter, FaInstagram, FaFacebookF } from "react-icons/fa";
import { Link } from "react-router-dom";
import Page from "../components/Page";

/**
 * @desc Renders Landing page of the site
 * @author Abraham Hernandez
 */

const Landing = () => {
  return (
    <Page onLanding={true}>
      <div className="flex justify-center items-center flex-col w-full h-full">
        <div className="flex justify-center items-center flex-col w-full h-full">
          <h1 className="text-3xl md:text-4xl lg:text-5xl w-full text-center">
            Welcome to
          </h1>
          <div className="bg-knight-hacks-logo w-full h-20 md:h-36 bg-no-repeat my-2 md:my-4 bg-center" />
          <p className="text-xl w-full text-center">
            October 9th - October 11th, 2021
          </p>
          <Link
            className="px-4 sm:px-6 md:px-12 py-2 border-white border-4 md:border-8 rounded-full text-xl sm:text-3xl md:text-4xl mt-4 md:mt-8 hover:bg-blue-400 focus:outline-none"
            to="/register"
          >
            <p className="tracking-widest select-none" unselectable="on">
              REGISTER
            </p>
          </Link>
        </div>
        <div className="flex flex-row mt-auto mb-8 space-x-8  text-4xl sm:text-5xl md:text-6xl">
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
    </Page>
  );
};

export default Landing;
