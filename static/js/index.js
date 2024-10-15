function send(category, control) {
    fetch(`/${category}/${control}`, {
        method: 'POST'
    });
}