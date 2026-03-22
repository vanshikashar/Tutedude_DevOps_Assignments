const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('views'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/views/index.html');
});

app.post('/submit', async (req, res) => {
    try {
        const response = await axios.post('http://backend:5000/submit', {
            name: req.body.name,
            email: req.body.email
        });

        res.send(`Response from backend: ${JSON.stringify(response.data)}`);
    } catch (error) {
        res.send("Error connecting to backend");
    }
});

app.listen(3000, () => {
    console.log("Frontend running on port 3000");
});
