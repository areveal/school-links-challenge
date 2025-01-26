import React from 'react';
import StudentResult from '../components/StudentResult'
import {Accordion} from "react-bootstrap";

function StudentRow({student}) {
    const studentHasResults = student.results.length > 0;
    return (
        <Accordion>
            <Accordion.Item eventKey={student.id}>
                <Accordion.Header>
                    {student.first_name} {student.last_name}
                </Accordion.Header>
                {studentHasResults && (
                    <Accordion.Body>
                        {student.results.map((result) => <StudentResult key={result.id} result={result} />)}
                    </Accordion.Body>
                )}
            </Accordion.Item>
        </Accordion>
    );
}

export default StudentRow;