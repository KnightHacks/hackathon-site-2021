import Page from "../components/Page";
import content from "../assets/content/schedule.json";
import ColorHash from "color-hash";

/**
 * @desc Displays Schedule using formatted events from JSON
 * @author Aileen
 */

const hash = new ColorHash({ lightness: 0.8 });
const Schedule = () => {
  return (
    <Page onLanding={true}>
      <div className="grid w-full flex-col my-4 md:my-12">
        <h1 className="my-10 justify-self-center text-4xl sm:text-5xl lg:text-6xl xl:text-7xl">
          Schedule
        </h1>
        {content.map((event) => {
          return (
            <div className="ml-24">
              <p className="font-medium text-2xl sm:text-3xl xl:text-4xl my-4">
                {event.day}
              </p>
              {/* Mapping through the content in each events block in JSON */}
              {event.events.map((item) => (
                <div className="mb-5">
                  <div className="font-thin mb-1 text-base space-x-4 sm:text-lg md:text-xl xl:text-2xl">
                    <span className="font-light"> {item.time} </span>{" "}
                    <span> {item.title} </span>
                  </div>
                  {/* Mapping through each string in the tags array in JSON */}
                  {item.tags.map((tag) => (
                    <span
                      style={{ backgroundColor: hash.hex(tag) }}
                      className="font-light rounded-full px-2 py-1 mr-2 text-gray-600"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              ))}
            </div>
          );
        })}
      </div>
    </Page>
  );
};

export default Schedule;
