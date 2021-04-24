import { FaTwitter, FaInstagram, FaFacebookF } from "react-icons/fa";
import Page from "../components/Page";
/**
 * @desc About Page
 * @author Ro-Hanna Jowallah
 */
const About = () => {
  return (
    <Page onLanding={false}>
      <div className="flex justify-start items-center w-full flex-col my-4 md:my-12">
        <h1 className="text-4xl sm:text-4xl mt-20 md:text-6xl text-center">
          About Knights Hacks
        </h1>
        <div className="my-2 flex flex-col items-center w-2/3">
          <div className="text-left font-extralight sm:text-lg  mb-2 text-lg sm:text-lg md:text-xl lg:text-2xl mt-24">
            Connect Collaborate and Create with 700 of the brightest developers,
            engineers, and designers in the south-east. Whether you’re a
            seasoned hacker or a tech newbie, Knight Hacks welcomes you. Just
            bring an open mind and a insatiable desire to learn, and we’ll take
            care of the rest. Create a product, learn new skills and have fun
            with friends old and new – all in 36 hours.
          </div>
        </div>
        <div className="flex flex-row  mb-8 space-x-8  mt-32 text-4xl sm:text-5xl md:text-6xl">
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

export default About;
