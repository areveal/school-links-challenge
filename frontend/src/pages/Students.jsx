import React, {useEffect, useState} from 'react'
import SchoolNavBar from "../components/SchoolNavBar";
import {Container} from "react-bootstrap";
import StudentRow from '../components/StudentRow'
import api from "../api";
import Filters from "../components/Filters";

function Students({urlParams, searchText, OnSortChange, OnFilterChange, OnSearchTextChange}) {
    const [students, setStudents] = useState([]);

    // function to build API call to get students using filter/search/sort criteria
    function getStudents() {

        const baseUrlPath = "api/students/";
        const urlPath = urlParams.toString() ? baseUrlPath + '?' +  urlParams.toString() : baseUrlPath;

        api
            .get(urlPath)
            .then((res) => res.data)
            .then((data) => {setStudents(data); console.log(data);})
            .catch((err) => alert(err));
    }

    useEffect(() => {
        getStudents();
    }, [urlParams]);

    return (
        <Container>
            <SchoolNavBar></SchoolNavBar>
            <Filters searchText={searchText} OnSortChange={OnSortChange} OnFilterChange={OnFilterChange} OnSearchChange={OnSearchTextChange} />
            {students.map((student) => <StudentRow student={student} key={student.id} />)}
        </Container>
    );
}

export default Students;