import React from 'react'


function ResultRow({result}) {
    const formattedDate = new Date(result.date).toLocaleDateString();
    return (
        <tr>
            <td>{result.student.first_name} {result.student.last_name}</td>
            <td>{result.exam.name}</td>
            <td>{result.score}</td>
            <td>{formattedDate}</td>
        </tr>
    );
}

export default ResultRow;