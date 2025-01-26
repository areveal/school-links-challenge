import React, {useEffect, useState} from "react";
import {BrowserRouter, Route, Routes} from "react-router";
import Home from "./pages/Home";
import Students from "./pages/Students";
import Exams from "./pages/Exams";
import ExamResults from "./pages/ExamResults";
import './index.css'

function App() {
    const [searchText, setSearchText] = useState("");
    const [filters, setFilters] = useState({});
    const [sort, setSort] = useState("");
    const [urlParams, setUrlParams] = useState(new URLSearchParams())

    useEffect(() => {
        // Update urlParams anytime our filters change
        const params = new URLSearchParams();

        if (searchText) {
            params.append("search", searchText);
        }

        if (filters) {
            Object.entries(filters).forEach(([key, value]) => {
                if (value) {
                    params.append(key, value);
                }
            })
        }

        if (sort) {
            params.append("ordering", sort);
        }

        setUrlParams(params);
    }, [sort, searchText, filters]);

    function HandleSearchTextChange(e) {
        setSearchText(e.target.value);
    }

    function HandleSortChange(e) {
        setSort(e.target.value);
    }

    function HandleFilterChange(e) {
        const filtersCopy = {...filters};
        filtersCopy[e.target.title] = e.target.value;
        setFilters(filtersCopy);
    }

  return (
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Home />} name="home" />
            <Route path="/students" element={<Students urlParams={urlParams} searchText={searchText} OnSortChange={HandleSortChange} OnFilterChange={HandleFilterChange} OnSearchTextChange={HandleSearchTextChange} />} name="students" />
            <Route path="/exams" element={<Exams />} name="exams" />
            <Route path="/exam-results" element={<ExamResults urlParams={urlParams} searchText={searchText} OnSortChange={HandleSortChange} OnFilterChange={HandleFilterChange} OnSearchTextChange={HandleSearchTextChange} />} name="exam-results" />
        </Routes>
    </BrowserRouter>
  );
}

export default App;
