import React from 'react'
import SchoolNavBar from "../components/SchoolNavBar";
import {Container} from "react-bootstrap";

function Home() {
    return (
        <Container>
            <SchoolNavBar></SchoolNavBar>
            <p>Welcome to my Demo! Please have a look around!</p>
        </Container>
    );
}

export default Home;