const express = require('express')
const {getTest, setTest, updateTest, deleteTest} = require('../controllers/testController')
const router = express.Router()

router.get('/', getTest)
router.post('/', setTest)
router.put('/:id', updateTest)
router.delete('/:id', deleteTest)

module.exports = router