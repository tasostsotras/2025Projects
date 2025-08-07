function createSquare() {
    const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // Note: J is omitted
    const square = [];
    const used = new Set();
    
    for (let char of alphabet) {
        if (!used.has(char)) {
            square.push(char);
            used.add(char);
        }
    }
    
    return square;
}

function createKeySquare(key) {
    const square = createSquare();
    const keySet = new Set();
    const keySquare = [];

    for (let char of key.toUpperCase()) {
        if (!keySet.has(char) && square.includes(char)) {
            keySquare.push(char);
            keySet.add(char);
        }
    }

    for (let char of square) {
        if (!keySet.has(char)) {
            keySquare.push(char);
        }
    }

    return keySquare;
}

function encrypt(message, key) {
    const keySquare = createKeySquare(key);
    const rows = 5;
    const cols = 5;
    const grid = Array.from({ length: rows }, () => Array(cols).fill(''));
    
    for (let i = 0; i < keySquare.length; i++) {
        grid[Math.floor(i / cols)][i % cols] = keySquare[i];
    }

    const encryptedMessage = [];
    for (let char of message.toUpperCase()) {
        const index = keySquare.indexOf(char);
        if (index !== -1) {
            const row = Math.floor(index / cols);
            const col = index % cols;
            encryptedMessage.push('ADFGX'[row] + 'ADFGX'[col]);
        }
    }

    return encryptedMessage.join('');
}

const userMessage = prompt("Enter the message to encrypt:");
const userKey = prompt("Enter the key:");
const encrypted = encrypt(userMessage.replace(/[^A-Z]/g, ''), userKey);
console.log("Encrypted Message:", encrypted);