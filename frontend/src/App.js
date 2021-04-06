import { CgMenu, CgVolume } from "react-icons/cg";
function App() {
  return (
    <div className="bg-koi-fish-pond w-screen h-screen grid grid-col-4 grid-rows-1 grid-flow-col gap-0">
      <div className="col-span-1 min-w-0 bg-red-800 w-full">
        <div className="flex flex-row text-white">
          <CgVolume size="1em" className=" bg-blue-800" />
          <CgMenu size="1em" className=" bg-purple-300" />
        </div>
      </div>

      <div className="col-span-2 text-white bg-green-800 w-full">
        <div className="flex justify-center items-center flex-col w-full h-full">
          <p className="text-5xl">Welcome to</p>
          <p className="text-8xl">KNIGHT HACKS</p> {/* change this */}
          <p className="text-xl">October 9th - October 11th, 2021</p>
        </div>
      </div>

      <div className="col-span-1 bg-yellow-500 w-full" />
    </div>
  );
}

export default App;
