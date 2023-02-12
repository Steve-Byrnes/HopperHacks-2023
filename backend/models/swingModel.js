const mongoose = require('mongoose')

const swingSchema = mongoose.Schema({
    user: {
        type: String,
        required: [true, 'Please add a user']
    },
    start_x: {
        type: String,
        required: [true, 'Please add a start_x']
    },
    start_y: {
        type: String,
        required: [true, 'Please add a start_y']
    },
    end_x: {
        type: String,
        required: [true, 'Please add an end_x']
    },
    end_y: {
        type: String,
        required: [true, 'Please add an end_y']
    },
    duration: {
        type: String,
        required: [true, 'Please add a duration']
    },
    angle: {
        type: String,
        required: [true, 'Please add an angle']
    },
    power: {
        type: String,
        required: [true, 'Please add a power']
    },
   }, {
    timestamps: true
   })

module.exports = mongoose.model('Swing', swingSchema)