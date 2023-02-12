// npm i express-async-handler
const asyncHandler = require('express-async-handler')

const Swing = require('../models/swingModel')

// Description: Get Test
// Route: GET /api/swings
// Access: Private
const getSwings = asyncHandler(async (req, res) => {
    const swings = await Swing.find()
    res.status(200).json(swings)
})

// Description: Set Test
// Route: Post /api/swings
// Access: Private
const setSwing = asyncHandler(async (req, res) => {

    if(!req.body.user) {
        res.status(400)
        throw new Error('Please add a user')
    }
    if(!req.body.start_x) {
        res.status(400)
        throw new Error('Please add a start_x')
    }
    if(!req.body.start_y) {
        res.status(400)
        throw new Error('Please add a start_y')
    }
    if(!req.body.end_x) {
        res.status(400)
        throw new Error('Please add an end_x')
    }
    if(!req.body.end_y) {
        res.status(400)
        throw new Error('Please add an end_y')
    }
    if(!req.body.duration) {
        res.status(400)
        throw new Error('Please add a duration')
    }
    if(!req.body.angle) {
        res.status(400)
        throw new Error('Please add an angle')
    }
    if(!req.body.power) {
        res.status(400)
        throw new Error('Please add a power')
    }

    const swing = await Swing.create({
        user: req.body.user,
        start_x: req.body.start_x,
        start_y: req.body.start_y,
        end_x: req.body.end_x,
        end_y: req.body.end_y,
        duration: req.body.duration,
        angle: req.body.angle,
        power: req.body.power
    })
    res.status(200).json(swing)
})

// Description: Update Test
// Route: PUT /api/swings/:id
// Access: Private
const updateSwing = asyncHandler(async (req, res) => {

    const swing = await Swing.findById(req.params.id)
    if (!swing) {
        res.status(400)
        throw new Error('Swing not found')
    }

    const updatedSwing = await Swing.findByIdAndUpdate(req.params.id, req.body, {new: false})
    res.status(200).json(updatedSwing)
})

// Description: Delete Test
// Route: DELETE /api/swings/:id
// Access: Private
const deleteSwing = asyncHandler(async (req, res) => {

    const swing = await Swing.findById(req.params.id)
    await swing.remove()
    
    res.status(200).json({id: req.params.id})
})

module.exports = {
    getSwings, 
    setSwing, 
    updateSwing, 
    deleteSwing
}