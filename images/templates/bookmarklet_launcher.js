(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(
        document.createElement('script')
        ).src='https://9b57-46-53-243-118.ngrok-free.app/static/js/bookmarklet.js?r='
        + Math.floor(Math.random()*99999999999999999999);
    }
})();