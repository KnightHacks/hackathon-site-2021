<h1 align="center">
  2021 Knight Hacks Hackathon Site
</h1>

This repository is the source code for the 2021 Fall hackathon source code.

## Installation

```shell
git clone https://github.com/KnightHacks/hackathon-site-2021.git
cd frontend
npm install
```

## Getting Started

To run a live development server, run the following in a terminal:

```shell
cd frontend
npm start
```

This will host the website at http://localhost:8000. As you make updates to the
code, the development server will automatically reload the page.

If you get errors, try running `npm install` (make sure you're in the
`frontend/` directory before you do this). Different branches might have
different dependencies installed, so running a fresh `npm install` after each
branch switch is advisable.

## Project Structure

This repository has both the frontend and backend code. This README discusses
the frontend code.

The project is a basic `create-react-app`. The root file is
`frontend/src/App.js`, but most of the actual logic lives in various files in
`frontend/src/pages/` and `frontend/src/components/`

CSS is mostly handled with Tailwind CSS, with some custom vanilla CSS here and
there.

## Stack

### React

In order to be able to work on this project, you'll need to be familiar with
React. React is a UI rendering library that is essentially a way to embed HTML
in your JavaScript, which gives enables for powerful, programmatic control over
the UI on the page. If you're not familiar with HTML, CSS, and JavaScript, you
should learn those first so that React makes more sense.

Docs: https://reactjs.org/docs/getting-started.html

### Tailwind CSS

Tailwind CSS is a CSS utility library. It provides useful prebuilt CSS classes
that enable simple and effective styling without dealing with separate
stylesheets. Tailwind CSS also provides responsive variants of classes to make
it easier to build a webpage that adapts to any screen size. It feels most like
inline CSS styles in regular HTML.

Docs: https://tailwindcss.com/

### Ripples

We are considering incorporating https://github.com/sirxemic/jquery.ripples to
the project later.
