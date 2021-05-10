module.exports = {
  purge: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      width: {
        "19/20": "95%",
      },
      height: {
        "19/20": "95%",
      },
      backgroundImage: (theme) => ({
        "koi-fish-pond": "url('/src/assets/KoiFishPond.png')",
        "knight-hacks-logo": "url('/src/assets/knightHacksLogo_WHITE.svg')",
      }),
      backgroundColor: (theme) => ({
        "landing-transparent": "rgba(191, 219, 254, 0.2)",
        "menu-transparent": "rgba(96, 165, 250, 0.6)",
      }),
    },
  },
  variants: {
    extend: {
      fontSize: ["hover", "focus"],
    },
  },
  plugins: [],
};
