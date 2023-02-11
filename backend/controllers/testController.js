// npm i express-async-handler
const asyncHandler = require('express-async-handler')

const Test = require('../models/testModel')

// Description: Get Test
// Route: GET /api/tests
// Access: Private
const getTest = asyncHandler(async (req, res) => {

    const test = await Test.find()
    res.status(200).json({
        text: "get successful"
    })
})

// Description: Set Test
// Route: Post /api/tests
// Access: Private
const setTest = asyncHandler(async (req, res) => {
    // if(!req.body.text) {
    //     res.status(400)
    //     throw new Error('Please add a text field')
    // }

    // const test = await Twat.create({
    //     text: req.body.text
    // })
    res.status(200).json({
        text: "set successful"
    })
})

// Description: Update Twats
// Route: PUT /api/twats/:id
// Access: Private
const updateTest = asyncHandler(async (req, res) => {

    // const twat = await Twat.findById(req.params.id)

    // if (!twat) {
    //     res.status(400)
    //     throw new Error('Twat not found')
    // }

    // const updatedTwat = await Twat.findByIdAndUpdate(req.params.id, req.body, {new: true})
    // res.status(200).json(updatedTwat)

    res.status(200).json({
        text: "update successful"
    })

})

// Description: Delete Twats
// Route: DELETE /api/twats/:id
// Access: Private
const deleteTest = asyncHandler(async (req, res) => {

    // const twat = await Twat.findById(req.params.id)

    // if (!goal) {
    //     res.status(400)
    //     throw new Error('Twat not found')
    // }

    // await twat.remove()
    // res.status(200).json({id: req.params.id})

    res.status(200).json({
        text: "delete successful"
    })
})

module.exports = {
    getTest, 
    setTest, 
    updateTest, 
    deleteTest
}