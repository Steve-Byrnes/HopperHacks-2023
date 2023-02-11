const mongoose = require('mongoose')

mongoose.set('strictQuery', false)

const connectDB = async () => {
    const uri = "mongodb+srv://stevebyrnes:Sjb2901sjb2901sjb!@lunarcluster.ycg0vs3.mongodb.net/?retryWrites=true&w=majority"
    try {
        const conn = await mongoose.connect(uri)
        console.log(`MongoDB connected: ${conn.connection.host}`)
    } catch (error) {
        console.log(error)
        process.exit(1)
    }
}

module.exports = connectDB