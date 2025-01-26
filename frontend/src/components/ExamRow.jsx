import React from 'react';
import {Col, Row} from "react-bootstrap";


function ExamRow({exam}) {
    return (
        <tr>
            <td>{exam.name}</td>
            <td>{exam.code}</td>
            <td>{exam.max_score}</td>
            <td>{exam.state}</td>
            <td>{exam.subject}</td>
            <td>{exam.grade}</td>
        </tr>
    );
}

export default ExamRow;