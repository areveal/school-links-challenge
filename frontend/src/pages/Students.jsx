import React, {useEffect, useState} from 'react'
import SchoolNavBar from "../components/SchoolNavBar";
import {Container} from "react-bootstrap";
import StudentRow from '../components/StudentRow'
import api from "../api";
import Filters from "../components/Filters";

function Students() {
    const [students, setStudents] = useState([]);
    const [searchText, setSearchText] = useState("");
    const [filters, setFilters] = useState({});
    const [sort, setSort] = useState("");

    // function to build API call to get students using filter/search/sort criteria
    function getStudents() {
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

        const baseUrlPath = "api/students/";
        const urlPath = params.toString() ? baseUrlPath + '?' +  params.toString() : baseUrlPath;

        api
            .get(urlPath)
            .then((res) => res.data)
            .then((data) => {setStudents(data); console.log(data);})
            .catch((err) => alert(err));
    }

    useEffect(() => {
        getStudents();
    }, [searchText, filters, sort]);

    function HandleSearchTextChange(e) {
        setSearchText(e.target.value);
    }

    function HandleSortChange(e) {
        setSort(e.target.value);
    }

    function HandleFilterChange(e) {
        console.log(e.target.value);
        const filtersCopy = {...filters};
        filtersCopy[e.target.title] = e.target.value;

        setFilters(filtersCopy);
    }

    return (
        <Container>
            <SchoolNavBar></SchoolNavBar>
            <Filters searchText={searchText} OnSortChange={HandleSortChange} OnFilterChange={HandleFilterChange} OnSearchChange={HandleSearchTextChange} />
            {students.map((student) => <StudentRow student={student} key={student.id} />)}
        </Container>
    );
}

export default Students;