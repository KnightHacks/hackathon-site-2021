module.exports = {
  purge: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      backgroundImage: (theme) => ({
        "koi-fish-pond": "url('/src/assets/KoiFishPond.png')",
        "knight-hacks-logo": "url('/src/assets/KnightHacksLogo.svg')",
      }),
      backgroundColor: (theme) => ({
        "landing-transparent": "rgba(191, 219, 254, 0.2)",
      }),
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
