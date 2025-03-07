import React, { useState, useEffect } from 'react'
import axios from 'axios'

const App = () => {

  const [data, setData] = useState({})

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/api/data")
      .then(res => {
        console.log(res.data)
        setData(res.data)
      })
  }, [])


  return (

    <div>
      <h1>{data.message}</h1>
    </div>
  )
}

export default App