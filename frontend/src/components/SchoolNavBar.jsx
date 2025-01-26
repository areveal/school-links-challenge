import React from "react";
import {Nav, Navbar, NavbarBrand} from "react-bootstrap";
import {NavLink} from "react-router";

function SchoolNavBar() {
    return (
        <Navbar>
            <NavbarBrand>School Links</NavbarBrand>
            <Nav>
                <Nav.Link as={NavLink} to="/" exact activeClassName="active">Home</Nav.Link>
                <Nav.Link as={NavLink} to="/students" activeClassName="active">Students</Nav.Link>
                <Nav.Link as={NavLink} to="/exams" activeClassName="active">Exams</Nav.Link>
                <Nav.Link as={NavLink} to="/exam-results" activeClassName="active">Exam Results</Nav.Link>
            </Nav>
        </Navbar>
    );
}

export default SchoolNavBar;