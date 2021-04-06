import { CgMenu, CgVolume } from "react-icons/cg";
function App() {
  return (
    <div className="bg-koi-fish-pond w-screen h-screen grid grid-cols-5 grid-rows-1 grid-flow-col gap-0">
      <div className="col-span-1 w-full">
        <div className="flex flex-row text-white justify-end space-x-8 mr-12 mt-12">
          <CgVolume className="text-5xl" />
          <CgMenu className="text-5xl" />
        </div>
      </div>

      <div className="col-span-3 text-white w-full bg-landing-transparent">
        <div className="flex justify-center items-center flex-col w-full h-full">
          <p className="text-5xl">Welcome to</p>
          <p className="text-8xl">KNIGHT HACKS</p> {/* change this */}
          <p className="text-xl">October 9th - October 11th, 2021</p>
        </div>
      </div>

      <div className="col-span-1 w-full" />
    </div>
  );
}

export default App;
