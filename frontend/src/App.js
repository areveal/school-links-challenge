import React from "react";
import {BrowserRouter, Route, Routes} from "react-router";
import Home from "./pages/Home";
import Students from "./pages/Students";
import Exams from "./pages/Exams";
import ExamResults from "./pages/ExamResults";
import './index.css'

function App() {
  return (
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Home />} name="home" />
            <Route path="/students" element={<Students />} name="students" />
            <Route path="/exams" element={<Exams />} name="exams" />
            <Route path="/exam-results" element={<ExamResults />} name="exam-results" />
        </Routes>
    </BrowserRouter>
  );
}

export default App;
