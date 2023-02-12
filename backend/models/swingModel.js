const mongoose = require('mongoose')

const swingSchema = mongoose.Schema({
    user: String,
    points: [{
        time: String,
        triangle: String,
        x: String,
        y: String
    }],
}, {
    timestamps: true
})

module.exports = mongoose.model('Test', swingSchema)