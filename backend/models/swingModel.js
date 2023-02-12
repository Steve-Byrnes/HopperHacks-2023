const mongoose = require('mongoose')

const swingSchema = mongoose.Schema({
    text: {
        type: String,
        required: [true, 'Please add some text']
    }
}, {
    timestamps: true
})

module.exports = mongoose.model('Test', swingSchema)