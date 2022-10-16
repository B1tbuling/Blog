async function post_like(post){
    await fetch(post + 'comment/like/')
}