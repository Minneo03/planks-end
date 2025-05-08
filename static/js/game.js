const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let player = { x: 50, y: 200, width: 30, height: 30, dy: 0, gravity: 0.5, jump: -10 };
let obstacles = [];
let score = 0;
let highScore = localStorage.getItem("highScore") || 0;  // <---- Load high score from local storage
let gameSpeed = 3;
let gameOver = false;
let gameStarted = false;
let minObstacleDistance = 150;

document.addEventListener("keydown", (e) => {
    if (e.code === "Space") {
        if (!gameStarted) {
            startGame();
        } else if (gameOver) {
            restartGame();
        } else if (player.y === 200) {
            player.dy = player.jump;
        }
    }
});

function drawPlayer() {
    ctx.fillStyle = "#419ed0";  // Character color
    ctx.fillRect(player.x, player.y, player.width, player.height);
}

function createObstacle() {
    // Checks if the last obstacle is far enough away
    if (obstacles.length > 0) {
        let lastObstacle = obstacles[obstacles.length - 1];
        if (canvas.width - lastObstacle.x < minObstacleDistance) return;
    }

    let height = Math.floor(Math.random() * 30) + 20;
    obstacles.push({ x: canvas.width, y: 200, width: 20, height: height });
}

function drawObstacles() {
    ctx.fillStyle = "#6e472a";  // Obstacle color
    obstacles.forEach((obs) => {
        ctx.fillRect(obs.x, obs.y, obs.width, obs.height);
        obs.x -= gameSpeed;

        // Player/Obstacle Collision detection
        if (player.x < obs.x + obs.width &&
            player.x + player.width > obs.x &&
            player.y < obs.y + obs.height &&
            player.height + player.y > obs.y) {
            gameOver = true;
            updateHighScore();
        }

        // Removes the offscreen obstacles
        if (obs.x + obs.width < 0) {
            obstacles.shift();
            score++;
            document.getElementById("score").innerText = `Score: ${score}`;
        }
    });
}

function updatePlayer() {
    player.dy += player.gravity;
    player.y += player.dy;
    if (player.y > 200) {
        player.y = 200;
        player.dy = 0;
    }
}

function updateGame() {
    if (gameOver) {
        ctx.fillStyle = "red";
        ctx.font = "30px Arial";
        ctx.fillText("Game Over! Press Space to Restart", canvas.width / 2 - 250, canvas.height / 2);
        return;
    }

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPlayer();
    drawObstacles();
    updatePlayer();

    // Spawn obstacles periodically with feasible spacing (make sure this is reasonable considering the player speed)
    if (Math.random() < 0.02) createObstacle();

    requestAnimationFrame(updateGame);
}

function updateHighScore() {
    if (score > highScore) {
        highScore = score;
        localStorage.setItem("highScore", highScore);  // <----- Saves the new high score to local storage
    }
    document.getElementById("highScore").innerText = `High Score: ${highScore}`;
}

function startGame() {
    gameStarted = true;
    gameOver = false;
    score = 0;
    document.getElementById("score").innerText = "Score: 0";
    updateGame();
}

function restartGame() {
    player.y = 200;
    player.dy = 0;
    obstacles = [];
    score = 0;
    gameSpeed = 3;
    gameOver = false;
    gameStarted = true;
    document.getElementById("score").innerText = "Score: 0";
    updateGame();
}

function showStartPrompt() {
    ctx.fillStyle = "blue";
    ctx.font = "30px Arial";
    ctx.fillText("Press Space to Start", canvas.width / 2 - 150, canvas.height / 2);
}

showStartPrompt();
document.getElementById("highScore").innerText = `High Score: ${highScore}`;  // Display the initial high score
