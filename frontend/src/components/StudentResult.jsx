import React from 'react';
import {Col, Row} from "react-bootstrap";

function StudentResult({result}) {
    return (
        <Row>
            <Col>{result.exam_name}</Col>
            <Col>{result.state}</Col>
            <Col>{result.subject}</Col>
            <Col>{result.grade}</Col>
            <Col>{result.score}</Col>
        </Row>
    );
}

export default StudentResult;