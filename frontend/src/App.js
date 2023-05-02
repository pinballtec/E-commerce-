import "./App.css";

import Header from "./components/Header";
import Footer from "./components/Footer";

import HomeScreen from "./screens/HomeScreen";
import ProductScreen from "./screens/productscreen";

import { Container } from "react-bootstrap";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <Header />
      <main className="py-5">
        <Container>
          {/* <HomeScreen /> */}
          <Routes>
            <Route
              exact
              path="/"
              element={<HomeScreen />}
            />
            <Route
              path="/product/:id"
              element={<ProductScreen />}
            />
          </Routes>
        </Container>
      </main>
      <Footer />
    </Router>
  );
}

export default App;
