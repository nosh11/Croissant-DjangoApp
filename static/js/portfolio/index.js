function getYoutubeId(youtubeURL) {
    const regex = [
        /(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([^&]+)/,
        /(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([^?]+)/,
        /(?:https?:\/\/)?youtu\.be\/([^?]+)/
    ];
    for (const pattern of regex) {
        const match = youtubeURL.match(pattern);
        if (match) {
            return match[1];
        }
    }
    return null;
}

function getYoutubeThumbnail(youtubeURL) {
    const videoId = getYoutubeId(youtubeURL);
    if (videoId) {
        return `https://img.youtube.com/vi/${videoId}/0.jpg`;
    }
    return null;
}

document.addEventListener('DOMContentLoaded', function() {
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    portfolioItems.forEach(function(item) {
        const url = item.getAttribute('data-url');
        const videoId = getYoutubeId(url);
        
        const image = item.getAttribute("data-img");
        if (item.getAttribute("data-img")) {
            const img = document.createElement('img');
            console.log(image);
            img.src = image;
            img.className = 'portfolio-thumbnail';
            item.appendChild(img);
        } else

        if (videoId) {
            const imageUrl = `https://img.youtube.com/vi/${videoId}/0.jpg`;
            const img = document.createElement('img');
            img.src = imageUrl;
            img.className = 'portfolio-thumbnail';
            item.appendChild(img);
        }
    });
});