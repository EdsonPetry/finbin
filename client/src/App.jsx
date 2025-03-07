import React, { useState, useEffect } from 'react'
import axios from 'axios'

const App = () => {

  const [data, setData] = useState({})

  useEffect(() => {
    axios
     .get("http://127.0.0.1:5000/api/data")
     .then(res => {
      setData(res)
      console.log(JSON.stringify(data))
     })
  }, [])

  return (

    <div>

    </div>
  )
}

export default App