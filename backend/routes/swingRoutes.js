const express = require('express')
const {getSwings, setSwing, updateSwing, deleteSwing} = require('../controllers/swingController')
const router = express.Router()

router.get('/', getSwings)
router.post('/', setSwing)
router.put('/:id', updateSwing)
router.delete('/:id', deleteSwing)

module.exports = router