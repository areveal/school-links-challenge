import React, {useEffect, useState} from 'react'
import SchoolNavBar from "../components/SchoolNavBar";
import {Container, Table} from "react-bootstrap";
import api from "../api";
import ExamRow from "../components/ExamRow";

function Exams() {
    const [exams, setExams] = useState([]);

    useEffect(() => {
        api.get("api/exams/")
            .then((res) => res.data)
            .then((data) => {setExams(data); console.log(data);})
            .catch((err) => alert(err))
    }, []);

    return (
        <Container>
            <SchoolNavBar></SchoolNavBar>
            <Table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Code</th>
                        <th>Max Score</th>
                        <th>State</th>
                        <th>Subject</th>
                        <th>Grade</th>
                    </tr>
                </thead>
                <tbody>
                    {exams.map((exam) => <ExamRow exam={exam} />)}
                </tbody>
            </Table>
        </Container>
    );
}

export default Exams;