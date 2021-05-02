import Page from "../components/Page";
import { Disclosure, Transition } from "@headlessui/react";
import { HiChevronDown } from "react-icons/hi";
import list from "../assets/content/faq.json";
/**
 * @desc Renders FAQ page using dropdowns
 * @author Abraham Hernandez
 */

const FAQ = () => {
  return (
    <Page onLanding={false}>
      <div className="flex justify-start items-center w-full flex-col my-4 md:my-12">
        <h1 className="text-4xl sm:text-6xl md:text-8xl">FAQ</h1>

        <div className="my-4 flex flex-col items-center w-2/3">
          {list.map((item, index) => (
            <Disclosure as="div" className="mb-2 w-full rounded-lg shadow-md" key={index}>
              {({ open }) => (
                <>
                  <Disclosure.Button as="div" className={`${open ? "rounded-t-lg" : "rounded-lg"} flex justify-between w-full px-4 py-2 text-xl font-medium text-left cursor-pointer text-gray-900 bg-blue-100 bg-opacity-70 hover:bg-blue-200 hover:bg-opacity-70 focus:outline-none focus-visible:ring focus-visible:ring-blue-500 focus-visible:ring-opacity-75`}
                  >
                    <span>{item.question}</span>
                    <HiChevronDown
                      className={`${
                        open ? "transform rotate-180" : ""
                      } w-5 h-5 text-blue-500`}
                    />
                  </Disclosure.Button>
                  <Transition
                    show={open}
                    enter="transition duration-200 ease-linear"
                    enterFrom="transform opacity-0"
                    enterTo="transform opacity-100"
                    leave="transition duration-100 ease-linear"
                    leaveFrom="transform opacity-100"
                    leaveTo="transform opacity-0"
                  >
                    <Disclosure.Panel
                      static
                      className="text-left text-base sm:text-lg text-gray-700 px-8 py-2 bg-blue-100 bg-opacity-70 rounded-b-lg"
                      dangerouslySetInnerHTML={{ __html: item.answer }}
                    />
                  </Transition>
                </>
              )}
            </Disclosure>
          ))}
        </div>
      </div>
    </Page>
  );
};

export default FAQ;
