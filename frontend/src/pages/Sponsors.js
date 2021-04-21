import Page from "../components/Page";

// for testing only, not for final production
import TestLogo from "../assets/KnightHacksLogo.svg";

/**
 * @desc sponsors page; still WIP since we are waiting on sponsors
 * @author Rob
 */
const Sponsors = () => {
  return (
    <Page onLanding={false}>
      <h1
        className={`
          text-4xl w-full text-center mt-16
          md:text-5xl md:mt-24
          lg:mt-32
          xl:text-6xl xl:mt-36
          2xl:text-7xl 2xl:mt-36
        `}
      >
        Our Sponsors
      </h1>
      <div className="flex flex-col flex-wrap content-center">
        <img
          className="w-2/3 xl:w-96 ml-36 mt-20"
          src={TestLogo}
          alt="test logo"
        />
        <img
          className="w-2/3 xl:w-96 mr-36 mt-20 transform rotate-180"
          src={TestLogo}
          alt="test logo"
        />
        <img
          className="w-2/3 xl:w-96 ml-36 mt-20"
          src={TestLogo}
          alt="test logo"
        />
      </div>
    </Page>
  );
};

export default Sponsors;
