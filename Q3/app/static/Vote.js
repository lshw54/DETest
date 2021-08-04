document.querySelectorAll('.vote_button').forEach((e) => {
    e.addEventListener('click', async (clickEvent) => {
        await fetch('/vote', {
            "headers": {
                "Content-Type": "application/json",
            },
            "body": JSON.stringify({
                "candidate": clickEvent.currentTarget.name
            }),
            "method": "POST",
        })
    })
})
