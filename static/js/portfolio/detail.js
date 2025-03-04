function getYouTubeEmbed(youtubeURL) {
    const regex = /(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/)|youtu\.be\/)([^?&]+)/;
    const match = youtubeURL.match(regex);
    return match ? `<iframe width='560' height='315' src='https://www.youtube-nocookie.com/embed/${match[1]}' frameborder='0' allowfullscreen></iframe>` : null;
}

document.addEventListener('DOMContentLoaded', () => {
    const element = document.getElementById('youtube-embed-container');
    if (element) {
        const url = element.getAttribute('data-url');
        const youtube_embed = url && getYouTubeEmbed(url);
        if (youtube_embed) {
            element.innerHTML = youtube_embed;
        }
    }
});
