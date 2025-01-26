import React from "react";
import {Nav, Navbar, NavbarBrand} from "react-bootstrap";
import {NavLink} from "react-router";

function SchoolNavBar() {
    return (
        <Navbar>
            <NavbarBrand>School Links</NavbarBrand>
            <Nav>
                <Nav.Link as={NavLink} to="/" exact="true">Home</Nav.Link>
                <Nav.Link as={NavLink} to="/students" >Students</Nav.Link>
                <Nav.Link as={NavLink} to="/exams" >Exams</Nav.Link>
                <Nav.Link as={NavLink} to="/exam-results" >Exam Results</Nav.Link>
            </Nav>
        </Navbar>
    );
}

export default SchoolNavBar;