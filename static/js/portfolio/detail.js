function getYouTubeEmbed(youtubeURL) {
    const regex = [
        /(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([^&]+)/,
        /(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([^?]+)/,
        /(?:https?:\/\/)?youtu\.be\/([^?]+)/
    ];
    for (const pattern of regex) {
        const match = youtubeURL.match(pattern);
        if (match) {
            const videoID = match[1];
            return `<iframe width='560' height='315' src='https://www.youtube.com/embed/${videoID}' frameborder='0' allowfullscreen></iframe>`;
        }
    }
    return null;
}

document.addEventListener('DOMContentLoaded', function() {
    const element = document.getElementById('youtube-embed-container');
    if (!element) {
        return;
    }
    const url = element.getAttribute('data-url');
    if (!url) {
        return
    }
    const youtube_embed = getYouTubeEmbed(url);
    if (youtube_embed) {
        element.innerHTML = youtube_embed;
    }
});