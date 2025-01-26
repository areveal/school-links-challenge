import React, {useEffect, useState} from 'react';
import {Accordion, Col, Form, Row} from "react-bootstrap";


function Filters({searchText, OnSortChange, OnFilterChange, OnSearchChange}) {
    const [filterables, setFilterables] = useState({});

    function getFilterables() {

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
                                    <option>Sort</option>
                                    <option value="score">Score Asc</option>
                                    <option value="-score">Score Desc</option>
                                </Form.Select>
                            </Col>
                            <Col>
                                <Form.Select onChange={OnFilterChange} title="exam_name">
                                    <option>Exam Name</option>
                                    <option>Ohio End of Course Exam</option>
                                    <option>WebXam</option>
                                </Form.Select>
                            </Col>
                            <Col>
                                <Form.Select onChange={OnFilterChange} title="subject">
                                    <option>Subject</option>
                                    <option>English</option>
                                    <option>Maths</option>
                                </Form.Select>
                            </Col>
                            <Col>
                                <Form.Select onChange={OnFilterChange} title="grade">
                                    <option>Grade</option>
                                    <option>9</option>
                                    <option>10</option>
                                    <option>11</option>
                                    <option>12</option>
                                </Form.Select>
                            </Col>
                            <Col>
                                <Form.Select onChange={OnFilterChange} title="state">
                                    <option>State</option>
                                    <option>CO</option>
                                    <option>TX</option>
                                    <option>OH</option>
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