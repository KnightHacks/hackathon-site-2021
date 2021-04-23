import { FaTwitter, FaInstagram, FaFacebookF } from "react-icons/fa";
import { Link } from "react-router-dom";
import Page from "../components/Page";
const About = () => {
  return (
    <Page onLanding={false}>
      <div className="flex justify-start items-center w-full flex-col my-4 md:my-12">
        <h1 className="text-4xl sm:text-4xl md:text-6xl">About Knights Hack</h1>
        <div className="my-4 flex flex-col items-center w-2/3">Hello</div>
      </div>
    </Page>
  );
};

export default About;
