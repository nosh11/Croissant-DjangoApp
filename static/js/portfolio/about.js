const rects = [
    { x: 50, y: 100, width: 50, height: 50, dx: 5, dy: 5, time: 0, paused: false },
];

const racket = { x: 10, y: 100, width: 3, height: 50};

var point = 0;
var maxPoint = 0;

var screen_height;

document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('my-canvas');
    screen_height = canvas.height;

    // outline
    canvas.style.border = '1px solid black';
    canvas.style.display = 'block';

    const ctx = canvas.getContext('2d');

    function drawRect(rect) {
        hue = rect.time % 360;
        ctx.fillStyle = `hsl(${hue}, 100%, 50%)`;
        ctx.fillRect(rect.x, rect.y, rect.width, rect.height);
    }
    function drawRacket(racket) {
        ctx.fillStyle = 'black';
        ctx.fillRect(racket.x, racket.y, racket.width, racket.height);
    }
    function drawPoint() {
        ctx.fillStyle = 'black';
        ctx.font = '20px serif';
        ctx.fillText(`point: ${point}`, 10, 20);
        ctx.fillText(`max point: ${maxPoint}`, 10, 40);
    }

    function update() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawRacket(racket);
        
        for (let rect of rects) {
            if (!rect.paused) {
                    
                rect.time += 1;
                rect.x += rect.dx;
                rect.y += rect.dy;

                if (rect.x + rect.width > canvas.width || rect.x < 0) {
                    rect.dx *= -1;
                    if (rect.x <= 0) {
                        point = 0;
                    }
                }

                if (rect.y + rect.height > canvas.height || rect.y < 0) {
                    rect.dy *= -1;
                }

                if (rect.dx <= 0 && rect.x <= racket.x + racket.width && rect.y + rect.height >= racket.y && rect.y <= racket.y + racket.height) {
                    rect.dx *= -1;
                    point += 1;
                    maxPoint = Math.max(maxPoint, point);
                }
            }

            drawRect(rect);
            drawPoint();
        }
        requestAnimationFrame(update);
    }

    update();
});

// click event
document.addEventListener('click', function(event) {
    const canvas = document.getElementById('my-canvas');
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    for (let rect of rects) {
        if (x >= rect.x && x <= rect.x + rect.width && y >= rect.y && y <= rect.y + rect.height) {
            rect.paused = !rect.paused;
        }
    }
});

// keydown and keyup events
let keys = {};

document.addEventListener('keydown', function(event) {
    keys[event.key] = true;
    // windowが上下に動かないようにする
    if (event.key === 'ArrowUp' || event.key === 'ArrowDown') {
        event.preventDefault();
    }
});

document.addEventListener('keyup', function(event) {
    keys[event.key] = false;
});

function moveRacket() {
    if (keys['ArrowUp']) {
        racket.y -= 2;
    }
    if (keys['ArrowDown']) {
        racket.y += 2;
    }
    if (screen_height)
        racket.y = Math.max(0, Math.min(racket.y, screen_height - racket.height));
    requestAnimationFrame(moveRacket);
}

moveRacket();