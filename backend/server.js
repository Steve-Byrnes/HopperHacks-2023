const express = require('express')
const dotenv = require('dotenv').config()
const {errorHandler} = require('./middleware/errorMiddleware')
const connectDB = require('./config/db')
const port = process.env.PORT || 8080

connectDB()

const app = express()

app.use(express.json())
app.use(express.urlencoded({extended: false}))

app.use('/api/tests', require('./routes/testRoutes'))

app.use(errorHandler)

app.listen(port, "0.0.0.0", () => console.log(`Server started on port ${port}`))