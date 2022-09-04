import React from 'react'
import {Link} from 'react-router-dom';
import { useParams } from 'react-router-dom';

import {Row, Col, Image, ListGroup, Button, Card} from 'react-bootstrap';

import Rating from '../components/Rating';
import products from '../products'; 
import { withRouter } from "react-router";

function ProductScreen() {
  const { id } = useParams();
  const product = products.find((p) => p._id === id)
  return (
    <div>
      <div>
        <Row>
          <Col md={6}>
            <Image src={product.image} alt={product.name} fluid/>
          </Col>
        </Row>
      </div>
        <Link to='/home' className='btn btn-light my-3'>Go Back</Link>
    </div>
  )
}

export default ProductScreen;