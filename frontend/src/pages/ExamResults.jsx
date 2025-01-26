import React, {useEffect, useState} from 'react'
import SchoolNavBar from "../components/SchoolNavBar";
import {Container, Table} from "react-bootstrap";
import Filters from "../components/Filters";
import api from "../api";
import ResultRow from "../components/ResultRow";

function ExamResults({urlParams, searchText, OnSortChange, OnFilterChange, OnSearchTextChange}) {
    const [results, setResults] = useState([])

    useEffect(() => {
        const baseUrlPath = "api/results/";
        const urlPath = urlParams.toString() ? baseUrlPath + '?' +  urlParams.toString() : baseUrlPath;

        api.get(urlPath)
            .then((res) => res.data)
            .then((data) => {setResults(data); console.log(data)})
            .catch((err) => alert(err));
    }, [urlParams]);

    return (
        <Container>
            <SchoolNavBar></SchoolNavBar>
            <Filters searchText={searchText} OnSortChange={OnSortChange} OnFilterChange={OnFilterChange} OnSearchChange={OnSearchTextChange} />
            <Table>
                <thead>
                    <tr>
                        <th>Student Name</th>
                        <th>Exam Name</th>
                        <th>Score</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {results.map((result) => <ResultRow key={result.id} result={result} />)}
                </tbody>
            </Table>
        </Container>
    );
}

export default ExamResults;