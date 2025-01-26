import React, {useEffect, useState} from 'react';
import {Accordion, Col, Form, Row} from "react-bootstrap";
import api from "../api";


function Filters({searchText, OnSortChange, OnFilterChange, OnSearchChange}) {
    const [filterables, setFilterables] = useState({
        "exam_names": [],
        "subjects": [],
        "grades": [],
        "states": []
    });

    function getFilterables() {
        api.get("api/filterables/")
            .then((res) => res.data)
            .then((data) => {setFilterables(data); console.log(data)})
            .catch((err) => {alert(err)});
    }

    useEffect(() => {
        getFilterables()
    }, []);

    return (
        <Row className="filters">
            <Accordion>
                <Accordion.Item>
                    <Accordion.Header>Filters</Accordion.Header>
                    <Accordion.Body>
                        <Row>
                            <Col>
                                <Form.Select onChange={OnSortChange}>
                                    <option value="">Sort</option>
                                    <option value="score">Score Asc</option>
                                    <option value="-score">Score Desc</option>
                                </Form.Select>
                            </Col>
                            <Col>
                                <Form.Select onChange={OnFilterChange} title="exam_name">
                                    <option value="">All Exams</option>
                                    {filterables.exam_names.map((exam_name) => <option key={"exam_name_" + exam_name}>{exam_name}</option>)}
                                </Form.Select>
                            </Col>
                            <Col>
                                <Form.Select onChange={OnFilterChange} title="subject">
                                    <option value="">All Subjects</option>
                                    {filterables.subjects.map((subject) => <option key={"subject_" + subject}>{subject}</option>)}
                                </Form.Select>
                            </Col>
                            <Col>
                                <Form.Select onChange={OnFilterChange} title="grade">
                                    <option value="">All Grades</option>
                                    {filterables.grades.map((grade) => <option key={"grade_" + grade}>{grade}</option>)}
                                </Form.Select>
                            </Col>
                            <Col>
                                <Form.Select onChange={OnFilterChange} title="state">
                                    <option value="">All States</option>
                                    {filterables.states.map((state) => <option key={"state_" + state}>{state}</option>)}
                                </Form.Select>
                            </Col>
                            <Col align="end">
                                <input placeholder="Search..." value={searchText} onChange={OnSearchChange} />
                            </Col>
                        </Row>
                    </Accordion.Body>
                </Accordion.Item>
            </Accordion>
        </Row>
    )
}

export default Filters;