import Page from "../components/Page";

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
    </Page>
  );
};

export default Sponsors;
