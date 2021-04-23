import { FaTwitter, FaInstagram, FaFacebookF } from "react-icons/fa";
import { Link } from "react-router-dom";
import Page from "../components/Page";
const About = () => {
  return (
    <Page onLanding={false}>
      <div className="flex justify-start items-center w-full flex-col my-4 md:my-12">
        <h1 className="text-4xl sm:text-4xl md:text-8xl">About Knights Hack</h1>
        <div className="my-6 flex flex-col items-center w-2/3">
          <div className="text-left font-light sm:text-lg  mb-4 text-xl sm:text-xl md:text-2xl mt-36">
            Connect Collaborate and Create with 700 of the brightest developers,
            engineers, and designers in the south-east. Whether you’re a
            seasoned hacker or a tech newbie, Knight Hacks welcomes you. Just
            bring an open mind and a insatiable desire to learn, and we’ll take
            care of the rest. Create a product, learn new skills and have fun
            with friends old and new – all in 36 hours.
          </div>
        </div>
      </div>
    </Page>
  );
};

export default About;
