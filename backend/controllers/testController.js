// npm i express-async-handler
const asyncHandler = require('express-async-handler')

const Test = require('../models/testModel')

// Description: Get Test
// Route: GET /api/tests
// Access: Private
const getTest = asyncHandler(async (req, res) => {

    const tests = await Test.find()
    res.status(200).json(tests)
})

// Description: Set Test
// Route: Post /api/tests
// Access: Private
const setTest = asyncHandler(async (req, res) => {
    if(!req.body.text) {
        res.status(400)
        throw new Error('Please add a text field')
    }

    const test = await Test.create({
        text: req.body.text
    })
    res.status(200).json(test)
})

// Description: Update Test
// Route: PUT /api/tests/:id
// Access: Private
const updateTest = asyncHandler(async (req, res) => {

    const test = await Test.findById(req.params.id)

    if (!test) {
        res.status(400)
        throw new Error('Test not found')
    }

    const updatedTest = await Test.findByIdAndUpdate(req.params.id, req.body, {new: true})
    res.status(200).json(updatedTest)
})

// Description: Delete Twats
// Route: DELETE /api/twats/:id
// Access: Private
const deleteTest = asyncHandler(async (req, res) => {

    const tes = await Test.findById(req.params.id)

    if (!goal) {
        res.status(400)
        throw new Error('Test not found')
    }

    await test.remove()
    res.status(200).json({id: req.params.id})
})

module.exports = {
    getTest, 
    setTest, 
    updateTest, 
    deleteTest
}