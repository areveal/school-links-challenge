import React from "react";
import {Nav, Navbar, NavbarBrand} from "react-bootstrap";

function SchoolNavBar() {
    return (
        <Navbar>
            <NavbarBrand>School Links</NavbarBrand>
            <Nav>
                <Nav.Link href="/">Home</Nav.Link>
                <Nav.Link href="/students">Students</Nav.Link>
                <Nav.Link href="/exams">Exams</Nav.Link>
                <Nav.Link href="/exam-results">Exam Results</Nav.Link>
            </Nav>
        </Navbar>
    );
}

export default SchoolNavBar;