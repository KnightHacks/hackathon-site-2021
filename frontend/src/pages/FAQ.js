import { useState } from "react";
import Page from "../components/Page";

const Dropdown = ({ item, index, open, setOpen }) => {
  return (
    <div className="w-full px-12 mt-5 flex flex-wrap">
      <p
        className="text-left text-lg sm:text-xl w-full cursor-pointer"
        onClick={() => {
          if (open === index) setOpen(-1);
          else setOpen(index);
        }}
      >
        {item.question}
      </p>
      {open === index ? (
        <p className="text-left text-base sm:text-lg text-gray-200 ml-4">
          {item.answer}
        </p>
      ) : null}
    </div>
  );
};

/**
 * @desc Renders FAQ page using dropdowns
 * @author Abraham Hernandez
 */

const FAQ = () => {
  const list = [
    {
      question: "What is Knight Hacks?",
      answer:
        "Knight Hacks is the University of Central Florida’s massive hackathon, where hundreds of students with different skill levels come together from around the world to experiment and create unique software or hardware projects from scratch. We empower and enable teams to make something great in only 36 hours by providing an abundance of resources like workshops, mentors, and hardware components.",
    },
    {
      question: "Who can participate?",
      answer:
        "Undergraduate and graduate students from any college or university anywhere in the world are eligible to apply to Knight Hacks, as well as those who have graduated in the past 12 months. Unfortunately, Knight Hacks 2020 cannot admit high school students or students under 18 years of age.",
    },
    {
      question: "Is Knight Hacks Free?",
      answer:
        "Admission to Knight Hacks is completely free. Meals, workshops, mentorship, swag, hardware, and snacks are free for the entire event!",
    },
    {
      question: "How many people can be on a team?",
      answer:
        "You can form teams of up to 4 people. There are no restrictions for team members, so you can team up with hackers of any school, country, or experience level. Teams can be formed before or during the event.",
    },
    {
      question: "What if I am a beginner?",
      answer:
        "Knight Hacks welcomes students of all skill levels. In previous years, about half of the students have attended Knight Hacks as their first hackathon. We’ll have talks, mentors and workshops to help you with your project. Hackathons can be a great place to learn new skills in a short amount of time. Just be eager to learn, and excited to meet lots of awesome people.",
    },
    {
      question: "What kind of workshops, talks, and activities will there be?",
      answer:
        "Previously, we’ve held workshops and talks for a range of skill levels from beginner to advanced like Intro to Web Development and Virtual Reality. We’ve also had introductory workshops to various programming tools such as APIs, databases and platforms. Whether it’s for relaxation or health, novelty or competition, our team has something exciting prepared for you!",
    },
    {
      question: "404: Question Not Found",
      answer:
        "If your question is not listed here, please feel free to reach out to us at team@knighthacks.org or message the Knight Hacks Facebook or Instagram pages.",
    },
    {
      question: "What is the code of conduct for the event?",
      answer: "The event uses the MLH code of conduct which can be found here",
    },
  ];
  const [open, setOpen] = useState(-1);
  return (
    <Page onLanding={false}>
      <div className="flex justify-start items-center w-full flex-col my-4 md:my-12">
        <h1 className=" text-4xl sm:text-6xl md:text-8xl">FAQ</h1>

        <div className="my-4 flex flex-col items-center w-full">
          {list.map((item, index) => (
            <Dropdown
              item={item}
              key={index}
              index={index}
              setOpen={setOpen}
              open={open}
            />
          ))}
        </div>
      </div>
    </Page>
  );
};

export default FAQ;
