import React from "react";
import { Routes, Route } from "react-router-dom";
import SignIn from "./routes/sign-in/sign-in.component";
import Home from "./routes/home/home.component";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/sign-in" element={<SignIn />} />
    </Routes>
  );
};

export default App;
