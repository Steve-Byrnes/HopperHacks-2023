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

    const swing = await Swing.create({
        user: req.body.user,
        points: req.body.points
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