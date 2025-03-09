document.addEventListener('DOMContentLoaded', function() {
    const tags = document.querySelectorAll('.portfolio-tag');
    tags.forEach(function(item) {
        if (item.getAttribute('data-color') === null) {
            return;
        }
        item.style.backgroundColor = item.getAttribute('data-color');
        item.style.outlineColor = item.getAttribute('data-color');
        const brightness = getBrightness(item.getAttribute('data-color'));
        if (brightness !== null) {
            console.log(item.getAttribute('data-color') + ' brightness: ' + brightness);
            if (brightness < 220) {
                item.style.color = 'white';
            } else {
                item.style.color = 'black';
            }
        } else {
            console.error('Invalid color format:', item.getAttribute('data-color'));
        }
    })
});


function getBrightness(color) {
    const match = color.match(/^#([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$/);
    if (match === null) {
        console.error('Invalid color format:', color);
        return null;
    }
    const rgb = match.slice(1).map((v) => parseInt(v, 16));
    return (Math.max(...rgb) + Math.min(...rgb)) / 2;
}
