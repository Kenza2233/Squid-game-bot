const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// Endpoint asas untuk Railway
app.get('/', (req, res) => {
    res.send('Bot Discord sedang berjalan!');
});

// Jalankan pelayan
app.listen(port, () => {
    console.log(`Pelayan berjalan di port ${port}`);
});
