const { Client, GatewayIntentBits } = require('discord.js');
require('dotenv').config(); // Untuk membaca token dari .env

const client = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});

// Event: Bot siap digunakan
client.once('ready', () => {
    console.log(`${client.user.tag} telah diaktifkan!`);
});

// Event: Apabila mesej dihantar
client.on('messageCreate', (message) => {
    if (message.author.bot) return; // Abaikan mesej dari bot sendiri

    if (message.content === '!ping') {
        message.reply('🏓 Pong!');
    }
});

// Log masuk menggunakan token
client.login(process.env.MTMyMjU3OTgzNTk0Nzg0MzYxNQ.G4UB9x.ZS8oPbf94_z4LfRgSD01eRvcx9M3pZ7_E8xnLI);
