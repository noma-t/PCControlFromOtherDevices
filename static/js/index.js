function send(category, control) {
    let result = confirm("実行しますか？\n" + category.toUpperCase() + '.' + control.toUpperCase());
    if (!result) { return; }


    let req;

    if (category === "clipboard" && control === "to_pc") {
        req = fetch(
            `/${category}/${control}`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    'content': "clipboard test"
                })
            }
        )
    } else {
        req = fetch(
        `/${category}/${control}`,
        {
                method: 'POST',
            }
        )
    }

    req.then(r => r.json()).then(data => {
        if (data.code === 1) {
            console.log(data.content);
        }
    });
}