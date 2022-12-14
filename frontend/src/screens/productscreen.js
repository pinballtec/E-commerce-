import React, {useState, useEffect} from 'react'
import {Link} from 'react-router-dom';
// import { useParams } from 'react-router-dom';

import {Row, Col, Image, ListGroup, Button, Card, ListGroupItem} from 'react-bootstrap';

import Rating from '../components/Rating';
import products from '../products'; 
import { withRouter } from "react-router";
import axios from 'axios';

function ProductScreen({ match }) {
  // const { id } = useParams();
  const [product, setProduct] = useState([])
  // const product = products.find((p) => p._id === id)

  useEffect(()=>{
    // console.log('Use effect triggered');  
    async function fetchProduct() {

      const {data} = await axios.get(`http://127.0.0.1:8000/api/products/${match.params.id}`)
      setProduct(data)
      
    }

    fetchProduct()

  },[])
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
                  <Button className='btn btn-default' type='button' disabled={product.countInStock === 0}>
                    Add to Card
                  </Button>
                </ListGroup.Item>

              </ListGroup>
            </Card>
          </Col>
        </Row>
      </div>
        <Link to='/' className='btn btn-light my-3'>Go Back</Link>
    </div>
  )
}

export default ProductScreen;