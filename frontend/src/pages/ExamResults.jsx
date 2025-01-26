import React, {useEffect, useState} from 'react'
import SchoolNavBar from "../components/SchoolNavBar";
import {Container, Table} from "react-bootstrap";
import Filters from "../components/Filters";
import api from "../api";
import ResultRow from "../components/ResultRow";

function ExamResults() {
    const [results, setResults] = useState([])

    useEffect(() => {
        api.get('api/results/')
            .then((res) => res.data)
            .then((data) => {setResults(data); console.log(data)})
            .catch((err) => alert(err));
    }, []);

    return (
        <Container>
            <SchoolNavBar></SchoolNavBar>
            <Filters />
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