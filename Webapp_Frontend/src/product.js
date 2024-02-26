import React, { useState,useEffect } from "react";
import axios from "axios";

export default function Product(){
    const [product,setProduct]=useState([])
    const myInputRef1 = React.createRef()
    const myInputRef2 = React.createRef()
    useEffect(()=>{
        console.log("request to api")
        axios.get("http://127.0.0.1:5000/products")
        .then(response=>setProduct(response.data))
        .catch(error => {
            console.error('Error fetching data:', error);
          })
    },[]) 
    const onAddProduct=()=>{
        console.log(myInputRef1.current.value)
        console.log(myInputRef2.current.value)
        const data={
            name:myInputRef1.current.value,
            price:myInputRef2.current.value
        }
        const names = myInputRef1.current.value
        const price = myInputRef2.current.value
        if (names != "" && price != "") {
            axios.post("http://127.0.0.1:5000/products", data)
            .then((response) => {
                setProduct(response.data);
            });
            myInputRef1.current.value = null
            myInputRef2.current.value = null
        }
    }
    const onDelete=(id)=>{
        axios.delete("http://127.0.0.1:5000/products/"+id)
        .then((response) => {
            setProduct(response.data);
            console.log(id)
        })
    }
    const onUpdate=(id)=>{
        const data={
            // id:{id},
            name:myInputRef1.current.value,
            price:myInputRef2.current.value
        }
        const names = myInputRef1.current.value
        const price = myInputRef2.current.value
        if (names != "" && price != "") {
            axios.put("http://127.0.0.1:5000/products/" + id, data)
            .then((response) => {
                setProduct(response.data);
            });
            myInputRef1.current.value = null
            myInputRef2.current.value = null
        }
    }
    const show_products = product.map((item)=> {
        return (<tr key={item._id}><td>{item._id}</td><td>{item.name}</td>
        <td>{item.price}</td>
        <td><button onClick={onDelete.bind(this, item._id)}>delete</button></td>
        <td><button onClick={onUpdate.bind(this, item._id)}>OK ot Edit</button></td>
        </tr>)
    })
    return (<div>
        <table border='1'><thead><tr><td>id</td><td>name</td><td>price</td><td></td></tr></thead>
        <tbody>{show_products}</tbody>
        </table>
        Product name : <input type="text" name ='product_name' ref={myInputRef1}/>
        <br/>
        Price : <input type="text" name ='product_price' ref={myInputRef2}/>
        <br/>
        <button onClick={onAddProduct.bind(this)}>Add</button>
        {/* <button >Add</button> */}
    </div>)
}