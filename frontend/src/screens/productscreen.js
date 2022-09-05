import React from 'react'
import {Link} from 'react-router-dom';
import { useParams } from 'react-router-dom';

import {Row, Col, Image, ListGroup, Button, Card, ListGroupItem} from 'react-bootstrap';

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
            <Image src={product.image} fluid/>
          </Col>
          <Col md={3}>
            <ListGroup variant='flush'>
              <ListGroup.Item>
                <h3>
                  {product.name}
                </h3>
              </ListGroup.Item>

              <ListGroup.Item>
                <Rating value={product.rating} text = {`${product.numReviews} Reviews`} color='#7FFF00'/>
              </ListGroup.Item>

              {/* <ListGroup.Item>
                Price: ${product.price}
              </ListGroup.Item> */}

              <ListGroup.Item>
                {product.description}
              </ListGroup.Item>
            </ListGroup>
          </Col>
          <Col md={3}>
            <Card>
              <ListGroup variant='flush'>

                <ListGroup.Item>
                  <Row>
                    <Col>
                      Price: 
                    </Col>
                    <Col>
                    <strong>
                      ${product.price}
                    </strong>
                    </Col>
                  </Row>
                </ListGroup.Item>

                <ListGroup.Item>
                  <Row>
                    <Col>
                      Status: 
                    </Col>
                    <Col>
                    <strong>
                      {product.countInStock > 0 ? 'In Stock' : 'Out of Stock'}
                    </strong>
                    </Col>
                  </Row>
                </ListGroup.Item>

                <ListGroup.Item className='d-flex justify-content-center'>
                  <Button className='btn btn-default' type='button' disabled={product.countInStock == 0}>
                    Add to Card
                  </Button>
                </ListGroup.Item>

              </ListGroup>
            </Card>
          </Col>
        </Row>
      </div>
        <Link to='/home' className='btn btn-light my-3'>Go Back</Link>
    </div>
  )
}

export default ProductScreen;